class automovil():
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
         

listacoord = []

marca_auto = input("Por favor digite la marca de su vehiculo: \n")
velocidad_auto = input("Por favor digite la velocidad maxima de su vehiculo: \n")

intancia = automovil(marca_auto, velocidad_auto)

a=1
b=1

while a!= 0 and b!= 0:
    a=int(input("Por favor inserte la coordenada X: "))
    listacoord.append(a)
    b=int(input("Por favor inserte la coordenada Y: "))
    listacoord.append(b)


print(listacoord)