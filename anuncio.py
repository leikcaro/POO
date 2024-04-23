from abc import ABC, abstractmethod
from error import SubTipoExeption
class Anuncio(ABC): #superclase abstracta
    
    def __init__(self, formato:str, ancho: int, alto: int, url_archivo: str= None, url_click: str= None, sub_tipo: str=None): #se pasa subtipos en la lista
        
        self.__ancho = max(1, ancho) if ancho is not None else 1
        self.__alto = max(1, alto) if alto is not None else 1
        self.__url_archivo = url_archivo 
        self.__url_click = url_click
        self.formato= formato 
        self.sub_tipo = sub_tipo
    #ancho
    @property
    def ancho (self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = nuevo_ancho if self.__alto > 0 else 1 #condiciones de 'nuevo_ancho'
    #alto
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto):
        self.__alto = nuevo_alto if self.__alto > 0 else 1 #condiciones de 'nuevo_alto'
        
        #pendiente...comentarios y docstrings
    
    #url_archivo
    @property
    def url_archivo (self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, nuevo_archivo):
        self.__url_archivo= nuevo_archivo 
    
    #url_click
    @property
    def url_click (self):
        return self.__url_click
    
    @url_click.setter
    def url_click(self, nuevo_click):
        self.__url_click= nuevo_click 

    @staticmethod
    def mostrar_formatos(formato: str, SUB_TIPOS):
        print("Los subtipos del formato: ", formato, " son:")
        for i in range(SUB_TIPOS):
            print("-",SUB_TIPOS[i])
    
    @abstractmethod
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    @abstractmethod
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
        



