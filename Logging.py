import logging as lg

lg.basicConfig(filename='mylog.log', level=lg.DEBUG)

miLog = lg.getLogger
miLog.debug("Excepcion en debug")
milog.critical("Excepcion en Critical")

try:
    numero = 0
    numero1 = numero/0
except ZeroDivisionError as VariableExcepcion:
    print("F"+str(VariableExcepcion))
else:
    print("Paso algo raro")
finally:
    print("Terminando el proceso")