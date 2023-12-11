import lista_doble_enlazada

class artista:
    def __init__(self, nombre_artista):
        self.nombre = nombre_artista
        self.album = lista_doble_enlazada.ListaDoble()

    def mostrarInfo(self):
        print('los datos del artista o grupo son los siguientes')
        print('nombre artista o grupo:' + self.nombre)