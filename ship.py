# Importamos el mòdulo de pygame
import pygame


class Ship():
    """Una clase para gestionar la nave."""

    # Tomamos dos paràmetros self y una referencia a la clase AlienInvasion
    def __init__(self, ai_game):
        """Inicializa la nave y configura su posiciòn inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Dibuja la nave en su ubicaciòn actual."""
        self.screen.blit(self.image, self.rect)    # rect ---> nos permite tratar los elementos como rectangulos