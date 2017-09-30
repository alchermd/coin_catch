"""
sprite.py - contains sprite classes derived from the pygame.sprite.Sprite class.
"""
import pygame


class Paddle(pygame.sprite.Sprite):
    """
    A player-controlled paddle.
    """
    def __init__(self, img: pygame.Surface, screen: pygame.Surface):
        """
        Creates a new Paddle object.

        Args:
            img: A pygame.Surface image loaded through pygame.image.load
            screen: A pygame.Surface where the Paddle is to be drawn.
        """
        super().__init__()
        self.screen = screen

        # Create the Paddle surface.
        width, height = img.get_width(), img.get_height()
        self.image = pygame.Surface((width, height))
        self.image.blit(img, (0, 0))

        # Save the dimensions to the rect attribute.
        self.rect = self.image.get_rect()

        self.x_speed = 0


    def update(self):
        self.rect.x += self.x_speed

        # Prevent going out of bounds.
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= self.screen.get_width() - self.image.get_width():
            self.rect.x = self.screen.get_width() - self.image.get_width()
