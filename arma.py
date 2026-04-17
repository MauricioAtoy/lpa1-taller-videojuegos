class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio
        self.nivel = 1

    def mejorar(self):
        self.nivel += 1
        self.danio += 5