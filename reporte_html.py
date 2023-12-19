import xml.etree.ElementTree as ET

def reporte(ruta_archivo):
    archivo_xml = ET.parse(ruta_archivo)
    raiz = archivo_xml.getroot()

    # Arreglar canciones en orden a más escuchadas
    sorted_songs = sorted(raiz.findall('.//cancion'), key=lambda x: int(x.find('vecesReproducida').text), reverse=True)

    # Tomar las 5 canciones más escuchadas y agregar contador
    top_songs = sorted_songs[:5]
    count = 0

    file_html = open("reporte.html", "w")

    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="reset.css">
        <link rel="stylesheet" href="reporte.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Rubik+Doodle+Shadow&display=swap" rel="stylesheet">
        <title>MP3 wrapped</title>
    </head>
    <header>
        <img src="wrapped/logo.png" class="logo">
        <h1 class="title">2023 wrapped</h1>
    </header>
    <body>
        <div class="songs">
            <h2 class="intro">Estas son las canciones mas escuchadas de tu 2023!</h2>
    '''

    for song in top_songs:
        song_name = song.get('nombre')
        artist = song.find('artista').text
        album = song.find('album').text
        times_played = song.find('vecesReproducida').text
        image_path = song.find('imagen').text
        audio_path = song.find('ruta').text

        count += 1

        html_content += f"""
            <div class="song">
                <div class="text">
                    <h3 class="songName">#{count} {song_name}</h3>
                    <h4>{artist}</h4>
                    <h5>La escuchaste {times_played} veces</h5>
                </div>
                <img src={image_path} class="album">
            </div>
        """

    html_content += '''
        </div>
    </body>
    </html>
    '''

    file_html.write(html_content)

    file_html.close()