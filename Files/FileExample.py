import csv

class Persona():
    def __init__(self, nombre, fecha_nacimineto, ID):
        self._nombre = nombre
        self._fecha_nacimineto = fecha_nacimineto
        self._id = ID
    @property
    def ID(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def fecha_nacimento(self):
        return self._fecha_nacimento


class Trabajador(Persona):
    def __init__(self, nombre, fecha_nacimineto, ID, tarifa):
        self.tarifa = tarifa
        Persona.__init__(self, nombre, fecha_nacimineto, ID)


planilla = {}
hours_worked = {}

with open("planilla.csv", newline='') as csvfile:
    planillaReader = csv.reader(csvfile, delimiter=",", quotechar="\"")
    for row in planillaReader:
        print(row)
        #['kevin,18/12/1900,1006,3,240']
        trab = Trabajador(row[0], row[1], row[2], row[3])
        planilla[row[2]] = trab
        hours_worked[row[2]] = row[4]

print(planilla)
print(hours_worked)