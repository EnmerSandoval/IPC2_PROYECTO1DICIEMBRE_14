import lista_doble_enlazada

class album_artista:
    def __init__(self, nombre_album):
        self.nombre = nombre_album
        self.canciones = lista_doble_enlazada.ListaDoble()

    