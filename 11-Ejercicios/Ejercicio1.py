"""
Crear una lista de 8 numeros enteros y hacer 
Recorrer la lista y mostrarla

"""

#lista 
numerosEnteros =[1,8,2,3,5,6,4,7]

#Recorriendo la lista y mostrarla usando una funcion
for i in numerosEnteros:
    print(i)
    
#Crear una  que recorra la lista
def numeroEntero(lista):
    for i in lista:
        print(i)
    
print("\n**************impresion por funcion*********************")
numeroEntero(numerosEnteros) 



#Ordenar y mostrar la lista 
numerosEnteros.sort()
#print(numerosEnteros)    

#monstrar longitud  de la lista

#print(len(numerosEnteros))
