from datetime import date
from display import Display
from social import Social
from video import Video
class LargoExcedidoExeption(Exception):
    pass

class Campania:
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date):
        if len(nombre) >= 250:
            raise LargoExcedidoExeption("El nombre de la campaña es demasiado largo.")
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.anuncios = []

    def __str__(self):
        return f"Campaña {self.nombre} creada con éxito del {self.fecha_inicio} al {self.fecha_termino}."

    def crear_anuncio(self): #, tipo, sub_tipo, nombre, fecha_inicio):
        
        tipos_anuncio= ['display','video', 'social']
        
        #Creacion de un anuncio
        tipo_anuncio =input("Ingrese un tipo de anuncio de entre 'display','video', 'social':")

        while tipo_anuncio not in tipos_anuncio:
            tipo_anuncio= input("Ingrese el tipo de anuncio que desea añadir: ")
            if tipo_anuncio not in tipos_anuncio:
                print("El tipo de anuncio seleccionado no es válido")
                
        #Solicitar nombre, alto y ancho de anuncio
        nombre_anuncio= input("Ingrese el nombre del anuncio: ")
        alto_anuncio= int(input("Ingrese el alto de anuncio: "))
        ancho_anuncio= int(input("Ingrese el ancho de anuncio: "))
            
        if tipo_anuncio == 'display':
            subtipo_anuncio = input("Ingrese el sub-tipo de anuncio: tradicional o native: ")
            anuncio = Display(ancho_anuncio, alto_anuncio, sub_tipo=subtipo_anuncio)  # Asegúrate de que los parámetros coincidan con el constructor de Display
            print(f'Se ha creado con éxito el anuncio display {nombre_anuncio}, subtipo {subtipo_anuncio}')

        elif tipo_anuncio == 'social':
            subtipo_anuncio = input("Ingrese el sub-tipo de anuncio: facebook o linkedin: ")
            anuncio = Social(ancho_anuncio, alto_anuncio, sub_tipo=subtipo_anuncio)  # Corregido para eliminar el argumento "Social"
            print(f'se ha creado con éxito el anuncio social {nombre_anuncio}')

        elif tipo_anuncio == 'video':
            duracion = input("Ingrese la duración del video: ")
            duracion=int(duracion)
            subtipo_anuncio = input("Ingrese el sub-tipo de anuncio: instream u outstream: ")
            anuncio = Video(ancho_anuncio, alto_anuncio, duracion, sub_tipo=subtipo_anuncio)  # Asegúrate de que los parámetros coincidan con el constructor de Video
            print(f'Se ha creado con éxito el anuncio Video {nombre_anuncio}, subtipo {subtipo_anuncio}')   
        self.anuncios.append(anuncio)
        return None
