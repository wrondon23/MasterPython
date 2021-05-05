#Bucle while 

contador = 1 

while  contador <= 100:
    print(f"Esta en el numero: {contador}")

    contador += 2

print("------------------------------------------------------")

contador2 = 1 
muestrame = str(0)

while  contador2 <= 100:
    muestrame = muestrame +" , "+ str(contador2)
    contador2 += 1
   
print(muestrame)