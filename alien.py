import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Una clase para representar una solo alien en la flota."""

    def __init__(self, ai_game):
        """Inicializa el alien y establece su posiciòn inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carga la imagen del alient y configura su atributo rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia un nuevo alien cerca de la parte superior izquierda de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guarda la posiciòn horizontal exacta del alien.
        self.x = float(self.rect.x)



    def check_edges(self):
        """Devuelve True si el alienigena està en el borde de la pantalla."""
        screen_rect = self.screen.get_rect()
        # Si el atributo rect es mayor o igual que el rect de la pantalla esta en el borde derecho
        # Si su valor left es menor o igual que 0, esta a la izquierda
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)


    def update(self):
        """Mueva el alien hacia la derecha o la izquierda."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    