"""
game.py - contains game instance classes.
"""
import pygame
import models.palette as p

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

        return True


    def run_game_logic(self):
        """
        Runs the logic for running the game.
        """
        pass


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

        # Update the screen.
        pygame.display.flip()