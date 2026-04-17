import pygame

class Entidad:
    def __init__(self, x, y, vida):
        self.x = x
        self.y = y
        self.vida = vida
        self.vida_max = vida
        self.rect = pygame.Rect(x, y, 40, 40)
        self.vivo = True
        self.turno = "jugador"  # control de turnos
        self.defendiendo = False
    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vivo = False
    def dibujar_barra_vida(self, pantalla):
        ancho = 40
        alto = 5

        # calcular proporción de vida
        porcentaje = self.vida / self.vida_max

        # barra roja (fondo)
        pygame.draw.rect(pantalla, (255, 0, 0), (self.x, self.y - 10, ancho, alto))

        # barra verde (vida actual)
        pygame.draw.rect(
            pantalla,
            (0, 255, 0),
            (self.x, self.y - 10, ancho * porcentaje, alto)
        )