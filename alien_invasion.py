import sys    # Usamos la herramientas de sys para salir del juego cuando el jugador quiera.
import pygame    # Contiene las funcionalidad que necesitamos para crear un juego.
from settings import Settings    # Importamos settings desde Settings
from ship import Ship    # Importamos ship
from bullet import Bullet
from alien import Alien
from time import sleep    # Nos permite poner el juego en pausa cuando la nave es alcanzada
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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

        # Crea una instancia para guardar las estadìsticas del juego.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)    # Hacemos una instancia despues de crear la pantalla, requiere un argumento --> self (instancia de AlienInvasion)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
        # Inicia alien invasion en un estado inactivo.
        self.game_active = False

        # Crea el bitòn Play
        self.play_button = Button(self, "Play")


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

            if self.game_active:
                self.ship.update()
                self._update_bullets()     
                self._update_aliens()

                # self.bullets.update()
            
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Inicia un juego nuevo cuando el jugador hace click en Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Restablece las configuraciones del juego.
            self.settings.initialize_dynamic_settings()

            # Restablecer las estadisticas del juego.
            self.stats.reset_stats()
            self.game_active = True

            # Se deshace de los aliens y las balas que quedan.
            self.aliens.empty()
            self.bullets.empty()

            # Crea una flota nueva y centra la nave.
            self._create_fleet()
            self.ship.center_ship()

            self.game_active = True
            self.sb.prep_score()

            pygame.mouse.set_visible(False)

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

        # Busca colisiones alien-nav.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()


        # Se deshace de las balas que han desaparecido.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Responde a las colisiones bala-alien."""
        # Retira todas las balas y aliens que han chocado.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        if not self.aliens:
            # Destruye las balas existentes y crea un flota nueva.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
        


    def _update_aliens(self):
        """Comprueba si la flota està en un borde, despuès actualiza las posiciones."""
        self._check_fleet_edges()
        self.aliens.update()

        # BUsca colisiones alien-nave.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Busca aliens llegando al fondo de la pantall.
        self._check_aliens_bottom()



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


    def _ship_hit(self):
        """Responde al impacto de una alien en la nave."""
        # Disminuye ships_left.
        if self.stats.ship_left > 0:
            # Disminuye ships_left.
            self.stats.ship_left -= 1
            # Se deshace de los aliens y balas restantes.
            self.aliens.empty()
            self.bullets.empty()
            # Crea una flota nueva y centra la nave.
            self._create_fleet()
            self.ship.center_ship()
            # Pausa.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """Comprueba si algùn alien ha llegado al fondo de la pantalla."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Trata esto como si la nave hubiese sido alcanzada.
                self._ship_hit()
                break


    def _update_screen(self):
        """Actualiza las imàgenes en pantallas y pasa a nueva pantalla."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()    # Dibujamos la nave en la pantalla, para que la nave aparezca encima del fondo
        self.aliens.draw(self.screen)

        # Dibuja la informaciòn de la puntuaciòn.
        self.sb.show_score()


        # Dibuja el botòn para jugar si el juego està incativo.
        if not self.game_active:
            self.play_button.draw_button()

        # Hace visible la ùltima pantalla dibujada --> Esta llamada actualiza constantemente la pantalla.
        pygame.display.flip()

    def _check_fleet_edges(self):
        """Responde adecuadamente si algùn alien ha legado a un borde."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su direcciòn."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



# Creamos una instancia del juego
if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()