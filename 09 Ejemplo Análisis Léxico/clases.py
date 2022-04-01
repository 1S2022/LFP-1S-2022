class Token:
    def __init__(self, n, l, f, c):
        self.nombre = n
        self.lexema = l
        self.fila = f
        self.columna = c


class Error:
    def __init__(self, t, v, f, c):
        self.tipo = t
        self.valor = v
        self.fila = f
        self.columna = c