#Condifncional IF
"""
Operadores de comparacion 
== igual
!= diferente
< menor que 
> mayor que 
<= menor o igual que
>= mayor o igual que 


Operadores logicos
and  = Y
or  = O
! = Negacion
not = no

"""

print("####################### Ejemplo 1 ###########################")

color = "verde"

#color = input("Advina cual es mi color favorito:")

if color == "rojo":
    print(f"Mi color favorito es rojo")
else:
    print(f"mi color favorido no es rojo")


print("\n####################### Ejemplo 2 ###########################")

year = 2021 

#year = int(input("En que año estamos?"))

if year >= 2021:
    print("Estamos en un año mayor o igual 2021")
else :
    print ("Estamos en un año menor al 2021")

#
print("\n####################### Ejemplo 3 ###########################")

nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "Europa"
edad = 17
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
        
    if continente != "Europa":
        print("El usuario no es de Europa")
    else:
        print(f"El usuario es Europeo de la ciudad: {ciudad}")
else:
    print (f"{nombre} no es mayor de edad")


#Ejemplo 4 
print("\n####################### Ejemplo 4 ###########################")

#dia = int(input("Seleciona el numero del dia de la semana: "))

dia = 1

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print ("Es fin de semana")


#Ejemplo 5 
print("\n####################### Ejemplo 5 ###########################")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >=  18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No esta en edad de trabajar")



#Ejemplo 6
print("\n####################### Ejemplo 6 ###########################")

pais = "Alemania"

if pais == "Colombia" or pais =="Republica Dominicana" or pais == "España":
    print("Es un pais de habla hispana")
else :
    print("No es un pais de habla hispana")

