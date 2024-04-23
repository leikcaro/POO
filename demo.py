from campania import Campania

#Solicitar nombre de campaña
nombre_campaña= input("Ingrese el nombre de la campaña que desea añadir: ")
if len(nombre_campaña) >250:
    while len(nombre_campaña) >250:
        print("el nombre de campaña es muy largo")
        nombre_campaña= input("Ingrese el nombre de la campaña que desea añadir: ")
        
#Fechas de la campaña
fecha_inicio= input("ingrese la fecha de inicio de la campaña: ")
fecha_termino= input("ingrese la fecha de término de la campaña: ")

camp = Campania(nombre_campaña, fecha_inicio, fecha_termino )

print("Se ha creado con éxito la campaña ",camp)

crear_anuncio = ""
while crear_anuncio != "no":
    anuncio=camp.crear_anuncio()
    crear_anuncio=input("¿Desea crear otro anuncio? si/no ")
    
    

print ("Los anuncios creados son: ")
for i in range(len(camp.anuncios)):
    print(camp.anuncios[i].formato)