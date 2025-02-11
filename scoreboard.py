import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Una clase para dar informaciòn de la puntuaciòn."""

    def __init__(self, ai_game):
        """Inicializa los atributos de la puntuaciòn"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.prep_ships()


        # Configuraciòn de fuente para la informaciòn de la puntuacòn.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara la imagen de la puntuaciòn inicial.
        self.prep_score()
        self.prep_hight_score()
        self.prep_level()

    def prep_level(self):
        """Convierte el nivel en una imagen renderizada."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Coloca el nivel debajo de la puntuaciòn.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_score(self):
        """Convierte la puntuaciòn en una imagen renderizada."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Muestra la puntuaciòn en la parte superior derecha de la pantalla.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_hight_score(self):
        """Convierte la puntuaciǹ màs alta en una imagen renderizada."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Centrar la puntuaciòn màs alta en la parte superior de la pantalla.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top



    def prep_ships(self):
        """Muestra cuàntas naves quedan."""
        self.ships = Group()    # Creamos una grupo vacio
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)    # Añadimos las nave una en una al grupo de ship


    def check_high_score(self):
        """Comprueba si hay una nueva puntuaciòn màs alta."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_hight_score()

    def show_score(self):
        """Dibuja la puntuaciòn en la pantalla."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)