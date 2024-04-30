"""
Controller for dino game
"""

import pygame
from abc import ABC, abstractmethod
from pose import CameraController


class DinoGameController(ABC):
    """
    Dino game controller super class.
    """

    def __init__(self, DinoGame):
        """
        Initialize the class.

        Parameters:
            DinoGame - the game model

        Returns:
            None
        """
        self._game = DinoGame

    @abstractmethod
    def get_input(self):
        """
        Check if the user has jumped
        """
        pass


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

    def get_restart_click(self):
        """
        Check to see if user have clicked restart button
        """
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if self._game.restart_button.collidepoint(event.pos):
                self._game.restart()

    def get_input(self):
        """
        Interpret the user input to change the model

         Returns:
             None
        """
        for event in pygame.event.get(
            (pygame.QUIT, pygame.KEYDOWN, pygame.K_d)
        ):
            if event.type == pygame.QUIT:
                self._game.quit()
            elif event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_SPACE:  # pylint: disable=no-member
                    self._game.start_game()
                    self._game.player.jump(self._game.ground)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:  # pylint: disable=no-member
            self._game.player.duck()
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

    def get_input(self):
        """
        Make the character jump user based on detected pose

         Returns:
             None
        """
        # print(pygame.event.get(pygame.USEREVENT + 3))
        self.detector.detect()
        if self.detector.is_jumping() == True and not self.jump_flag:
            self.jump_flag = True
            self._game.player.jump(self._game.ground)
        else:
            self.jump_flag = False
        if self.detector.is_ducking() == True:
            self._game.player.duck()
            duck_event = pygame.event.Event(pygame.USEREVENT + 2)
            pygame.event.post(duck_event)
        elif pygame.event.get(pygame.USEREVENT + 3) == []:
            self._game.player.unduck()
