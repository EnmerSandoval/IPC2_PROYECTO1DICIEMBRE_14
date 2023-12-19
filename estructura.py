import sys
import xml.etree.ElementTree as ET
import lista_doble_enlazada
import lista_doble_ciruclar
import artistas
import albums
import canciones
import interfaz
import playlist
import creacion_xml
import reporte_html

lista_artistas = lista_doble_enlazada.ListaDoble()
lista_reproduccion = lista_doble_ciruclar.lista_circular()
lista_reproducir = None
cancion_actual = None

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
            album_nuevo = albums.album_artista(nombre_album)
            el_artista.album.agregar_nodo_final(album_nuevo)
        
        el_album = el_artista.album.get(nombre_album)

        if el_album.canciones.get(nombre_cancion) is not None:
            print('ERROR!!!: La cancion ya se encuentra registrada')
        else:
            cancion_nueva = canciones.cancion(nombre_cancion,ruta_audio,nombre_artista,nombre_album,ruta_imagen)
            el_album.canciones.agregar_nodo_final(cancion_nueva)

    lista_artistas.imprimirLista()
    
    print()
    #nombre_artista_obtener = input('escriba el nombre del artista que desea ver las canciones: ')
    #mostr_canciones_artista(nombre_artista_obtener)

def obtener_texto():
    if interfaz.label_nombre_cancion.config("textvariable")[-1]:
        var = interfaz.label_nombre_cancion.config("textvariable")[-1]
        return var.get()
    else:
        return interfaz.label_nombre_cancion.config("text")[-1]
    
def mostr_canciones_playlist(nombre,cancion_actual):
    la_lista = lista_reproduccion.get(nombre)
    if cancion_actual == '..........':
        nodo_temporal1 = la_lista.canciones.primero
        if nodo_temporal1 is not None:
            la_cancion = la_lista.canciones.get(nodo_temporal1.valor.nombre)
            print('nombre de la cancion en la lista ', la_cancion.nombre)
            nombre_cancion = la_cancion.nombre
            album_cancion = la_cancion.nombre_alb
            artista_cancion = la_cancion.nombre_art
            ruta_imagen = la_cancion.ruta_album
            interfaz.label_nombre_cancion.config(text=nombre_cancion)
            interfaz.label_nombre_album.config(text=album_cancion) 
            interfaz.label_nombre_artista.config(text=artista_cancion)
            interfaz.colocar_imagen_album(ruta_imagen)
            la_cancion.aumentar_reproduccion()
            return
        else:
            mensaje = 'No hay ninguna cancion agregada a la playlist ', nombre
            interfaz.mostrar_mensaje_error(mensaje)
            return
    else:
        nodo_temporal1 = la_lista.canciones.get(cancion_actual)
        if nodo_temporal1 is not None:
            la_cancion = la_lista.canciones.get(nodo_temporal1.valor.nombre)
            print('nombre de la cancion en la lista ', la_cancion.nombre)
            nombre_cancion = la_cancion.nombre
            album_cancion = la_cancion.nombre_alb
            artista_cancion = la_cancion.nombre_art
            ruta_imagen = la_cancion.ruta_album
            interfaz.label_nombre_cancion.config(text=nombre_cancion)
            interfaz.label_nombre_album.config(text=album_cancion) 
            interfaz.label_nombre_artista.config(text=artista_cancion)
            interfaz.colocar_imagen_album(ruta_imagen)
            la_cancion.aumentar_reproduccion()
            return


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
                interfaz.colocar_imagen_album(la_cancion.ruta_album)
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
        
def agreg_cancion_lista(nombre_playlist,nombre_cancion):
    print(nombre_playlist,nombre_cancion)
    la_lista = lista_reproduccion.get(nombre_playlist)
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
                nombre_cancion_encontrada = la_cancion.nombre
                nombre_album_encontrad = nombre_album
                nombre_artista_encontrado = nombre_artista
                ruta_album_encontrada = la_cancion.ruta_album
                ruta_audio_encontrada = la_cancion.ruta
                if la_lista.canciones.get(nombre_cancion) is not None:
                    print('ERROR!!!: La cancion ya se encuentra registrada')
                    mensaje = 'la cancion ', nombre_cancion_encontrada, 'ya se encuentra en la playlist'
                    interfaz.mostrar_mensaje_error(mensaje)
                    return
                else:
                    cancion_nueva = canciones.cancion(nombre_cancion_encontrada,ruta_audio_encontrada,nombre_artista_encontrado,nombre_album_encontrad,ruta_album_encontrada)
                    la_lista.canciones.insertar(cancion_nueva)
                    mensaje = 'Se agrego la cancion ', nombre_cancion_encontrada,' y se agrego a la playlist ',nombre_playlist
                    interfaz.mostrar_mensaje_proceso_correcto(mensaje)
                    la_lista.canciones.imprimir()
                return
        nodo_temporal = nodo_temporal.siguiente
    #salio de todos los whiles, por ende ya busco en todas las canciones de todos
    #los albumes de todos los artistas y por ende no encontro nodo
    mensaje = 'No se encontro la cancion ',nombre_cancion
    interfaz.mostrar_mensaje_error(mensaje)

def colocar_cancion_display(nombre_lista):
    global lista_reproducir
    lista_reproducir = nombre_lista
    if nombre_lista == '':
        mensaje = ('No se ingreso ninguna playlist para buscar')
        interfaz.mostrar_mensaje_error(mensaje)
        return
    global cancion_actual
    cancion_actual = obtener_texto()
    mostr_canciones_playlist(nombre_lista,cancion_actual)

def cambiar_siguiente_cancion():
    print(cancion_actual)
    nueva_cancion = siguiente_cancion()
    print(nueva_cancion)
    mostr_canciones_playlist(lista_reproducir,nueva_cancion)

def siguiente_cancion():
    global cancion_actual
    cancion_actual = obtener_texto()
    la_lista = lista_reproduccion.get(lista_reproducir)
    nodo_temporal1 = la_lista.canciones.primero
    while nodo_temporal1 is not None:
        la_cancion = la_lista.canciones.get(nodo_temporal1.valor.nombre)
        print('nombre de la cancion en la lista ', la_cancion.nombre)
        if la_cancion.nombre == cancion_actual:
            nodo_temporal1 = nodo_temporal1.siguiente
            cancion_nueva = la_lista.canciones.get(nodo_temporal1.valor.nombre)
            cancion_actual = cancion_nueva.nombre
            return cancion_actual
        nodo_temporal1 = nodo_temporal1.siguiente
        if nodo_temporal1 is la_lista.canciones.primero:
            return

def mostrar_reporte_reproducidos():
    la_lista = lista_reproduccion.get(lista_reproducir)
    nodo_temporal1 = la_lista.canciones.primero
    while nodo_temporal1 is not None:
        if nodo_temporal1 is not None:
            la_cancion = la_lista.canciones.get(nodo_temporal1.valor.nombre)
            print('nombre de la cancion en la lista ', la_cancion.nombre)
            nombre_cancion = la_cancion.nombre
            album_cancion = la_cancion.nombre_alb
            artista_cancion = la_cancion.nombre_art
            ruta_imagen = la_cancion.ruta_album
            ruta_audio = la_cancion.ruta
            veces_repetida = la_cancion.retornar_reproduccion
            creacion_xml.exportar_cancion_a_xml(lista_reproducir,nombre_cancion,artista_cancion,album_cancion,veces_repetida,ruta_imagen,ruta_audio)
        nodo_temporal1 = nodo_temporal1.siguiente
        if nodo_temporal1 is la_lista.canciones.primero:
            break
    reporte_html.reporte('biblioteca_final.xml')