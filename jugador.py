import pygame
from entidad import Entidad
from arma import Arma

class Jugador(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, 100)
        self.velocidad = 5
        self.arma = Arma("Espada", 10)
        self.xp = 0
        self.xp_max = 100
        self.nivel = 1
    def mover(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w]:
            self.y -= self.velocidad
        if teclas[pygame.K_s]:
            self.y += self.velocidad
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
        if teclas[pygame.K_d]:
            self.x += self.velocidad

        self.rect.topleft = (self.x, self.y)

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.arma.danio)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (0, 200, 0), self.rect)
        #dibujar barra de vida
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (0, 200, 0), self.rect)
        self.dibujar_barra_vida(pantalla) 
    def ganar_xp(self, cantidad):
        self.xp += cantidad
        print(f"+{cantidad} XP")
        # subir nivel si alcanza el máximo
        while self.xp >= self.xp_max:
            self.xp -= self.xp_max
            self.subir_nivel()

            
    def subir_nivel(self):
        self.nivel += 1
        self.xp_max += 50  # cada nivel pide más XP

        # mejoras
        self.vida_max += 20
        self.vida = self.vida_max
        self.arma.danio += 2

        print(f"¡Subiste a nivel {self.nivel}!")