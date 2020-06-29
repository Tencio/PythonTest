import re
import os

text= "Bomboclat Marafoka focarron"

expresionregular = '\W'

#
# 
#print(text.split())

palabras = re.split(expresionregular, text)

print(palabras) 

text = """
this is    my text wow.
But this wow, has some problems.
Python 101
A problem of problems
"""

expresion_regular = '\\W+'
#print(text.split())

#palabras = re.split(expresion_regular, text)
palabras = re.findall(r'[a-z|A-Z]+', text)
print(palabras)

numeros = re.findall(r'\d+', text)
print(numeros)

ipconfig = os.popen('ipconfig').read()
ipconfig2= re.findall('IPv4 Address.{3,}?(\d+\.\d+\.\d+)', ipconfig)

sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append(2, "Scott")
print(sampleList)