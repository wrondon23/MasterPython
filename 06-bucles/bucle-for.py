"""
bucle for variable in elemento interable
    bloque de instrucciones
"""

## EJMPLO UNO 
numero = 0
resultado = 0
for contador in range(0,10):
    print(f"Voy por el numero {str(contador)}")

    resultado +=  contador

print(f"El resultado es: {resultado}")


#EJEMPLO TABLAS DE MULTIPLICAR 

numero_usuario = int(input("De que numero quieres la tabla: "))
if numero_usuario < 1 :
    numero_usuario = 1

print(f"\n#### TABLA DE MULTIPLICAR DEL NUMERO: {numero_usuario}")

for numero_tabla in range(1,11):
    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos !!")
        break
    
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")

else:
    print("Tabla Finalizada")