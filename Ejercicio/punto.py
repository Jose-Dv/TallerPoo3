class Punto:

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def print_cords(self):
        print("Coordenada x:",self.x,"Coordenada y:",self.y)

    def mover_cords(self, new_x: float, new_y: float):
        self.x = self.x + new_x
        self.y = self.y + new_y

    def calcular_distancia(self,new_x: float, new_y: float):
        print(((self.x - new_x)**2 + (self.y - new_y)**2)**0.5)


mi_punto = Punto(4,5)
mi_punto.print_cords()
mi_punto.mover_cords(4,5)
mi_punto.print_cords()
mi_punto.calcular_distancia(5,10)