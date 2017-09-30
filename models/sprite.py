"""
sprite.py - contains sprite classes derived from the pygame.sprite.Sprite class.
"""
import pygame


class Paddle(pygame.sprite.Sprite):
    """
    A player-controlled paddle.
    """
    def __init__(self, img: pygame.Surface):
        """
        Creates a new Paddle object.

        Args:
            img: A pygame.Surface image loaded through pygame.image.load
        """
        super().__init__()

        # Create the Paddle surface.
        width, height = img.get_width(), img.get_height()
        self.image = pygame.Surface((width, height))
        self.image.blit(img, (0, 0))

        # Save the dimensions to the rect attribute.
        self.rect = self.image.get_rect()
