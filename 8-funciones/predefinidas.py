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

year = 2022 
print(year)
del year

#print(year)

#Comprobar si la variable esta vacia 

texto = "  ff  "

if len(texto) <=0:
    print("la variable esta vacia")
else:
    print(f"La variable tiene contenido: {len(texto)} ")

#Encontrar caracters de un string 

frase = "la vida es bella"
print(frase.find("vida"))

#Remplazar una palabra en un string 

nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

#convertir todo a minuscula o mayuscula en string 

print(frase.upper())
print(frase.lower())