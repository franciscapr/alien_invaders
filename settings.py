class Settings:
    """Una clase para guardar toda la configuraciòn de Alien Invasion."""

    def __init__(self):
        """Inicializa la configuraciòn del juego."""
        # Configuraciòn de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230)
        self.bg_color = (230, 230, 230)

        # Configuraciòn de la nave.
        # self.ship_speed = 3.0    # Cuando la nave se mueve, su posiciòn se ajusta 1.5 pixeles
        self.ship_limit = 3    # Nùmero de naves con las que se empieza a jugar

        # Configuraciòn de las balas.
        # self.bullet_speed = 2.5     # Se moveran a 2.0 pixeles de velocidad
        self.bullet_width = 3    # Anchura de 3 pixeles
        self.bullet_height = 15    # Altura de 15 pixeles
        self.bullet_color = (60, 60, 60)    # Balas de color gris
        self.bullets_allowed = 10    # Nùmero de balas permitidas -> 3 balas cada vez

        # Rapidez con la que se acelera el juego
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Configuraciòn del alien
        # self.alien_speed = 2.5    # Velocidad del alien
        self.fleet_drop_speed = 10    # Controla la velocidad a la que descience la flota, cada vez que un alien llega al borde
        # fleet_direction de 1 reprsenta derecha; -1 representa izquierda.
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """Inicializa las configuraciones que cambian durante el juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction de 1 representa la derecha; -1 representa la izquierda.
        self.fleet_direction = 1
        # Configuraciòn de puntuaciòn
        self.alien_points = 50

    def increase_speed(self):
        """Incrementa las configuraciones de valocidad"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale