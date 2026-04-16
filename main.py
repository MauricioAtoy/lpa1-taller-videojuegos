# programa principal
class Juego:
    def __init__(self):
        self.estado = "menu"  # menu, combate, dialogo, tienda
        self.jugador = Jugador()
        self.enemigos = []
    
    def actualizar(self):
        pass
    
    def dibujar(self):
        pass

class Entidad:
    def __init__(self, x, y, vida):
        self.x = x
        self.y = y
        self.vida = vida

    def mover(self):
        pass

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
