

"""
Variables locales: Se definen dentro de la funcion y no 
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return

Variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas.

"""

#variable goblal

frase = " Ni los genios son tan genios, ni  los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase ="Hola mundo!!"
    print(frase)

holaMundo()