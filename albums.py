import lista_doble_enlazada

class album_artista:
    def __init__(self, nombre_album, ruta_imagen):
        self.nombre = nombre_album
        self.ruta = ruta_imagen
        self.canciones = lista_doble_enlazada.ListaDoble()

    