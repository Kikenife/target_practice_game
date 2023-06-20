import pygame

"""Overall class to manage the rectangle barrier"""
class Rectangle:
    def __init__(self, tp_game):
        """Initialize game resources and set a starting position for the rectangle """
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = tp_game.settings

        """Create the rectangle rect and its starting position"""
        self.rect = pygame.Rect(0, 0, self.settings.rectangle_width, self.settings.rectangle_height)
        self.center_block()

        # #Movement flag; start with a block that is not moving
        # self.moving_up = False
        # self.moving_down = False
        self.direction = 1

    def update_block(self):
        """Move the block staedily up and down"""
        #Update the decimal position of the target
        self.y += self.direction * self.settings.block_speed

        if self.rect.top < 0:
            #It's moved past the top of the screen. place at the top of the screen,
            # and chnage direction
            self.rect.top = 0
            self.direction = 1
        elif self.rect.bottom > self.screen_rect.bottom:
            #Place at bottom, and change direction.
            self.rect.bottom = self.screen_rect.bottom
            self.direction = -1

        #Update the rest of the position.
        self.rect.y = self.y

    def center_block(self):
        """Center the target on the right side of the screen."""
        self.rect.midright = self.screen_rect.midright
        
        # Store the target's position as a decimal value.
        self.y = float(self.rect.y)

    def draw_block(self):
        """Draw the rectangle to the screen"""
        pygame.draw.rect(self.screen, self.settings.rectangle_color, self.rect)



