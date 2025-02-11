import pygame.font

class Scoreboard:
    """Una clase para dar informaciòn de la puntuaciòn."""

    def __init__(self, ai_game):
        """Inicializa los atributos de la puntuaciòn"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats


        # Configuraciòn de fuente para la informaciòn de la puntuacòn.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara la imagen de la puntuaciòn inicial.
        self.prep_score()
        self.prep_hight_score()

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


    def show_score(self):
        """Dibuja la puntuaciòn en la pantalla."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """Comprueba si hay una nueva puntuaciòn màs alta."""
        if self.stats.score > self.stats.high_score:
            self.prep_hight_score()