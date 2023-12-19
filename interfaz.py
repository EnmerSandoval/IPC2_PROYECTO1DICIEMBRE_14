import tkinter as Tk
from tkinter import filedialog, Canvas, messagebox
from PIL import Image, ImageTk
import estructura


#uso de variables para que varios metodos accedan a ellas
label_rectangular_global = None
entry_buscar_cancion_global = None
entry_buscar_playlist_global = None
dato = None
dato_playlist = None
nombre_playlist_almacenada = None

#metodos

#metodo para buscar el archivo
def buscar_archivo():
    archivo = filedialog.askopenfilename()
    if archivo.endswith('.xml'):
        # Cargar biblioteca
        estructura.obtencion_datos(archivo)
    else:
        # Mostrar mensaje de error
        print("Error: El archivo seleccionado no es un archivo '.xml'")

#metodo de archivo-cargar biblioteca
def cargar_biblioteca():
    buscar_archivo()

#metodo para reproducir cancion y contar reproduccion
def reproducir_cancion():
    print("Reproduciendo...")
    estructura.buscar_cancion('Cancion prueba')

#metodo para detener cancion y quitar todos los datos de la cancion 
def parar_cancion():
    print("Deteniendo...")
    global imagen_logo, resized_logo, logo_imagen
    imagen_logo = Image.open('logo.png')
    resized_logo = imagen_logo.resize((250, 250))
    logo_imagen = ImageTk.PhotoImage(resized_logo)
    canvas_imagen.delete()
    canvas_imagen.create_image(0, 0, anchor='nw', image=logo_imagen)
    canvas_imagen.pack()
    label_nombre_cancion.config(text='..........')
    label_nombre_album.config(text='..........') 
    label_nombre_artista.config(text='..........')

#metodo para pausar cancion, no se usa por simulacion
def pausar_cancion():
    print("Pausando...")

#metodo para siguiente cancion y en caso sea una sola cancion debera realizar funcion de parar cancion
def siguiente_cancion():
    estructura.cambiar_siguiente_cancion()

#metodo para anterior cancion y en caso sea una sola cancion debera realizar funcion de parar cancion
def anterior_cancion():
    print("anterior...")

#metodo para mostrar mensaje error
def mostrar_mensaje_error(mensaje):
    messagebox.showerror('Error: ', mensaje)

def mostrar_mensaje_proceso_correcto(mensaje):
    messagebox.showinfo('Proceso exitoso: ', mensaje)

#metodo para colocar imagen del album
def colocar_imagen_album(ruta):
    global imagen_logo, resized_logo, logo_imagen
    imagen_logo = Image.open(ruta)
    resized_logo = imagen_logo.resize((250, 250))
    logo_imagen = ImageTk.PhotoImage(resized_logo)
    canvas_imagen.delete()
    canvas_imagen.create_image(0, 0, anchor='nw', image=logo_imagen)
    canvas_imagen.pack()

#metodo para obtener el valor a buscar, en este caso obtener la cancion solo para el frame secundario donde coloca la cancion directamente
def obtener_cancion_buscar(nombre):
    print(f"el texto a buscar es: {nombre}")
    estructura.buscar_cancion(nombre)

#metodo para obtener datos de la cancion para agregar a playlist
def obtener_cancion_mostrar(nombre):
    print(f"el texto a buscar es: {nombre}")
    if nombre_playlist_almacenada is None or nombre_playlist_almacenada =='':
        mensaje = 'no se ha cargado la playlist a la cual se agregara la cancion'
        mostrar_mensaje_error(mensaje)
        return
    datos_cancion = estructura.buscar_cancion_para_mostrar_agregar_playlist(nombre)
    if datos_cancion is not None:
        global label_rectangular_global
        print(datos_cancion)
        label_rectangular_global.config(text=datos_cancion)
        root.update_idletasks()
        estructura.agreg_cancion_lista(nombre_playlist_almacenada,nombre)

    

#metodo para obtener dato del entry dentro del frame crear playlist
def obtener_dato_entry_global_cancion():
    global dato
    dato = entry_buscar_cancion_global.get()

#metodo para obtener dato del entry dentro del frame pedir nombre playlist
def obtener_dato_global_playlist():
    global dato_playlist
    dato_playlist = entry_buscar_playlist_global.get()
    print(dato_playlist)

#metodo para cerrar el frame playlist
def regresar_frame_playlist():
    frame_playlist.place_forget()

#metodo para ocultar el frame de nombre_playlist
def regresar_frame_pedir_nomb_playlist():
    frame_pedir_nombre_playlist.place_forget()


def pedir_nombre_playlist_crear():
    frame_pedir_nombre_playlist.place(x=265, y=150, width=400, height=200)
    global entry_buscar_playlist_global
    #entry labelFrame
    entry_buscar_playlist_global = Tk.Entry(frame_pedir_nombre_playlist)
    entry_buscar_playlist_global.place(x=20,y=20,width=200,height=30)
    #botones
    boton_crear = Tk.Button(frame_pedir_nombre_playlist, text="Crear", command=lambda: [obtener_dato_global_playlist(),crear_playlist(),entry_buscar_playlist_global.delete(0, 'end')])
    boton_regresar = Tk.Button(frame_pedir_nombre_playlist, text="Regresar", command=regresar_frame_pedir_nomb_playlist)
    boton_crear.place(x=20, y=80, width=100, height=30)
    boton_regresar.place(x=150, y=80, width=100, height=30)

def pedir_nombre_playlist_cargar():
    frame_pedir_nombre_playlist.place(x=265, y=150, width=400, height=200)
    global entry_buscar_playlist_global
    #entry labelFrame
    entry_buscar_playlist_global = Tk.Entry(frame_pedir_nombre_playlist)
    entry_buscar_playlist_global.place(x=20,y=20,width=200,height=30)
    #botones
    boton_crear = Tk.Button(frame_pedir_nombre_playlist, text="Cargar", command=lambda: [obtener_dato_global_playlist(),cargar_playlist(),entry_buscar_playlist_global.delete(0, 'end')])
    boton_regresar = Tk.Button(frame_pedir_nombre_playlist, text="Regresar", command=regresar_frame_pedir_nomb_playlist)
    boton_crear.place(x=20, y=80, width=100, height=30)
    boton_regresar.place(x=150, y=80, width=100, height=30)

def crear_playlist():
    estructura.crear_nombre_playlist(dato_playlist)

def cargar_playlist():
    global nombre_playlist_almacenada
    nombre_playlist_almacenada = estructura.cargar_playlist_guardada(dato_playlist)
    print('nombre de la playlist encontrada es: ',nombre_playlist_almacenada)

#metodo para crear un labelFrame
def mostar_frame_playlist():
    global nombre_playlist_almacenada
    nombre_playlist_almacenada = None

    frame_playlist.place(x=0, y=0, width=876, height=476)
    global lupa_image, resized_lupa,lupa_image
    #entry labelFrame playlist
    global entry_buscar_cancion_global
    entry_buscar_cancion_global = Tk.Entry(frame_playlist, font=('Arial', 12, 'bold'))
    entry_buscar_cancion_global.place(x=60, y=20, width=500, height=30)
    #icono lupa y label
    lupa_image = Image.open('lupa.png')
    resized_lupa = lupa_image.resize((28,28))
    lupa_image = ImageTk.PhotoImage(resized_lupa)
    label_lupa = Tk.Label(frame_playlist, image=lupa_image, bg='white')
    label_lupa.place(x=530, y=21, width=28, height=28)
    #label rectangular
    global label_rectangular_global
    label_rectangular_global = Tk.Label(frame_playlist, bg='white', fg='black',wraplength=800, justify='left', anchor='nw', font=('Arial', 12, 'bold'))
    label_rectangular_global.place(x=40, y=70, width=800, height=300)
    #botones
    boton_crear_playlist = Tk.Button(frame_playlist, text="Crear Playlist Nueva", font=('Arial', 12, 'bold'), command=pedir_nombre_playlist_crear)
    boton_crear_playlist.place(x=200, y=400, width=200, height=30)
    boton_cargar_playlist = Tk.Button(frame_playlist, text="Cargar Playlist", font=('Arial', 12, 'bold'), command=pedir_nombre_playlist_cargar)
    boton_cargar_playlist.place(x=450, y=400, width=200, height=30)
    boton_buscar_cancion = Tk.Button(frame_playlist, text="Buscar", font=('Arial', 12, 'bold'), command=lambda: [obtener_dato_entry_global_cancion(),obtener_cancion_mostrar(dato), entry_buscar_cancion_global.delete(0, 'end')])
    boton_buscar_cancion.place(x=560, y=21, width=100, height=30)
    boton_regresar = Tk.Button(frame_playlist, text="Regresar", font=('Arial', 12, 'bold'),command=regresar_frame_playlist)
    boton_regresar.place(x=725, y=400, width=100, height=30)

root = Tk.Tk()
root.title("MP3 Player")

# Configurar el tamaño de la ventana antes de llamar a mainloop()
root.geometry("875x475")

# Desactivar la capacidad de cambiar el tamaño de la ventana
root.resizable(0, 0)

# Crear menu
menu = Tk.Menu(root)
root.config(menu=menu)

# Crear opciones del menu
menu_archivo = Tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Cargar biblioteca", command=cargar_biblioteca)
menu_archivo.add_command(label="Crear playlist por cancion", command=mostar_frame_playlist)
menu_archivo.add_command(label="Mostrar más reproducidos")
menu_archivo.add_command(label="Mostrar reporte de biblioteca")

# Frames
#frame principal
frame_principal = Tk.Frame(root, bg='#A62D65')
frame_principal.place(x=0, y=0, width=900, height=500)

#frame secundario adentro del frame principal
frame_secundario = Tk.Frame(frame_principal, bg='#295073')
frame_secundario.place(x=50, y=20, width=800, height=425)

#frame info cancion adentro del frame secundario
frame_info_cancion = Tk.Frame(frame_secundario, bg='#A3C9D9')
frame_info_cancion.place(x=350, y=150, width=400, height=150)

#frame imagen del album adentro del frame secundario
frame_imagen_album = Tk.Frame(frame_secundario)
frame_imagen_album.place(x=50, y=100, width=250, height=250)
canvas_imagen = Canvas(frame_imagen_album, width=250, height=250)
canvas_imagen.pack()
imagen_logo = Image.open('logo.png')
resized_logo = imagen_logo.resize((250, 250))
logo_imagen = ImageTk.PhotoImage(resized_logo)
canvas_imagen.create_image(0, 0, anchor='nw', image=logo_imagen)

#frame crear playlist
frame_playlist = Tk.LabelFrame(root, text="Playlist",bg='#295073',font=('Arial', 20, 'bold'))

#frame pedir nombre playlist
frame_pedir_nombre_playlist = Tk.LabelFrame(root,text="Nombre Playlist",bg='#295073',font=('Arial', 20, 'bold'))

# labels

# label cancion
label_cancion = Tk.Label(frame_info_cancion, text="Cancion", font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_cancion.place(x=0, y=10, anchor="nw")

# label artista
label_artista = Tk.Label(frame_info_cancion, text="Artista", font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_artista.place(x=0, y=60, anchor="nw")

# label album
label_album = Tk.Label(frame_info_cancion, text="Album", font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_album.place(x=0, y=110, anchor="nw")

# label nombre cancion
label_nombre_cancion = Tk.Label(frame_info_cancion, text='..........', font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_nombre_cancion.place(x=150, y=10, anchor="nw")

# label nombre artista
label_nombre_artista = Tk.Label(frame_info_cancion, text='..........', font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_nombre_artista.place(x=150, y=60, anchor="nw")

# label nombre album
label_nombre_album = Tk.Label(frame_info_cancion, text='..........', font=('Arial', 12, 'bold'), bg='#E0E6F8')
label_nombre_album.place(x=150, y=110, anchor="nw")

#entrys

#entry frame secundario
entry_buscar = Tk.Entry(frame_secundario, font=('Arial', 12, 'bold'))
entry_buscar.place(x=60, y=20, width=500, height=30)
lupa_image = Image.open('lupa.png')
resized_lupa = lupa_image.resize((28,28))
lupa_image = ImageTk.PhotoImage(resized_lupa)
label_lupa = Tk.Label(frame_secundario, image=lupa_image, bg='white')
label_lupa.place(x=530, y=21, width=28, height=28)


# botones

# Play boton
image_play = Image.open('play.png')
resized_play = image_play.resize((50, 50))
play_image = ImageTk.PhotoImage(resized_play)
Tk.Button(frame_secundario,image=play_image,command=reproducir_cancion,bg='#81BEF7',highlightthickness=0).place(x=400, y=85, width=50, height=50)


# Pausa boton
image_pause = Image.open('pause.png')
resized_pause = image_pause.resize((50,50))
pause_image = ImageTk.PhotoImage(resized_pause)
Tk.Button(frame_secundario,image=pause_image,command=pausar_cancion,bg='#81BEF7',highlightthickness=0).place(x=525, y=85, width=50, height=50)

# Para boton
image_stop = Image.open('stop.png')
resized_stop = image_stop.resize((40,40))
stop_image = ImageTk.PhotoImage(resized_stop)
Tk.Button(frame_secundario,image=stop_image, command=parar_cancion,bg='#81BEF7',highlightthickness=0).place(x=650, y=85, width=50, height=50)

# next boton
image_next = Image.open('next.png')
resized_next = image_next.resize((40,40))
next_image = ImageTk.PhotoImage(resized_next)
Tk.Button(frame_secundario,image=next_image,command=siguiente_cancion,bg='#81BEF7',highlightthickness=0).place(x=475, y=315, width=50, height=50)

# back boton
image_back = Image.open('back.png')
resized_back = image_back.resize((40,40))
image_back = ImageTk.PhotoImage(resized_back)
Tk.Button(frame_secundario,image=image_back, command=anterior_cancion,bg='#81BEF7',highlightthickness=0).place(x=600, y=315, width=50, height=50)

#boton buscar frame secundario
boton_buscar = Tk.Button(frame_secundario, text="Buscar", font=('Arial', 12, 'bold'), command=lambda: [estructura.colocar_cancion_display(entry_buscar.get()), entry_buscar.delete(0, 'end')])
boton_buscar.place(x=560, y=21, width=100, height=30)



root.mainloop()