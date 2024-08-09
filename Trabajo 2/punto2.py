import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def actualizar_coordenadas(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return distancia
    
punto1 = Punto(7, 9)
print("x1 = {} \ny1 = {}".format(punto1.x, punto1.y))

punto2 = Punto(2, 5)
print("x2 = {} \ny2 = {}".format(punto2.x, punto2.y))

distancia = punto1.calcular_distancia(punto2)
print("La distancia es {}".format(distancia))
