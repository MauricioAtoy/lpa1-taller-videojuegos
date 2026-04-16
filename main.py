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

class Jugador(Entidad):
    def __init__(self):
        super().__init__(100, 100, 100)
        self.arma = None
        self.inventario = []
        self.oro = 100
    
    def atacar (self, enemigo):
        if self.arma:
            enemigo.recibir_daño(self.arma.daño)

class enemigo (Entidad):
    def __init__(self, x, y, vida, daño):
        super().__init__(x, y, vida)
        self.daño = daño
    def atacar (self, jugador):
        jugador.recibir_daño(self.daño)

class arma:
    def __init__(self, nombre, daño, nivel=1):
        self.nombre = nombre
        self.dañi = daño
        self.nivel = nivel

    def mejorar (self):
        self.nivel += 1
        self.daño += 5