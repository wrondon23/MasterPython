#importar modulo base de datos sqlite

import sqlite3

#Abrir la conexion
conexion = sqlite3.connect('pruebas.db')

#crear cursor

cursor = conexion.cursor()
#Crear una tabla 

cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
               
    
    
    )")



#cerrar la conexion 
conexion.close()
