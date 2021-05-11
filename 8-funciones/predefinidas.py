"""
Ejemplo de algunas funciones predefinidas de python
"""
#variable global
nombre = "Wilfrido Rondon"

#funciones generales 
print(nombre)

print(type(nombre))

#Detetarel tipado 
comprobar = isinstance(nombre, int)

if comprobar:
    print("Es una variable string")
else:
    print("No es un string")

#limpiar espacio de string

frase ="    mi contenido    "

print(frase)
print(frase.strip())

#eliminar variables

