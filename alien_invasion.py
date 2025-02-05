import sys    # Usamos la herramientas de sys para salir del juego cuando el jugador quiera.
import pygame    # Contiene las funcionalidad que necesitamos para crear un juego.
from settings import Settings    # Importamos settings desde Settings
from ship import Ship


# Definimos una clase AlienINvasion()
class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego."""

    # Funciòn que inicializa la configuraciòn de fondo de pygame.
    def __init__(self):
        """Inicializa el juego y crea recursos."""
        pygame.init()
        # Definimos un reloj
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Creamos una ventana con display.set_mode (1200, 800), es una tupla que define las dimensiones de la ventana del juego 1200 pixeles de ancho por 800 de alto.
        # Asignamos la ventana al atributo self.screen --> para que este disponible en todos los mètodo de clase
        # Este objeto se denomina superficie
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    # Controla el juego --> contiene un bucle while
    # El bucle while --> contiene un buble de eventos y codigo para administrar las actualizaciones de la pantalla.
    # Un evento --> Es una accion que realiza el usuario en la pantalla
    def run_game(self):
        """Inicia el buble principal para el juego."""
        while True:
            # Busca eventos de teclas y ratòn
            # Con pygame.event.get() --> Obtenemos los eventos detectados por pygame
            for event in pygame.event.get():
                # Los if los utilizamos para detectar eventos especificos.
                if event.type == pygame.QUIT:
                    sys.exit()

            # Rediguja la pantalla en cada paso por el bucle.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


            # Hace visible la ùltima pantalla dibujada --> Esta llamada actualiza constantemente la pantalla.
            pygame.display.flip()
            self.clock.tick(60)    # El bucle se ejecuta 60 veces por segundo





# Creamos una instancia del juego
if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()