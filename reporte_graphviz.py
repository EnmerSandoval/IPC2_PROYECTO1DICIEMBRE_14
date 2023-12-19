from graphviz import Digraph

class ReporteGraphviz:
    
    @staticmethod
    def graficar_lista_doble(lista_doble, path='grafo_nodo_'):
        if lista_doble.head is None:
            print("Advertencia: La lista está vacía.")
            return

        nodoTemporal = lista_doble.head

        while nodoTemporal is not None:
            if nodoTemporal.dato is not None and nodoTemporal.dato.album.head is not None:
                dot = Digraph(comment=f'Nodo: {nodoTemporal.dato.nombre}')
                dot.format = 'png'

                dot.node(str(id(nodoTemporal.dato.nombre)), str(nodoTemporal.dato.nombre))

                if nodoTemporal.siguiente is not None:
                    dot.edge(str(id(nodoTemporal.dato.nombre)), str(id(nodoTemporal.siguiente.dato.nombre)), label='siguiente')
                if nodoTemporal.anterior is not None:
                    dot.edge(str(id(nodoTemporal.dato.nombre)), str(id(nodoTemporal.anterior.dato.nombre)), label='anterior')

                filename = f"{path}{nodoTemporal.dato.nombre}.png"
                dot.render(filename, view=True)
            else:
                print(f"Artista: {nodoTemporal.dato.nombre} - No hay álbumes asociados.")

            nodoTemporal = nodoTemporal.siguiente