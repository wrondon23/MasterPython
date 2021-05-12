"""
Listas(arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre
Para acceder a esos valores podemos usar un indice numero.

"""

#Definicion de lista 
Peliculas = ["Batman","Spiderman","El senor de los anillos"]
cantantes = list(("2pac","Drake","jenifer lopez"))
years = list(range(2020,2050))
variada = ["victor", 30, 4.4, True]

"""
print(Peliculas)
print(cantantes)
print(years)
print(variada)
"""

#indices
print(Peliculas[1])
print(Peliculas[-2])
print(cantantes[1:3])
print(cantantes[0:2])
print(Peliculas[1:])

#agregar elementos a una lista 
cantantes.append("kase O")

print(cantantes)

#Recorrer una lista 
print("***************Listado de Peliculas*********************")
for i in cantantes:
    print(f"{cantantes.index(i)+1}.{i}")
   

""""
print("***************INSTRODUCCION DE PELICULA*********************")

nueva_peliculas =""
while  nueva_peliculas != "exit":
    nueva_peliculas = input("Instroduce una nueva pelicula: ")
    Peliculas.append(nueva_peliculas)

for i in Peliculas:
    print(f"{Peliculas.index(i)+1}.{i}")

"""
#Listas Multidimensionales

print("\n******************Listado de Contactos*********************")

contactos = [
    [
        'Antonio', 'antonio@antonio.com'
    ],
     [
        'Luis', 'luis@luis.com'
    ],
     [
        'Salvador', 'Salvador@Salvador.com'
     ]

]

##print(contactos[1][1])

for i in contactos:
    print(i[0])

#Imprimir los elementos 
print("******************IMPRIMIR ELEMENTOS**********************")
for i in contactos:
      for elementos in i:
        print(elementos)
print("\n")      


