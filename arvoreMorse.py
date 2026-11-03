from noMorse import NoMorse

PONTO = "."
TRACO = "-"

TABELA_MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
}


class ArvoreMorse:
    """Árvore binária onde o caminho da raiz até o nó é o código Morse do caractere."""

    def __init__(self):
        self.raiz = NoMorse()  # raiz vazia (início de todo código)

    def inserir(self, caractere, codigo):
        """Percorre o código: '.' desce à esquerda, '-' desce à direita.
        Cria nós intermediários vazios quando o caminho ainda não existe."""
        noAtual = self.raiz
        for simbolo in codigo:
            if simbolo == PONTO:
                if noAtual.esquerda is None:
                    noAtual.esquerda = NoMorse()
                noAtual = noAtual.esquerda
            elif simbolo == TRACO:
                if noAtual.direita is None:
                    noAtual.direita = NoMorse()
                noAtual = noAtual.direita
            else:
                raise ValueError(f"Símbolo inválido no código Morse: '{simbolo}'")
        noAtual.caractere = caractere

    def carregarTabela(self, tabela=TABELA_MORSE):
        for caractere, codigo in tabela.items():
            self.inserir(caractere, codigo)

    def decodificarLetra(self, codigo):
        """Retorna o caractere de um código Morse, ou '?' se não existir."""
        noAtual = self.raiz
        for simbolo in codigo:
            if simbolo == PONTO:
                noAtual = noAtual.esquerda
            elif simbolo == TRACO:
                noAtual = noAtual.direita
            else:
                return "?"
            if noAtual is None:
                return "?"
        return noAtual.caractere or "?"

    def decodificarMensagem(self, mensagemMorse):
        """Letras separadas por espaço; palavras separadas por ' / '."""
        palavrasDecodificadas = []
        for palavraMorse in mensagemMorse.strip().split("/"):
            letras = [self.decodificarLetra(codigo) for codigo in palavraMorse.split()]
            palavrasDecodificadas.append("".join(letras))
        return " ".join(palavrasDecodificadas)

    def buscarCodigo(self, caractere, noAtual=None, caminho=""):
        """Busca em profundidade o caminho (código Morse) até o caractere."""
        if noAtual is None:
            noAtual = self.raiz
        if noAtual.caractere == caractere:
            return caminho
        if noAtual.esquerda is not None:
            resultado = self.buscarCodigo(caractere, noAtual.esquerda, caminho + PONTO)
            if resultado is not None:
                return resultado
        if noAtual.direita is not None:
            resultado = self.buscarCodigo(caractere, noAtual.direita, caminho + TRACO)
            if resultado is not None:
                return resultado
        return None

    def codificarMensagem(self, texto):
        """Converte texto em Morse usando a própria árvore (sem consultar a tabela)."""
        palavrasCodificadas = []
        for palavra in texto.upper().split():
            codigos = []
            for caractere in palavra:
                codigo = self.buscarCodigo(caractere)
                codigos.append(codigo if codigo is not None else "?")
            palavrasCodificadas.append(" ".join(codigos))
        return " / ".join(palavrasCodificadas)

    def calcularAltura(self, noAtual="inicio"):
        if noAtual == "inicio":
            noAtual = self.raiz
        if noAtual is None:
            return 0
        return 1 + max(self.calcularAltura(noAtual.esquerda), self.calcularAltura(noAtual.direita))
