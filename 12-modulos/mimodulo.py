
def holaMundo(nombre):
    return f"hola que tal estas: {nombre}"


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