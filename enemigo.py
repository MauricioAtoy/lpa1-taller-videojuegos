import pygame
from entidad import Entidad

class Enemigo(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, 50)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (200, 0, 0), self.rect)
        self.dibujar_barra_vida(pantalla)
    def mover_hacia(self, jugador):
        if self.x < jugador.x:
            self.x += 2
        elif self.x > jugador.x:
            self.x -= 2

        if self.y < jugador.y:
            self.y += 2
        elif self.y > jugador.y:
            self.y -= 2

        self.rect.topleft = (self.x, self.y)

    def atacar(self, jugador):
        jugador.recibir_danio(5)