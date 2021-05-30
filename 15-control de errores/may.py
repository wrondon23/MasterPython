#capturar excepciones y manejar errrores en codigo susceptible o fallos

#Ejemplo en para el manejo de errores en python 
"""
try:
    nombre = input("Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuarios =f"El nombre es {nombre} "
    
    print(nombre_usuarios)

except:
    print("Ha ocurrido un error, mete bien el nombre")

"""
##Multiples excepciones 

try:
    numero = int(input("Numero para elevarlo al cuadrado : "))
    print(f"El cuadrado es:  {str(numero*numero)}")

except TypeError:
    print("Debes convertir tus cadenas en numeros entero")
except ValueError:
    print("Introduce un numero correcto")
    