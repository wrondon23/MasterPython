
"""
Algunas funciones predeterminada de una lista 
"""

cantantes = ["David bisbal","Eros ramazoti0","Alex bueno","Tuc Pack"]
numeros =[1,2,5,6,8,7,3]

#funcion para ordenar una lista 

numeros.sort()
print(numeros)

#funcines para agregar elementos a una lista 
cantantes.append("El lapiz")
cantantes.insert(1, "Glen adams")

print(cantantes)


#funciones para eleminar elementos

cantantes.pop(1)
cantantes.remove("El lapiz")

print(cantantes)

#Ordenar de mayor a menor una lista 
numeros.reverse()
print(numeros)

#buscar en una lista 
print("Alex bueno" in cantantes)

#Contar las veces que un elemento aparece en  una lista 
numeros.append(8)
print(numeros.count(8))

#Contar elementos de una lista 

print(len(cantantes))

#Mostrar el indice de un elemento

print(cantantes.index("Alex bueno"))

#Unir dos listas 

cantantes.extend(numeros)
print(cantantes)

