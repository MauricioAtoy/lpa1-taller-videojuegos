from jugador import Jugador
from enemigo import Enemigo
import random 
import pygame
from trampa import TrampaExplosiva
class Juego:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.estado = "exploracion"

        self.jugador = Jugador(100, 100)
        self.enemigo = Enemigo(400, 300)
        self.turno = "jugador"
        self.defendiendo = False
        self.font = pygame.font.SysFont(None, 28)
        self.xp = 0
        self.xp_max = 100  # XP necesaria para subir nivel
        self.nivel = 1
        self.tiempo = 5
        self.trampas = []
    def actualizar(self):
        teclas = pygame.key.get_pressed()
        if self.estado == "exploracion":
            self.jugador.mover()
            #crear nuevo enemigo
            if self.enemigo is None:
                self.enemigo = Enemigo(
                    random.randint(0, 700),
                    random.randint(0, 500)
            )
            if self.enemigo:
                self.enemigo.mover_hacia(self.jugador)

            # detectar combate
            if self.enemigo and self.jugador.rect.colliderect(self.enemigo.rect):
                self.estado = "combate"

        elif self.estado == "combate":
            self.combate()
        if self.estado == "game_over":
            return  # detener todo
        if self.enemigo is None:
            vida = 50 + (self.nivel * 20)
            danio = 5 + (self.nivel * 2)

            self.enemigo = Enemigo(
                random.randint(0, 700),
                random.randint(0, 500)
            )

            self.enemigo.vida = vida
            self.enemigo.vida_max = vida
            self.enemigo.danio = danio
        #trampa
        for trampa in self.trampas:
            if trampa.activa:
                trampa.explotar(self.enemigo)
                trampa.tiempo -= 1
                if trampa.tiempo <= 0:
                    trampa.explotar(self.enemigo)

    def combate(self):
        if self.turno == "enemigo":

            if self.defendiendo:
                self.jugador.recibir_danio(2)
                self.defendiendo = False
            else:
                self.enemigo.atacar(self.jugador)

            self.turno = "jugador"

        if self.enemigo and self.enemigo.vida <= 0:
            print("¡Enemigo derrotado!")
            xp_ganada = 30 + (self.jugador.nivel * 10)  # cálculo de XP
            self.jugador.ganar_xp(xp_ganada) 
            self.enemigo = None
            self.estado = "exploracion"
            return

        if self.jugador.vida <= 0:
            print("Game Over")

        elif self.turno == "enemigo":

            if self.defendiendo:
                self.jugador.recibir_danio(2)  # menos daño
                self.defendiendo = False
            else:
                self.enemigo.atacar(self.jugador)

            self.turno = "jugador"
        
        if self.enemigo and self.enemigo.vida <= 0:
            print("¡Enemigo derrotado!")
    
            xp_ganada = 50  # puedes escalar luego
            self.jugador.ganar_xp(xp_ganada)

            self.enemigo = None
            self.estado = "exploracion"
            return

    # muerte del enemigo
        if self.enemigo and self.enemigo.vida <= 0:
            print("¡Enemigo derrotado!")
            xp_ganada = 30 + (self.jugador.nivel * 10) 
            self.jugador.ganar_xp(xp_ganada)
            self.enemigo = None
            self.estado = "exploracion"

    # muerte del jugador
        if self.jugador.vida <= 0:
            self.estado = "game_over"
        

    def dibujar(self):
        self.pantalla.fill((30, 30, 30))

        fuente = pygame.font.SysFont(None, 28)

        texto_xp = fuente.render(
            f"XP: {self.jugador.xp}/{self.jugador.xp_max}",
            True,
            (255, 255, 0)
        )

        self.pantalla.blit(texto_xp, (20, 80))
        self.jugador.dibujar(self.pantalla)
        if self.enemigo:  #verificar antes de dibujar
            self.enemigo.dibujar(self.pantalla)
        if self.estado == "combate":
            self.dibujar_ui()
        if self.estado == "game_over":
            self.dibujar_game_over()
            return
        fuente = pygame.font.SysFont(None, 28)

        texto_xp = fuente.render(
            f"XP: {self.jugador.xp}/{self.jugador.xp_max}",
            True,
            (255, 255, 0)
        )
        self.pantalla.blit(texto_xp, (20, 80))
        # barra XP
        #pygame.draw.rect(self.pantalla, (60,60,60), (20, 100, 200, 10)) 
        progreso = self.jugador.xp / self.jugador.xp_max
        # pygame.draw.rect(
        #     self.pantalla,
        #     (255,255,0),
        #     (20, 100, 200 * progreso, 10)

        # )
        fuente = pygame.font.SysFont(None, 30)

        texto_nivel = fuente.render(
            f"Nivel: {self.jugador.nivel}",
            True,
            (255, 255, 255)
        )

        self.pantalla.blit(texto_nivel, (20, 50))
        # dibujar trampa
        for trampa in self.trampas:
            if trampa.activa:
            # centro de la trampa
                pygame.draw.circle(
                    self.pantalla,
                    (250, 250, 250),
                    (int(trampa.x), int(trampa.y)),
                    20
                )
            # radio de explosión
                pygame.draw.circle(
                    self.pantalla,
                    (255, 200, 0),
                    (int(trampa.x), int(trampa.y)),
                    int(trampa.alcance),
                    1
                )

    

    def dibujar_barra_vida(self, pantalla):
        ancho = 40
        alto = 6

        porcentaje = self.vida / self.vida_max

        # fondo
        pygame.draw.rect(pantalla, (60, 60, 60), (self.x, self.y - 12, ancho, alto))

        # vida
        pygame.draw.rect(
            pantalla,
            (0, 200, 0),
            (self.x, self.y - 12, ancho * porcentaje, alto)
        )

    # borde
        pygame.draw.rect(
            pantalla,
            (255, 255, 255),
            (self.x, self.y - 12, ancho, alto),
            1
        )
    def manejar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            
            if evento.key == pygame.K_t and self.estado == "exploracion":
                trampa = TrampaExplosiva(
                    self.jugador.rect.centerx,
                    self.jugador.rect.centery,
                    alcance=100,
                    danio=20
                )
                self.trampas.append(trampa)
                print("Trampa colocada")
            if self.estado == "combate" and self.turno == "jugador":

                if evento.key == pygame.K_j:  # atacar
                    self.jugador.atacar(self.enemigo)
                    self.turno = "enemigo"

                elif evento.key == pygame.K_k:  # defender
                    self.defendiendo = True
                    self.turno = "enemigo"
            if self.estado == "game_over":
            
                if evento.key == pygame.K_r:
                    self.reiniciar()
    def dibujar_ui(self):
    # texto del turno
        if self.turno == "jugador":
            texto_turno = "Turno: Jugador"
        else:
            texto_turno = "Turno: Enemigo"

        texto_surface = self.font.render(texto_turno, True, (255, 255, 255))
        self.pantalla.blit(texto_surface, (20, 20))

        # instrucciones
        instrucciones = "J: Atacar   K: Defender"
        texto_instr = self.font.render(instrucciones, True, (200, 200, 200))
        # tamaño del texto
        ancho_texto = texto_instr.get_width()
        alto_texto = texto_instr.get_height()

        # tamaño pantalla
        ancho_pantalla = self.pantalla.get_width()
        alto_pantalla = self.pantalla.get_height()

        # posición abajo derecha
        x = ancho_pantalla - ancho_texto - 20
        y = alto_pantalla - alto_texto - 20

        self.pantalla.blit(texto_instr, (x, y))
        
    def dibujar_game_over(self):
        # fondo oscuro
        self.pantalla.fill((0, 0, 0))

        # texto grande
        fuente_grande = pygame.font.SysFont(None, 72)
        texto = fuente_grande.render("GAME OVER", True, (255, 0, 0))

        # centrar texto
        rect = texto.get_rect(center=(400, 250))
        self.pantalla.blit(texto, rect)

        # texto pequeño
        fuente_pequena = pygame.font.SysFont(None, 32)
        texto2 = fuente_pequena.render("Presiona R para reiniciar", True, (200, 200, 200))
        rect2 = texto2.get_rect(center=(400, 320))
        self.pantalla.blit(texto2, rect2)

    def reiniciar(self):
        self.jugador = Jugador(100, 100)
        self.enemigo = Enemigo(400, 300)
        self.estado = "exploracion"
        self.turno = "jugador"
        self.defendiendo = False