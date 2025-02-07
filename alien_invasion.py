import sys    # Usamos la herramientas de sys para salir del juego cuando el jugador quiera.
import pygame    # Contiene las funcionalidad que necesitamos para crear un juego.
from settings import Settings    # Importamos settings desde Settings
from ship import Ship    # Importamos ship
from bullet import Bullet
from alien import Alien

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

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)    # Hacemos una instancia despues de crear la pantalla, requiere un argumento --> self (instancia de AlienInvasion)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # ***** FULL SCREEN *****
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # pygame.display.set_caption("Alien Invasion")

        # Creamos una ventana con display.set_mode (1200, 800), es una tupla que define las dimensiones de la ventana del juego 1200 pixeles de ancho por 800 de alto.
        # Asignamos la ventana al atributo self.screen --> para que este disponible en todos los mètodo de clase
        # Este objeto se denomina superficie



    # Controla el juego --> contiene un bucle while
    # El bucle while --> contiene un buble de eventos y codigo para administrar las actualizaciones de la pantalla.
    # Un evento --> Es una accion que realiza el usuario en la pantalla
    def run_game(self):
        """Inicia el buble principal para el juego."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()            
            self._update_screen()

            self.clock.tick(60)    # El bucle se ejecuta 60 veces por segundo


    def _check_events(self):
        # Busca eventos de teclas y ratòn
        # Con pygame.event.get() --> Obtenemos los eventos detectados por pygame
        for event in pygame.event.get():
            # Los if los utilizamos para detectar eventos especificos.
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a pulsaciones de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a liberaciones de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.bullets_allowed:    # Si len(self.bullets) es menor a 3 -> creamos una bala nueva
            new_ballet = Bullet(self)
            self.bullets.add(new_ballet)


    def _update_bullets(self):
        """Actualiza la posiciòn de las balas y se deshace de las viejas."""
        # Actualiza las posiciones de las balas.
        self.bullets.update()

        # Se deshace de las balas que han desaparecido.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _create_fleet(self):
        """Crea la flota de alienigenas."""
        # Crea un alienìgena y va añadiendo aloenìgenas hasta que no haya espacio.
        # La distancia entre alienìgenas es equivalente al ancho de un extraterrestre.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size    # size -> contiene el ancho y alto de una elementos en este caso del alienigena

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Fila terminada; resetea valor de x e incrementa valor de y.
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """Crea un alienigena y lo coloa en la fila."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)




    def _update_screen(self):
        """Actualiza las imàgenes en pantallas y pasa a nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()    # Dibujamos la nave en la pantalla, para que la nave aparezca encima del fondo
        self.aliens.draw(self.screen)

        # Hace visible la ùltima pantalla dibujada --> Esta llamada actualiza constantemente la pantalla.
        pygame.display.flip()





# Creamos una instancia del juego
if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()