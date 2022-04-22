class Terminal:
    def __init__(self, tk, lex):
        self.token = tk
        self.valor = lex

class noTerminal:
    def __init__(self, n):
        self.nombre = n