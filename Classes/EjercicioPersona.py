class Persona():
    #Asegrado is optional, they need to be at he end
    def __init__(self, nombre, fechanacimiento, cedula, asegurado=True):
        self._nombre = nombre
        self.fechanacimiento = fechanacimiento
        self.cedula = cedula

    #this defaults the print statement for objects of this class
    def __str__(self):
        return "Esta persona se llama: " + self._nombre
    
    #This will prevent another method to change the name, as it only can be set on the constructor itself
    @property
    def nombre(self):
        return self._nombre


class Trabajador(Persona):
    def __init__(self, nombre, fechanacimiento, cedula, tarifa):
        self.tarifa = tarifa
        Persona.__init__(self,nombre, fechanacimiento, cedula)



class Planilla():
    
    @classmethod
    def PedirDatos(cls):
        
        bandera=" "    
        dicemple = {}
        while bandera != "x":

            recinombre = input("Digite el nombre del empleado: ")

            recicedula = input("Digite el ID del empleado: ")

            recifecha = input("Digite la fecha de nacimiento del empleado: ")

            tarifa_emple = input("Digite cuanto gana el empleado por hora: ")

            recihoras = input("Digite las horas trabajadas por el empleado: ")

            bandera = input("Presione ENTER para agregar otro o X para salir... ").lower()

            trabajador1=Trabajador(recinombre, recifecha, recicedula, tarifa_emple)

            if trabajador1 not in dicemple:
                dicemple[trabajador1] = recihoras
    
        return dicemple

    @classmethod
    def Calculo(cls):
        suma1 = 0
        diclleno = Planilla.PedirDatos()
        for item in diclleno:
            sueldo = int(item.tarifa) * int(diclleno.get(item))
            suma1 += sueldo
            print("\n\nNombre: {0} ID: {1} Total a pagar: {2} \n".format(item.nombre, item.cedula, sueldo))
        print("----------------------------------------------------------- \n")
        print("Total a pagar por planilla {0} \n \n".format(suma1))

Planilla.Calculo()
