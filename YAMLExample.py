import yaml

lista = [1, 3, 6, 7, 7]

conjunto = {7, 8, 0}

diccionario = {1:'Juan', 2:'Carlos', 3: 'Frank'}

texto = yaml.dump(diccionario)

print(texto)


#Guardando un nuevo archivo YAML
with open('MiObjeto.yml', 'w') as yml_file:
    yml_file.write(yaml.dump(diccionario))


#Leyedo archivo YAML y asignandolo a una variable de impresion
with open('MiObjeto.yml' , 'r') as yml_file:
    nuevo_obj = yaml.load(yml_file, Loader=yaml.SafeLoader)

print(nuevo_obj)

