class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class lista_circular: 
    def __init__(self):
        self.primero = None

    def insertar(self, valor):
        nuevo = nodo(valor)
        if self.primero is None:
            self.primero = nuevo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            nuevo.siguiente = self.primero
            nuevo.anterior = self.primero.anterior
            self.primero.anterior.siguiente = nuevo
            self.primero.anterior = nuevo
            self.primero = nuevo
    
    def eliminar(self, valor):
        if self.primero is not None:
            actual = self.primero
            while actual.valor != valor:
                actual = actual.siguiente
                if actual is self.primero:
                    return
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            if actual is self.primero:
                self.primero = actual.siguiente
    
    def imprimir(self):
        #caso de estar vacia
        if self.primero is None:
            return
        if self.primero is not None:
            actual = self.primero
            while actual.siguiente != self.primero:
                print(actual.valor)
                actual = actual.siguiente
            print(actual.valor)
