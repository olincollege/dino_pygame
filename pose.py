"""
This defines the classes and subclasses needed to receive cameral input

Name: Kenneth
Class: SoftDes SP24
"""

# pylint: disable=no-name-in-module
import time
from time import time
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import (
    landmark_pb2,
)


class PoseDetector:  # pylint: disable=no-member
    """
    This class uses google media pipe to detect key features on

    Attributes:
        self._image - current image detection is being run on
        self._vision_running_mode - mediapipe config for live inputs
        self._base_options - mediapipe object for model configuration
        self._options - combines previous attributes to feed to model
        self._pose_landmarks - detected points from pose detection
        self._detector - mediapipe pose detector object
    """

    def __init__(self):
        """
        Initialize PoseDetector class.

        Parameters:
            A numpy array that is input image to do detection on
        """
        self._image = []
        self._base_options = python.BaseOptions(
            model_asset_path="pose_landmarker_heavy.task"
        )
        self._vision_running_mode = mp.tasks.vision.RunningMode
        self_options = vision.PoseLandmarkerOptions(
            base_options=self._base_options,
            output_segmentation_masks=True,
            running_mode=self._vision_running_mode.LIVE_STREAM,
            result_callback=self._set_pose_landmarks_async,
        )
        self._detector = vision.PoseLandmarker.create_from_options(self_options)
        self._pose_landmarks = []

    @property
    def pose_landmarks(self):
        "Acsess the pose_landmarks property"
        return self._pose_landmarks

    def detect_landmarks(self, image):
        """
        Detect landmarks on image

         Parameters:
             image - numpy image to get the landmarks of

         Returns:
             a list of pose landmarks
        """
        self._image = image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self._detector.detect_async(mp_image, int(1000 * time()))

    def _set_pose_landmarks_async(self, result, _, __):
        """
        Async callback function to interact with results from detection

        Parameters:
            result - PoseLandmarks object containing coordiantes to pose
            features
            output_image - the output image as a mediapipe image object
            timestamp_ms - timestamp of image

        Returns:
            None
        """
        self._pose_landmarks = result.pose_landmarks

    def draw_landmarks_on_image(self):
        """
        Show the annotated image

        Parameters:
            None

        Returns:
            None
        """
        annotated_image = np.copy(self._image)

        # Loop through the detected poses to visualize.
        for _, pose_landmarks in enumerate(self._pose_landmarks):
            # Draw the pose landmarks.
            pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            pose_landmarks_proto.landmark.extend(
                [
                    landmark_pb2.NormalizedLandmark(
                        x=landmark.x, y=landmark.y, z=landmark.z
                    )
                    for landmark in pose_landmarks
                ]
            )
            solutions.drawing_utils.draw_landmarks(
                annotated_image,
                pose_landmarks_proto,
                solutions.pose.POSE_CONNECTIONS,
                solutions.drawing_styles.get_default_pose_landmarks_style(),
            )
        cv2.imshow("Annoted Image", annotated_image)
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            raise TypeError


class CameraController:  # pylint: disable=no-member
    """
    This class instantiates the openCV based contoller for the human dyno game

    Attributes:
        self._detector - PoseDetector detector
        self._capture - opencv camera object
        self._past_feet - (2, 450) numpy array of last 15 seconds of feet
        landmarks
        self._past_head - (450) numpy array of last 15 seconds of head landmarks
        self._pose_landmarks - array of pose landmarks for a given frame
    """

    def __init__(self, camera=0):
        """
        Initialize the CameraController Class

        Paramters:
            camera - an integer equal to which camera source to use

        Returns:
            None
        """
        self._detector = PoseDetector()
        self._capture = cv2.VideoCapture(camera)
        self._past_feet = np.ones((2, 450))
        self._past_head = np.zeros(450)
        self._pose_landmarks = []

    def detect(self):
        """
        Detects pose landmarks

        Parameters:
            None

        Returns:
            None
        """
        _, image = self._capture.read()
        self._detector.detect_landmarks(image)
        try:
            self._pose_landmarks = self._detector.pose_landmarks[0]
            if (  # Make sure feet are visible
                self._pose_landmarks[27].visibility < 0.4
                or self._pose_landmarks[28].visibility < 0.4
            ):
                raise IndexError
            self._past_feet = np.roll(
                self._past_feet, -1
            )  # move "frame" forward
            self._past_feet[:, -1] = np.array(
                [
                    self._pose_landmarks[27].y,
                    self._pose_landmarks[28].y,
                ]
            )
            self._past_head = np.roll(self._past_head, -1)  # same for head
            self._past_head[-1] = self._pose_landmarks[0].y
        except IndexError:
            pass
        # self._detector.draw_landmarks_on_image()  # debugging line

    def is_jumping(self):
        """
        Check if player is jumping

        Parameters:
            None

        Returns:
            True if jumping, false if not
        """
        feet_threshold = np.average(np.median(self._past_feet))
        try:
            if (  # make sure feet are visible
                self._pose_landmarks[27].visibility > 0.4
                or self._pose_landmarks[28].visibility > 0.4
            ):
                if (
                    # define threshold for jumping equal to 10 percent of image
                    self._pose_landmarks[27].y < feet_threshold - 0.07
                    and self._pose_landmarks[28].y < feet_threshold - 0.07
                ):
                    return True
            return False
        except IndexError:
            return False

    def is_ducking(self):
        """
        Check if player is ducking

        Parameters:
            None

        Returns:
            True if ducking, false if not
        """
        head_threshold = np.average(np.median(self._past_head))
        try:
            if (  # make sure feet visible so we can see the entire body
                self._pose_landmarks[27].visibility > 0.4
                or self._pose_landmarks[28].visibility > 0.4
            ):
                # define threshold for ducking equal to 5 percent of image
                if self._pose_landmarks[0].y > head_threshold + 0.07:
                    return True
            return False
        except IndexError:
            return False


if __name__ == "__main__":
    test = CameraController()
    COUNT = 0
    while True:
        test.detect()
        if test.is_jumping():
            print(f"U JUMPED{COUNT}")
            COUNT += 1
        if test.is_ducking():
            print(f"U ducked{COUNT}")
            COUNT += 1
