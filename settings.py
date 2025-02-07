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
        self.ship_speed = 1.5    # Cuando la nave se mueve, su posiciòn se ajusta 1.5 pixeles

        # Configuraciòn de las balas.
        self.bullet_speed = 2.0     # Se moveran a 2.0 pixeles de velocidad
        self.bullet_width = 3    # Anchura de 3 pixeles
        self.bullet_height = 15    # Altura de 15 pixeles
        self.bullet_color = (60, 60, 60)    # Balas de color gris