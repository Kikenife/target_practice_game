class GameStats:
    """Track statistics for the game"""

    def __init__(self, tp_game):
        """Initialize statistics"""
        self.settings = tp_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit

        self.num_misses = 0