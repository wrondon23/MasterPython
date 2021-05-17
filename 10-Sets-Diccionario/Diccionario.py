
"""
Un diccionario es un conjunto de datos parecido a un array asociativo y/o un objeto 
tipo jSON
"""

#CREACION DE UN  DICCIONARIO 

persona ={
    "Nombre":"Wilfrido"
    ,"Apellidos": "Rondon de Jesus"
    ,"email":"wilfridorondon14@gmail.com"
    
}

#print(persona)

#print(persona["Nombre"])

#recorrer un diccionario 

#lista de diccionearios 

contatos=[
          
          {
              'nombre':'wilfrido rondon',
               'email': 'wilfrido@wilfrido.com'
              
          },
          {
              'nombre':'yadier rondon',
               'email': 'yadier@yadier.com'
              
          },
          {
              'nombre':'carlos rondon',
               'email': 'carlos@carlos.com'
              
          }
          
        
]

#print(contatos)

for contatos in contatos:
    print(contatos["nombre"])
    print(contatos['email'])
    
