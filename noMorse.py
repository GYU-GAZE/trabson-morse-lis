class NoMorse:
    """Nó da árvore binária de Morse: ponto vai para a esquerda, traço para a direita."""

    def __init__(self, caractere=None):
        self.caractere = caractere
        self.esquerda = None  # ponto (.)
        self.direita = None   # traço (-)

    def ehFolha(self):
        return self.esquerda is None and self.direita is None
