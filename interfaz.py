import tkinter as Tk
from tkinter import filedialog
from PIL import Image, ImageTk

def browse_file():
    file_ = filedialog.askopenfilename()
    if file_.endswith('.xml'):
        # Cargar biblioteca
        pass
    else:
        # Mostrar mensaje de error
        print("Error: El archivo seleccionado no es un archivo '.xml'")

def load_library():
    browse_file()
    print("Biblioteca cargada")

def play_song():
    print("Reproduciendo...")

def stop_song():
    print("Deteniendo...")

def pause_song():
    print("Pausando...")

def unpause_song():
    print("Reanudando...")

def next_song():
    print("siguiente...")

def back_song():
    print("anterio...")
    
root = Tk.Tk()
root.title("MP3 Player")

# Configurar el tamaño de la ventana antes de llamar a mainloop()
root.geometry("900x400")

# Desactivar la capacidad de cambiar el tamaño de la ventana
root.resizable(0, 0)

# Variables
song_name = Tk.StringVar(root)
song_artist = Tk.StringVar(root)
song_album = Tk.StringVar(root)
song_name.set('nombre cancion')
song_artist.set('nombre artista')
song_album.set('nombre album')

# Crear menu
menu = Tk.Menu(root)
root.config(menu=menu)

# Crear opciones del menu
file_menu = Tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Cargar biblioteca", command=load_library)
file_menu.add_command(label="Mostrar más reproducidos")

# Frames
main_frame = Tk.Frame(root, bg='#81F7BE')
main_frame.place(x=0, y=0, width=900, height=400)

display_frame = Tk.Frame(main_frame, bg='#81BEF7')
display_frame.place(x=50, y=50, width=800, height=325)

# Song Information
song_info_frame = Tk.Frame(display_frame, bg='#E0E6F8')
song_info_frame.place(x=350, y=100, width=400, height=150)

# Song Name
song_name_label = Tk.Label(song_info_frame, text="Cancion", font=('Arial', 12, 'bold'), bg='#E0E6F8')
song_name_label.place(x=0, y=0, anchor="nw")

# Song Artist
song_artist_label = Tk.Label(song_info_frame, text="Artista", font=('Arial', 12, 'bold'), bg='#E0E6F8')
song_artist_label.place(x=0, y=50, anchor="nw")

# Song Album
song_album_label = Tk.Label(song_info_frame, text="Album", font=('Arial', 12, 'bold'), bg='#E0E6F8')
song_album_label.place(x=0, y=100, anchor="nw")

# Controls Frame

# Play Button
image_play = Image.open('play.png')
resized_play = image_play.resize((50, 50))
play_image = ImageTk.PhotoImage(resized_play)
Tk.Button(display_frame,image=play_image,command=play_song,bg='#81BEF7',highlightthickness=0).place(x=400, y=35, width=50, height=50)


# Pause Button
image_pause = Image.open('pause.png')
resized_pause = image_pause.resize((50,50))
pause_image = ImageTk.PhotoImage(resized_pause)
Tk.Button(display_frame,image=pause_image,command=pause_song,bg='#81BEF7',highlightthickness=0).place(x=525, y=35, width=50, height=50)

# Stop Button
image_stop = Image.open('stop.png')
resized_stop = image_stop.resize((40,40))
stop_image = ImageTk.PhotoImage(resized_stop)
Tk.Button(display_frame,image=stop_image, command=stop_song,bg='#81BEF7',highlightthickness=0).place(x=650, y=35, width=50, height=50)

# next Button
image_next = Image.open('next.png')
resized_next = image_next.resize((40,40))
next_image = ImageTk.PhotoImage(resized_next)
Tk.Button(display_frame,image=next_image,command=next_song,bg='#81BEF7',highlightthickness=0).place(x=475, y=265, width=50, height=50)

# back Button
image_back = Image.open('back.png')
resized_back = image_back.resize((40,40))
image_back = ImageTk.PhotoImage(resized_back)
Tk.Button(display_frame,image=image_back, command=back_song,bg='#81BEF7',highlightthickness=0).place(x=600, y=265, width=50, height=50)

root.mainloop()