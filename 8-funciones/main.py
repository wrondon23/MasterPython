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


#ejmeplo tabla de multiplicar

def tablaMultiplicar(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(1,11):
        print(f"{numero} x {contador} = {numero  * contador}")

    print("\n")


for numero_tabla in range(1,11):
    tablaMultiplicar(numero_tabla)
    print("\n")


    #ejemplo asercar de los parametros opcionales

    def getEmpleados(nombre, dni = None):
        print("EMPLEADO")
        print(f"Nombre: {nombre}")

        if dni != None:
            print(f"DNI: {dni}") 

getEmpleados("wilfrido Rondon", 222542)


print ("\n")
print("EJEMPLO DE FUNCION UTILIZANDO RETURN")

def calculadora(numero1, numero2, basico = False):

    suma = numero1 +  numero2
    resta = numero1 - numero2
    multi = numero1 *  numero2
    divi = numero1 / numero2

    cadena = ""
    
    if basico == True:
        cadena += f"Suma: {str(suma)}"
        cadena += ("\n")
        cadena += f"resta: {str(resta)}"
    else:
        cadena += ("\n")
        cadena += f"Multiplicacion: {str(multi)}"
        cadena += ("\n")
        cadena += f"divicion: {str(divi)}"
     
    return cadena

print(calculadora(10,3, False))
