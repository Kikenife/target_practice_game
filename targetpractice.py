import sys

import pygame

from ship import Ship
from settings import Settings
from rectangle import Rectangle
from bullet import Bullet
from button import Button
from game_stats import GameStats

class Target:
    """overall class that contronls the target game behavior"""
    def __init__(self):
        """initialize the game and create game resourses"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        """Create an instance to store game statistics"""
        self.stats = GameStats(self)

         # Make the Play button.
        self.play_button = Button(self, "Play")

        #Create instances to store game statistics.
        self.rectangle = Rectangle(self)
        self.bullets = pygame.sprite.Group()
        self.ship = Ship(self)

        #Start game in an inactive state.
        self.game_active = False

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.rectangle.update_block()  

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _start_game(self):
        """Start a new game."""
        # Reset the game statistics.
        self.stats.reset_stats()
        self.game_active = True

        # Get rid of any remaining bullets.
        self.bullets.empty()

        # Center the ship and target.
        self.ship.center_ship()
        self.rectangle.center_block()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of bullet and get rid of the old bullets.
        Also, update stats for number of misses
        """
        #update bullet positio
        self.bullets.update()

        #Get rid of the bullet that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self._increment_misses()

        self._check_bullet_target_collisions()

    def _increment_misses(self):
        """increase the number of misses, and check if the game should end"""
        self.stats.num_misses += 1
        if self.stats.num_misses >= self.settings.miss_limit:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_bullet_target_collisions(self):
        """Check whether any bullet has hit the target"""
        collisions = pygame.sprite.spritecollide(
            self.rectangle, self.bullets, True
        )

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rectangle.draw_block()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    target = Target()
    target.run_game()