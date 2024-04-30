"""
Test file for pose.py
"""

import pytest
from pose import CameraController, PoseDetector


@pytest.fixture
def camera_controller():
    """
    Create CameraController for testing
    """
    return CameraController()


@pytest.fixture
def pose_detector():
    """
    Create PoseDetector for testing
    """
    return PoseDetector()


def test_detect(capsys):
    """
    Test detect() when given no camera/one that doesn't exist.
    """
    CameraController(camera=1).detect()
    assert (
        capsys.readouterr().out.strip()
        == "Camera not loaded. Please use keyboard input"
    )


def test_is_jumping(camera_controller):  # pylint: disable=redefined-outer-name
    """
    Test when there is no valid input/pose is_jumping() returns false.
    """
    assert camera_controller.is_jumping() is False


def test_is_ducking(camera_controller):  # pylint: disable=redefined-outer-name
    """
    Test when there is no valid input/pose is_ducking() returns false.
    """
    assert camera_controller.is_ducking() is False


def test_pose_landmarks(pose_detector):  # pylint: disable=redefined-outer-name
    """
    Test that pose_landmarks = [] when nothing is detected.
    """
    assert pose_detector.pose_landmarks == []


def test_detect_landmarks(
    pose_detector, capsys
):  # pylint: disable=redefined-outer-name
    """
    Test detect_landmarks doesn't crash when not given a valid image.
    """
    pose_detector.detect_landmarks([])
    assert (
        capsys.readouterr().out.strip()
        == "Invalid value for image was inputed."
    )


def test_draw_landmarks_on_image(
    pose_detector, capsys
):  # pylint: disable=redefined-outer-name
    """
    Test draw_landmarks_on_image() doesn't crash when not given a proper input
    """
    pose_detector.draw_landmarks_on_image()
    assert capsys.readouterr().out.strip() == "Image was not present."
