


class GameStats:
    """Sigue las estadìsticas de Alien Invasiòn"""

    def __init__(self, ai_game):
        """Inicializa las estadìsticas."""
        self.settings = ai_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Inicializa las estadìsticas que pueden cambiar durante el juego."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        