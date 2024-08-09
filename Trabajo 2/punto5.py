import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        area = 3.14 * (self.radio**2)
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * 3.14 * self.radio
        return perimetro
    
    def esta_en_circunferencia(self, punto):
        distancia = math.sqrt((punto[0] - self.centro[0])**2 + (punto[1] - self.centro[1])**2)
        return distancia == self.radio
    
mi_circulo = Circulo((3, 5), 6)

area_circulo = mi_circulo.calcular_area()
print("El área del círculo es: {}".format(area_circulo))

perimetro_circulo = mi_circulo.calcular_perimetro()
print("El perímetro del círculo es: {}".format(perimetro_circulo))

punto = (9, 5)
punto_pertenece = mi_circulo.esta_en_circunferencia(punto)
if punto_pertenece:
    print("El punto {} pertenece a la circunferencia".format(punto))
else:
    print("El punto {} no pertenece a la circunferencia".format(punto))

