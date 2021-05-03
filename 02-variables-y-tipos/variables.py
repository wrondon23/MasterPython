"""
una variable es un contenedor de informacion
que dentro guardara un data, se pueden crear
muchas variables y que cada una tenga un dato distinto

"""

texto = "Master en Python"
texto2= "con Victor Robles"
numero = 45
decimal = 6.2

#crear variables y asginar un valor

print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------------------------")


#sustituir valores de algunas variables
numero = 77
decimal = 8.96

print(numero)
print(decimal)

print("------------------------------------------------")

#Concatenacion 

nombre = "Victor"
apellido = "Robles"
web = "vitorrobles.es"

print(nombre+" "+apellido+" - "+web)
print(f"{nombre} {apellido} - {web}")
print("hola mi nombres {} {} y mi web es {}".format(nombre,apellido,web))
