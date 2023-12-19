import sys
import xml.etree.ElementTree as ET
import lista_doble_enlazada
import lista_doble_ciruclar
import artistas
import albums
import canciones
import interfaz
import playlist
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
        print(nombre_artista)
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
            el_artista.album.agregar_nodo_final(album_nuevo)
        
        el_album = el_artista.album.get(nombre_album)

        if el_album.canciones.get(nombre_cancion) is not None:
            print('ERROR!!!: La cancion ya se encuentra registrada')
        else:
            cancion_nueva = canciones.cancion(nombre_cancion,ruta_audio,nombre_artista,nombre_album)
            el_album.canciones.agregar_nodo_final(cancion_nueva)

    lista_artistas.imprimirLista()
    
    print()
    #nombre_artista_obtener = input('escriba el nombre del artista que desea ver las canciones: ')
    #mostr_canciones_artista(nombre_artista_obtener)

def mostr_canciones_artista(nombre):
    el_artista = lista_artistas.get(nombre)
    el_artista.album.imprimirLista()
    nodo_temporal1 = el_artista.album.head
    while nodo_temporal1 is not None:
        el_album = el_artista.album.get(nodo_temporal1.dato.nombre)
        el_album.canciones.imprimirLista()
        nodo_temporal1 = nodo_temporal1.siguiente

def buscar_cancion(nombre_cancion):
    nodo_temporal = lista_artistas.head
    while nodo_temporal is not None:
        el_artista = lista_artistas.get(nodo_temporal.dato.nombre)
        nombre_artista = el_artista.nombre
        nodo_temporal2 = el_artista.album.head
        while nodo_temporal2 is not None:
            el_album = el_artista.album.get(nodo_temporal2.dato.nombre)
            nombre_album = el_album.nombre
            la_cancion = el_album.canciones.get(nombre_cancion)
            if la_cancion is None:
                #no encontro la cancino y metodo get nos devulve None
                #ponemos continue para que pase al siguiente album
                nodo_temporal2 = nodo_temporal2.siguiente
            else:
                #si encuentra la cancion mandaremos los parametros a la interfaz
                interfaz.label_nombre_cancion.config(text=la_cancion.nombre)
                interfaz.label_nombre_album.config(text=nombre_album) 
                interfaz.label_nombre_artista.config(text=nombre_artista)
                interfaz.colocar_imagen_album(el_album.ruta)
                return
        nodo_temporal = nodo_temporal.siguiente
    #salio de todos los whiles, por ende ya busco en todas las canciones de todos
    #los albumes de todos los artistas y por ende no encontro nodo
    mensaje = 'No se encontro la cancion ',nombre_cancion
    interfaz.mostrar_mensaje_error(mensaje)

def buscar_cancion_para_mostrar_agregar_playlist(nombre_cancion):
    nodo_temporal = lista_artistas.head
    while nodo_temporal is not None:
        el_artista = lista_artistas.get(nodo_temporal.dato.nombre)
        nombre_artista = el_artista.nombre
        nodo_temporal2 = el_artista.album.head
        while nodo_temporal2 is not None:
            el_album = el_artista.album.get(nodo_temporal2.dato.nombre)
            nombre_album = el_album.nombre
            la_cancion = el_album.canciones.get(nombre_cancion)
            if la_cancion is None:
                #no encontro la cancino y metodo get nos devulve None
                #ponemos continue para que pase al siguiente album
                nodo_temporal2 = nodo_temporal2.siguiente
            else:
                #si encuentra la cancion mandaremos los datos solo para mostrar en el label de la creacion de playlist
                nombre_cancion = la_cancion.nombre
                datos_cancion = " / ".join([nombre_artista, nombre_album, nombre_cancion])
                
                return datos_cancion
        nodo_temporal = nodo_temporal.siguiente
    #salio de todos los whiles, por ende ya busco en todas las canciones de todos
    #los albumes de todos los artistas y por ende no encontro nodo
    mensaje = 'No se encontro la cancion ',nombre_cancion
    interfaz.mostrar_mensaje_error(mensaje)
    return None
            
def buscar_playlist(nombre_playlist):
    nodo_temporal = lista_reproduccion.primero
    if nodo_temporal is None:
        mensaje = 'No se encontro la playlist ',nombre_playlist
        interfaz.mostrar_mensaje_error(mensaje)
    while nodo_temporal.siguiente is not None:
            if nodo_temporal.valor.nombre == nombre_playlist:
                return nodo_temporal.valor
            nodo_temporal = nodo_temporal.siguiente
            if nodo_temporal is lista_reproduccion.primero:
                mensaje = 'Se reviso la base de datos y la playlist no esta creada'
                interfaz.mostrar_mensaje_error(mensaje)
                return
            
def crear_nombre_playlist(nombre_playlist):
    if nombre_playlist is None or nombre_playlist == '':
        print('valido vacio')
        mensaje = 'no se ingreso ningun texto'
        interfaz.mostrar_mensaje_error(mensaje)
        return
    if lista_reproduccion.get(nombre_playlist) is None:
        print('valido para agregar')
        playlist_nueva = playlist.lista_rep(nombre_playlist)
        lista_reproduccion.insertar(playlist_nueva)
        mensaje = 'creacion de playlist ',nombre_playlist
        interfaz.mostrar_mensaje_proceso_correcto(mensaje)
        print('Agrego nombre de playlist y la creo')
    else:
        print('valido repetido')
        mensaje = 'la playlist ',nombre_playlist,' ya esta creada'
        interfaz.mostrar_mensaje_error(mensaje)

    lista_reproduccion.imprimir()

def cargar_playlist_guardada(nombre_playlist):
    if nombre_playlist is None or nombre_playlist == '':
        print('valido vacio')
        mensaje = 'no se ingreso ningun texto'
        interfaz.mostrar_mensaje_error(mensaje)
        return None
    if lista_reproduccion.get(nombre_playlist) is None:
        print('valido que no encontro la playlist o no se ha creado')
        mensaje = 'No se encontro la playlist o no se ha creado'
        interfaz.mostrar_mensaje_error(mensaje)
        return  None
    
    la_playlist = lista_reproduccion.get(nombre_playlist)
    mensaje = 'Encontro la playlist ', nombre_playlist
    interfaz.mostrar_mensaje_proceso_correcto(mensaje)
    return la_playlist.nombre
        
def agreg_cancion_lista(nombre_plaaylist,datos_cancion):
    print()

                



        
        