class Settings:
    """A class to store all settings fro Target Practice"""
    def __init__ (self):
        """Initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 3.0
        self.ship_limit = 3

        #rectangle settings.
        self.rectangle_width = 15
        self.rectangle_height = 120
        self.rectangle_color = (79, 69, 87)

        #block settings
        self.block_speed = 3

        # Overall game dynamics.
        self.miss_limit = 3

        #bullet settings
        self.bullet_speed = 12.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3