"""
Modulos: son funcionalidades ya hechas para reutilizar.
en python por defectos hay muchos modulos que estan en python modulos index

"""
#importar un modulo propio
import mimodulo
#from mimodulo import holaMundo
#from mimodulo import *


print(mimodulo.holaMundo("wilfrido"))

print(mimodulo.calculadora(25,18, True))

#importar modulo de fecha en python

import datetime as dt

print(dt.date.today())

#################################################################################
#modulo de fecha en python
#imprimir fecha
fecha_completa = dt.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y")

print(fecha_personalizada)

##################################################################################

#Modulo Matematicas python

import math

print("Raiz cuadara de 10", math.sqrt(10))

print("Sacar el numero pi", float(math.pi))

print("Redondear ",math.ceil(6.554557896))

#modulo numero aleatoreos

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))