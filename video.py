from anuncio import Anuncio

class Video(Anuncio):
    #definicion de formato de los anuncios, en video y en dos subtipos; 'instream' y 'outstream'
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, ancho: int, alto: int, duracion, sub_tipo: str, url_archivo: str=None , url_clic: str=None):
        # funcion integrada de Python que permite acceder a los métodos y atributos de la superclase 'Anuncio'.
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo) 
        # atributos de los objetos de la superclase 'Anuncio'
        self.__alto = int(1)
        self.__ancho = int(1)
        self.__duracion = max(5, duracion) # configuracion de la duracion del video
        
    @property
    def ancho(self, ):
        return self.__ancho
    
    @ancho.setter #configuracion de nuevas dimensiones de ancho en 'nuevo_ancho'
    def ancho(self, nuevo_ancho): 
        pass
    @property
    def alto(self, ):
        return self.__alto

    @alto.setter #configuracion de nuevas dimensiones de alto en 'nuevo_alto'
    def alto(self, nuevo_alto):
        pass
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

