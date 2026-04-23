class TrampaExplosiva:
    def __init__(self, x, y, alcance, danio):
        self.x = x
        self.y = y
        self.alcance = alcance
        self.danio = danio
        self.activa = True
        self.tiempo = 5
    def explotar(self, enemigo):
        if not self.activa or enemigo is None:
            return

        distancia = ((self.x - enemigo.x)**2 + (self.y - enemigo.y)**2) ** 0.5

        if distancia <= self.alcance:
            enemigo.recibir_danio(self.danio)
            print("Trampa explotó")

        self.activa = False