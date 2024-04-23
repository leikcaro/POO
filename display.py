from anuncio import Anuncio

class Display(Anuncio):
    def __init__(self, ancho: int, alto: int, sub_tipo: str, url_archivo: str = None, url_click: str = None):
        super().__init__("Display", ancho, alto, url_archivo, url_click, sub_tipo)

    def comprimir_anuncio(self):

        print("Comprimiendo anuncio Display...")

    def redimensionar_anuncio(self):
        
        print("Redimensionando anuncio Display...")


