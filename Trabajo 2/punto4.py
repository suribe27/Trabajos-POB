class Rectangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def es_cuadrado(self):
        return self.lado_a == self.lado_b

    def calcular_perimetro(self):
        perimetro = 2 * (self.lado_a + self.lado_b)
        return perimetro
    
    def calcular_area(self):
        area = self.lado_a * self.lado_b
        return area

mi_rectangulo = Rectangulo(7, 10)
print("Lado A: {}, Lado B: {}".format(mi_rectangulo.lado_a, mi_rectangulo.lado_b))

if mi_rectangulo.es_cuadrado():
    print("Es un cuadrado")
else:
    perimetro_rectangulo = mi_rectangulo.calcular_perimetro()
    print("El perímetro del rectángulo es {}".format(perimetro_rectangulo))

    area_rectangulo = mi_rectangulo.calcular_area()
    print("El área del rectángulo es: {}".format(area_rectangulo))
