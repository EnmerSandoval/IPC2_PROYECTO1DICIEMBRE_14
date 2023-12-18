import tkinter as Tk
from tkinter import filedialog, Canvas, messagebox
from PIL import Image, ImageTk
import estructura

def buscar_archivo():
    archivo = filedialog.askopenfilename()
    if archivo.endswith('.xml'):
        # Cargar biblioteca
        estructura.obtencion_datos(archivo)
    else:
        # Mostrar mensaje de error
        print("Error: El archivo seleccionado no es un archivo '.xml'")

def cargar_biblioteca():
    buscar_archivo()

def reproducir_cancion():
    print("Reproduciendo...")
    estructura.buscar_cancion('Cancion prueba')

def parar_cancion():
    print("Deteniendo...")

def pausar_cancion():
    print("Pausando...")

def siguiente_cancion():
    print("siguiente...")

def anterior_cancion():
    print("anterior...")

def mostrar_mensaje_error(mensaje):
    messagebox.showerror('Error: ', mensaje)

def colocar_imagen_album(ruta):
    global imagen_logo, resized_logo, logo_imagen
    imagen_logo = Image.open(ruta)
    resized_logo = imagen_logo.resize((250, 250))
    logo_imagen = ImageTk.PhotoImage(resized_logo)
    canvas_imagen.delete()
    canvas_imagen.create_image(0, 0, anchor='nw', image=logo_imagen)
    canvas_imagen.pack()
    
root = Tk.Tk()
root.title("MP3 Player")

# Configurar el tamaño de la ventana antes de llamar a mainloop()
root.geometry("900x400")

# Desactivar la capacidad de cambiar el tamaño de la ventana
root.resizable(0, 0)

# Variables
nombre_cancion = 'nombre cancion'
nombre_artista = 'nombre artista'
nombre_album = 'nombre album'

# Crear menu
menu = Tk.Menu(root)
root.config(menu=menu)

# Crear opciones del menu
menu_archivo = Tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Cargar biblioteca", command=cargar_biblioteca)
menu_archivo.add_command(label="Crear playlist por cancion")
menu_archivo.add_command(label="Crear playlist por artistas")
menu_archivo.add_command(label="Mostrar más reproducidos")
menu_archivo.add_command(label="Mostrar reporte de biblioteca")

# Frames
frame_principal = Tk.Frame(root, bg='#81F7BE')
frame_principal.place(x=0, y=0, width=900, height=400)

frame_secundario = Tk.Frame(frame_principal, bg='#81BEF7')
frame_secundario.place(x=50, y=50, width=800, height=325)

frame_info_cancion = Tk.Frame(frame_secundario, bg='#E0E6F8')
frame_info_cancion.place(x=350, y=100, width=400, height=150)

frame_imagen_album = Tk.Frame(frame_secundario, bg='#81BEF7')
frame_imagen_album.place(x=50, y=50, width=250, height=250)
canvas_imagen = Canvas(frame_imagen_album, width=250, height=250)
canvas_imagen.pack()
imagen_logo = Image.open('logo.png')
resized_logo = imagen_logo.resize((250, 250))
logo_imagen = ImageTk.PhotoImage(resized_logo)
canvas_imagen.create_image(0, 0, anchor='nw', image=logo_imagen)

# label cancion
label_cancion = Tk.Label(frame_info_cancion, text="Cancion", font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_cancion.place(x=0, y=0, anchor="nw")

# label artista
label_artista = Tk.Label(frame_info_cancion, text="Artista", font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_artista.place(x=0, y=50, anchor="nw")

# label album
label_album = Tk.Label(frame_info_cancion, text="Album", font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_album.place(x=0, y=100, anchor="nw")

# label nombre cancion
label_nombre_cancion = Tk.Label(frame_info_cancion, text=nombre_cancion, font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_nombre_cancion.place(x=150, y=0, anchor="nw")

# label nombre artista
label_nombre_artista = Tk.Label(frame_info_cancion, text=nombre_artista, font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_nombre_artista.place(x=150, y=50, anchor="nw")

# label nombre album
label_nombre_album = Tk.Label(frame_info_cancion, text=nombre_album, font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_nombre_album.place(x=150, y=100, anchor="nw")

# Controls Frame

# Play Button
image_play = Image.open('play.png')
resized_play = image_play.resize((50, 50))
play_image = ImageTk.PhotoImage(resized_play)
Tk.Button(frame_secundario,image=play_image,command=reproducir_cancion,bg='#81BEF7',highlightthickness=0).place(x=400, y=35, width=50, height=50)


# Pause Button
image_pause = Image.open('pause.png')
resized_pause = image_pause.resize((50,50))
pause_image = ImageTk.PhotoImage(resized_pause)
Tk.Button(frame_secundario,image=pause_image,command=pausar_cancion,bg='#81BEF7',highlightthickness=0).place(x=525, y=35, width=50, height=50)

# Stop Button
image_stop = Image.open('stop.png')
resized_stop = image_stop.resize((40,40))
stop_image = ImageTk.PhotoImage(resized_stop)
Tk.Button(frame_secundario,image=stop_image, command=parar_cancion,bg='#81BEF7',highlightthickness=0).place(x=650, y=35, width=50, height=50)

# next Button
image_next = Image.open('next.png')
resized_next = image_next.resize((40,40))
next_image = ImageTk.PhotoImage(resized_next)
Tk.Button(frame_secundario,image=next_image,command=siguiente_cancion,bg='#81BEF7',highlightthickness=0).place(x=475, y=265, width=50, height=50)

# back Button
image_back = Image.open('back.png')
resized_back = image_back.resize((40,40))
image_back = ImageTk.PhotoImage(resized_back)
Tk.Button(frame_secundario,image=image_back, command=anterior_cancion,bg='#81BEF7',highlightthickness=0).place(x=600, y=265, width=50, height=50)

root.mainloop()