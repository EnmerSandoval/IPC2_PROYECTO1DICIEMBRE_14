import lista_doble_ciruclar

class lista_rep:
    def __init__(self, nombre_playlist):
        self.nombre = nombre_playlist
        self.canciones = lista_doble_ciruclar.lista_circular()

    def mostrarInfo(self):
        print('Datos de la playlist')
        print('nombre :' + self.nombre)