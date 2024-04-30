"""
Controller for dino game
"""

from abc import ABC, abstractmethod
import pygame
from pose import CameraController


class DinoGameController(ABC):
    """
    Dino game controller super class.
    """

    def __init__(self, DinoGame):  # pylint: disable=invalid-name
        """
        Initialize the class.

        Parameters:
            DinoGame - the game model

        Returns:
            None
        """
        self._game = DinoGame

    @property
    def game(self):
        """
        Get the _game property

        Returns:
            DinoGame
        """
        return self._game

    @abstractmethod
    def get_input(self):
        """
        Check if the user has inputed a jump or duck
        """

    @abstractmethod
    def get_restart(self):
        """
        Check if the user has requested to restart
        """


class KeyboardDinoGameController(DinoGameController):
    """
    Keyboard based controller for dino game
    """

    def jump(self):
        """
        Make the character jump when the user has pressed space

         Returns:
             None
        """

    def get_restart(self):
        """
        Check to see if user has clicked restart button.
        """
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if self._game.restart_button.collidepoint(event.pos):
                self._game.restart()

    def get_input(self):
        """
        Interpret the user keyboard input to affect model

         Returns:
             None
        """
        for event in pygame.event.get(  # filter by specific event
            (pygame.QUIT, pygame.KEYDOWN, pygame.K_d)
        ):
            if event.type == pygame.QUIT:  # Exit game
                self._game.quit()
            elif event.type == pygame.KEYDOWN:  # Check for jump duck
                if event.key == pygame.K_SPACE:
                    self._game.start_game()
                    self._game.player.jump(self._game.ground)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self._game.player.duck()
            # publishes event so vision controller doesnt force unduck
            duck_event = pygame.event.Event(pygame.USEREVENT + 3)
            pygame.event.post(duck_event)
        elif pygame.event.get(pygame.USEREVENT + 2) == []:
            self._game.player.unduck()


class CameraDinoGameController(DinoGameController):
    """
    Opencv and mediapipe based controller for dino game
    """

    def __init__(self, DinoGame):
        super().__init__(DinoGame)
        self.detector = CameraController()
        self.jump_flag = False

    def get_restart(self):
        """
        Check if the user has jumped to restart the game
        """
        self.detector.detect()
        if self.detector.is_jumping() and not self.jump_flag:
            self.jump_flag = True  # stops constant jump input while in air
            self._game.player.jump(self._game.ground)
            self._game.restart()
        else:
            self.jump_flag = False

    def get_input(self):
        """
        Make the character jump based on user detected pose

         Returns:
             None
        """
        # print(pygame.event.get(pygame.USEREVENT + 3))
        self.detector.detect()
        if self.detector.is_jumping() and not self.jump_flag:
            self.jump_flag = True  # stops constant jump input while in air
            self._game.player.jump(self._game.ground)
        else:
            self.jump_flag = False
        if self.detector.is_ducking():
            self._game.player.duck()
            # publishes event so keyboard controller doesnt force unduck
            duck_event = pygame.event.Event(pygame.USEREVENT + 2)
            pygame.event.post(duck_event)
        elif pygame.event.get(pygame.USEREVENT + 3) == []:
            self._game.player.unduck()
