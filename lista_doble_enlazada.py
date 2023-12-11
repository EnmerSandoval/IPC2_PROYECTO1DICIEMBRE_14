class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, dato):
        nuevoNodo = Nodo(dato)

        #Validamos si la lista esta vacia
        if self.head == None:
            print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo
        
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            print("Insertando nodo al principio")
            self.head.anterior = nuevoNodo
            nuevoNodo.siguiente = self.head
            self.head = nuevoNodo

    def añadirNodoFinal(self, dato):
        nuevoNodo = Nodo(dato)

        #insertamos si la lista esta vacia
        if self.head == None:
            print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo

        #si por lo menos hay un nodo, insertamos al final
        else:
            print("Insertando nodo al final")
            self.end.siguiente = nuevoNodo
            nuevoNodo.anterior = self.end
            self.end = nuevoNodo
    

    def imprimirLista(self):
        print("*** Imprimiendo lista ***")
        # Caso de estar vacia
        if self.head is None:
            return
        nodoTemporal = self.head
        while nodoTemporal is not None:
            print(nodoTemporal.dato.nombre, end=", ")
            nodoTemporal = nodoTemporal.siguiente
        print()
        print('*** Fin de la lista ***')

    def get(self, nombre):
        # Caso de estar vacia
        if self.head is None:
            return None
        nodoTemporal = self.head
        while nodoTemporal is not None:
            # Si el dato actual es el que buscamos
            if (nodoTemporal.dato.nombre == nombre):
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente
        # Si ya buscamos toda la lista y no lo encontramos
        return None
    
    
    def get_datos(self):
        # Caso de estar vacia
        if self.head is None:
            return None
        nodoTemporal = self.head
        return nodoTemporal.dato
    
    