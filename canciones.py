class cancion:
    def __init__(self, nombre_cancion, ruta_audio,nombre_artista, nombre_album):
        self.nombre = nombre_cancion
        self.ruta = ruta_audio
        self.nombre_art = nombre_artista
        self.nombre_alb = nombre_album
        self.reproducciones = 0

    def aumentar_reproduccion(self):
        self.reproducciones += 1
    
    def retornar_reproduccion(self):
        return self.reproducciones
        