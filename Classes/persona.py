class Persona():
    #Asegrado s optional, they need to be at he end
    def __init__(self, nombre, fechanacimiento, cedula, asegurado=True):
        self._nombre = nombre
        self.fechanacimiento = fechanacimiento
        self.cedula = cedula

    #this defaults the print statement for objects of this clas
    def __str__(self):
        return "Esta persona se llama: " + self._nombre
    
    #This will prevent another method to change the name, as it only can be set on the constructor itself
    @property
    def nombre(self):
        return self._nombre
.

class Trabajador(Persona):
    def __init__(self, nombre, fechanacimiento, cedula, tarifa):
        self.tarifa = tarifa



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

            recihoras = input("Digite las horas trabajadores el empleado: ")

            bandera = input("Presione ENTER para agregar otro o X para salir... ").lower()

            trabajador1=Trabajador(recinombre, recicedula, recifecha, tarifa_emple)

            if trabajador1 not in dicemple:
                dicemple[trabajador1] = recihoras
    
        return dicemple

    @classmethod
    def Calculo(cls):

        diclleno = Planilla.PedirDatos()

        for item in diclleno:
            sueldo = item.tarifa * diclleno.get(item)
            suma1 += sueldo
            print("Nombre: {0} ID: {1} Total a pagar: {1} \n\n".format(item.nombre, item.cedula, sueldo)


            