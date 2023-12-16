import sys
import xml.etree.ElementTree as ET
import lista_doble_enlazada
import lista_doble_ciruclar
import artistas
import albums
import canciones
lista_artistas = lista_doble_enlazada.ListaDoble()
lista_reproduccion = lista_doble_ciruclar.lista_circular()

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

def pedir_ruta():
    
    ruta_archivo = str(input('Ingrese la ruta del archivo xml: '))
    obtencion_datos(ruta_archivo)
    

def obtencion_datos(ruta):

    archivo_xml = ET.parse(ruta)
    raiz = archivo_xml.getroot()

    for datos in raiz.findall('cancion'):
        nombre_cancion = datos.get('nombre')
        nombre_artista = datos.find('artista').text.replace('"',"")
        nombre_album = datos.find('album').text.replace('"',"")
        ruta_imagen = datos.find('imagen').text.replace('"',"")
        ruta_audio = datos.find('ruta').text.replace('"',"")

        if lista_artistas.get(nombre_artista) is None:
            artista_nuevo = artistas.artista(nombre_artista)
            lista_artistas.agregar_nodo_final(artista_nuevo)
            print('agrego artista')
        
        el_artista = lista_artistas.get(nombre_artista)

        if el_artista.album.get(nombre_album) is None:
            album_nuevo = albums.album_artista(nombre_album,ruta_imagen)
            el_artista.album.añadirNodoFinal(album_nuevo)
        
        el_album = el_artista.album.get(nombre_album)

        if el_album.canciones.get(nombre_cancion) is not None:
            print('ERROR!!!: La cancion ya se encuentra registrada')
        else:
            cancion_nueva = canciones.cancion(nombre_cancion,ruta_audio)
            el_album.canciones.añadirNodoFinal(cancion_nueva)

    lista_artistas.imprimirLista()
    print()
    nombre_artista_obtener = input('escriba el nombre del artista que desea ver las canciones: ')
    mostr_canciones_artista(nombre_artista_obtener)

def mostr_canciones_artista(nombre):
    el_artista = lista_artistas.get(nombre)
    el_artista.album.imprimirLista()
    nodo_temporal1 = el_artista.album.head
    while nodo_temporal1 is not None:
        el_album = el_artista.album.get(nodo_temporal1.dato.nombre)
        el_album.canciones.imprimirLista()
        nodo_temporal1 = nodo_temporal1.siguiente
        
def agreg_cancion_lista(datos_cancion):
    print()

                



        
        