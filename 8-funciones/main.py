"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo 
un nombre concreto que pueden reutilizarse invocando a la
funcion tantas veces como sea necesaria
"""

#ejemplo 1
print("#### EJMEPLO 1 ######")

#Definir la funcion
def imprimirNombre():
    print("Wilfrido")
    print("Pedro")
    print("Juan")
    print("Carlos")
    print("\n")


#invocar  funcion 
imprimirNombre()


#ejemplo 2
print("#### EJMEPLO 2 ######")

def mostrarTuNombre(nombre):
    print(f"Tu nombre es : {nombre}")


nombre = input("Cual es tu nombre :")
mostrarTuNombre(nombre)


#ejemplo 3
print("#### EJMEPLO 2 ######")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es : {nombre}")

    if edad >= 18:
        print(" Y eres mayor de edad")
    else :
        print("Y eres menor de edad")


nombre = input("Cual es tu nombre: ")
edad = int(input("Cual es tu edad: "))
mostrarTuNombre(nombre, edad)