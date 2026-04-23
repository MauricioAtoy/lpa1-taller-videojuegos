import pygame
from juego import Juego

pygame.init()
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego 2D POO")

clock = pygame.time.Clock()

juego = Juego(pantalla)

ejecutando = True
while ejecutando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        juego.manejar_eventos(evento)

    juego.actualizar()
    juego.dibujar()

    pygame.display.flip()

pygame.quit()
        

        
