class carro:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

auto1= carro(180,14000)
print("La velocidad maxima es {} km/h".format (auto1.velocidad_maxima))
print("El kilometraje del carro es {}".format (auto1.kilometraje))

