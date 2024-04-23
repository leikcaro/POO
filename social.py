from anuncio import Anuncio

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def __init__(self, ancho: int, alto: int, sub_tipo: str, url_archivo: str= None, url_clic: str= None): #definicion de atributos de la superclase 'Anuncio' en el constructor
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo) #ejecutar atributos de superclase 'Anuncio'

    def comprimir_anuncio(self, ):
        print("COMPRESIÓN DE ANUNCIOS SOCIAL NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self, ):
        print("REDIMENSIÓN DE ANUNCIOS SOCIAL NO IMPLEMENTADA AÚN")

