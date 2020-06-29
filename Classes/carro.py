class carro:
    def __init__(self, motor):
        self.motor = motor

    def acelerar(self, tiempo, intensidad):
        self.motor.acelerar(tiempo, intensidad)


class motor:
    def __init__(self, tipo):
        self.tipo = tipo


    def acelerar(self, tiempo, intensidad):
        print("Estoy acelerando por "+ str(tiempo) +" segundos, a una intensidad de "+intensidad)


diesel = motor("diesel")

jeep = carro(diesel)

jeep.acelerar(10, "alta")