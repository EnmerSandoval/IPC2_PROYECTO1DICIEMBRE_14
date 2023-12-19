import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def leer_archivos_xml(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return ET.Element("biblioteca")
    else:
        try:
            tree = ET.parse(nombre_archivo)
            biblioteca = tree.getroot()
            return biblioteca
        except (FileNotFoundError, ET.ParseError):
            print(f"Error al analizar {nombre_archivo}. Se devuelve una 'biblioteca' vacía.")
            return ET.Element("biblioteca")

def exportar_cancion_a_xml(nombre_lista, nombre_cancion, nombre_artista, nombre_album, veces_repetida, ruta_imagen, ruta_audio):
    try:
        tree = ET.parse("biblioteca_final.xml")
        biblioteca = tree.getroot()
    except (FileNotFoundError, ET.ParseError):
        tree = ET.ElementTree(ET.Element("biblioteca"))
        biblioteca = tree.getroot()
    
    nombrelista_elem = ET.SubElement(biblioteca, "nombreLista", nombre=nombre_lista)

    cancion_elem = ET.SubElement(nombrelista_elem, "cancion")
    cancion_elem.text = nombre_cancion

    artista_elem = ET.SubElement(nombrelista_elem, "artista")
    artista_elem.text = nombre_artista

    album_elem = ET.SubElement(nombrelista_elem, "album")
    album_elem.text = nombre_album

    imagen_elem = ET.SubElement(nombrelista_elem, "imagen")
    imagen_elem.text = ruta_imagen

    ruta_elem = ET.SubElement(nombrelista_elem, "ruta")
    ruta_elem.text = ruta_audio

    veces_reproducida_elem = ET.SubElement(nombrelista_elem, "vecesReproducida")
    veces_reproducida_elem.text = str(veces_repetida)

    xml_str = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml(indent="  ")

    with open("biblioteca_final.xml", "w", encoding="utf-8") as xml_file:
        xml_file.write(xml_str)