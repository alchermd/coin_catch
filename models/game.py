"""
game.py - contains game instance classes.
"""
import pygame
import os
import random
import models.palette as p
from models.sprite import Paddle, Coin

class Game(object):
    """
    Represents the framework for a Pygame project.
    """
    def __init__(self, screen: pygame.Surface, bg_img: pygame.Surface):
        self.screen = screen
        self.bg_img = bg_img

        # Scoring system.
        self.score = 0
        score_font = pygame.font.Font(None, 30)
        self.score_text = score_font.render("SCORE: {}".format(self.score), True, p.black)

        # Create sprite groups.
        self.all_sprites = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        # Resolve path for paddle image.
        paddle_path = os.path.join("../", os.getcwd(), "assets/image/paddle.png")
        paddle_img = pygame.image.load(paddle_path).convert()

        # Create player's paddle object.
        self.paddle = Paddle(paddle_img, self.screen)
        self.all_sprites.add(self.paddle)

        # Set the starting position of the paddle.
        self.paddle.rect.x = self.screen.get_width() / 2 - self.paddle.image.get_width() / 2
        self.paddle.rect.y = self.screen.get_height() - self.paddle.image.get_height()

        # Generate some coins.
        for i in range(50):
            # Resolve path for coin image.
            coin_path = os.path.join("../", os.getcwd(), "assets/image/coin.png")
            coin_img = pygame.image.load(coin_path).convert()
            
            # Create a new coin object.
            new_coin = Coin(coin_img, self.screen)
            new_coin.image.set_colorkey(p.black)

            # Set coin location randomly.
            new_coin.rect.x = random.randrange(self.screen.get_width() - new_coin.image.get_width())
            new_coin.rect.y = random.randrange(-(self.screen.get_height() // 2), self.screen.get_height() // 2)

            # Save coin to sprite groups.
            self.all_sprites.add(new_coin)
            self.coins.add(new_coin)

    def handle_events(self) -> bool:
        """
        Processes the events in the Pygame event queue.

        Returns:
            A boolean value indicating whether the game is still
            processing events or not.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            # Adjust the paddle position depending on key pressed.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.paddle.x_speed = -5

                if event.key == pygame.K_RIGHT:
                    self.paddle.x_speed = 5
                
            # Stop the motion of the paddle on key release.
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.paddle.x_speed = 0

            
        return True


    def run_game_logic(self):
        """
        Runs the logic for running the game.
        """
        self.all_sprites.update()


    def display_frame(self, screen: pygame.Surface=None):
        """
        Updates the Pygame display.

        Args:
            screen: Pygame surface to draw on.
        """
        if screen is None:
            screen = self.screen

        # Draw the background.
        screen.blit(self.bg_img, (0, 0))

        # Draw the scoreboard.
        screen.blit(self.score_text, (10, 10))

        # Draw the sprites.
        self.all_sprites.draw(screen)

        # Update the screen.
        pygame.display.flip()