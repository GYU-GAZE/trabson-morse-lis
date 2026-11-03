"""Impressão da árvore Morse no console e em janela gráfica (Tkinter).
Adaptado da ideia do TreeVisualizer.java fornecido pela professora."""

RAIO_NO = 16
ESPACO_VERTICAL = 80


def imprimirArvoreConsole(raiz):
    """Árvore deitada: direita (traço) em cima, esquerda (ponto) embaixo.
    Gire a cabeça 90° para a esquerda para ver a árvore em pé."""
    print("\n(gire 90° para a esquerda: '-' = direita/cima, '.' = esquerda/baixo)\n")
    if raiz.direita is not None:
        _imprimirNo(raiz.direita, "", False)
    print("(raiz)")
    if raiz.esquerda is not None:
        _imprimirNo(raiz.esquerda, "", True)


def _imprimirNo(no, prefixo, ehEsquerda):
    if no.direita is not None:
        _imprimirNo(no.direita, prefixo + ("│     " if ehEsquerda else "      "), False)
    conector = "└─.─ " if ehEsquerda else "┌─-─ "
    print(prefixo + conector + (no.caractere or "•"))
    if no.esquerda is not None:
        _imprimirNo(no.esquerda, prefixo + ("      " if ehEsquerda else "│     "), True)


def imprimirArvorePorNivel(raiz):
    """Impressão em largura (nível a nível), útil para conferir a estrutura."""
    nivelAtual = [raiz]
    numeroNivel = 0
    while any(no is not None for no in nivelAtual):
        textos = [(no.caractere or "•") if no else " " for no in nivelAtual]
        print(f"Nível {numeroNivel}: " + " ".join(textos))
        proximoNivel = []
        for no in nivelAtual:
            proximoNivel.append(no.esquerda if no else None)
            proximoNivel.append(no.direita if no else None)
        nivelAtual = proximoNivel
        numeroNivel += 1


def mostrarArvoreJanela(arvore):
    """Desenha a árvore em uma janela Tkinter (biblioteca padrão do Python)."""
    import tkinter as tk

    altura = arvore.calcularAltura()
    larguraJanela = max(900, (2 ** (altura - 1)) * (RAIO_NO * 2 + 6))
    alturaJanela = altura * ESPACO_VERTICAL + 60

    janela = tk.Tk()
    janela.title("Árvore Binária - Código Morse (ponto à esquerda, traço à direita)")
    canvas = tk.Canvas(janela, width=larguraJanela, height=alturaJanela, bg="white")
    canvas.pack(fill="both", expand=True)

    def desenharNo(no, x, y, deslocamento):
        if no.esquerda is not None:
            xFilho, yFilho = x - deslocamento, y + ESPACO_VERTICAL
            canvas.create_line(x, y, xFilho, yFilho, fill="#1f77b4", width=2)
            canvas.create_text((x + xFilho) / 2 - 8, (y + yFilho) / 2, text=".", font=("Consolas", 16, "bold"))
            desenharNo(no.esquerda, xFilho, yFilho, deslocamento / 2)
        if no.direita is not None:
            xFilho, yFilho = x + deslocamento, y + ESPACO_VERTICAL
            canvas.create_line(x, y, xFilho, yFilho, fill="#d62728", width=2)
            canvas.create_text((x + xFilho) / 2 + 8, (y + yFilho) / 2 - 4, text="-", font=("Consolas", 16, "bold"))
            desenharNo(no.direita, xFilho, yFilho, deslocamento / 2)
        corFundo = "#ffe08a" if no.caractere else "#dddddd"
        canvas.create_oval(x - RAIO_NO, y - RAIO_NO, x + RAIO_NO, y + RAIO_NO, fill=corFundo, outline="black")
        canvas.create_text(x, y, text=no.caractere or ("início" if no is arvore.raiz else ""), font=("Arial", 10, "bold"))

    desenharNo(arvore.raiz, larguraJanela / 2, 40, larguraJanela / 4)
    janela.mainloop()
