import clase

persona = clase.Informatico()
persona.setNombre("Victor")
persona.setApellido("Robles")
persona.setAltura("190 cm")
persona.setEdad("20 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellido()}\n altura : {persona.getAltura()}\n edad: {persona.getEdad()}\n legunajes: {persona.getLenguajes()}")