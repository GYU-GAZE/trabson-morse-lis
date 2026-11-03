from arvoreMorse import ArvoreMorse
from somMorse import tocarMorse
from visualizadorArvore import imprimirArvoreConsole, imprimirArvorePorNivel, mostrarArvoreJanela


def exibirMenu():
    print("\n===== TDE 2 - Código Morse (Árvore Binária) =====")
    print("1 - Decodificar Morse -> texto")
    print("2 - Codificar texto -> Morse")
    print("3 - Imprimir árvore no console")
    print("4 - Mostrar árvore em janela gráfica")
    print("5 - Tocar som de uma mensagem Morse")
    print("0 - Sair")
    return input("Escolha: ").strip()


def perguntarSeToca(mensagemMorse):
    if input("Tocar o som? (s/n): ").strip().lower() == "s":
        tocarMorse(mensagemMorse)


def main():
    arvore = ArvoreMorse()
    arvore.carregarTabela()

    while True:
        opcao = exibirMenu()
        if opcao == "1":
            mensagemMorse = input("Digite o Morse (letras separadas por espaço, palavras por ' / '):\n> ")
            print("Texto decodificado:", arvore.decodificarMensagem(mensagemMorse))
            perguntarSeToca(mensagemMorse)
        elif opcao == "2":
            texto = input("Digite o texto:\n> ")
            mensagemMorse = arvore.codificarMensagem(texto)
            print("Morse:", mensagemMorse)
            perguntarSeToca(mensagemMorse)
        elif opcao == "3":
            imprimirArvoreConsole(arvore.raiz)
            print()
            imprimirArvorePorNivel(arvore.raiz)
        elif opcao == "4":
            mostrarArvoreJanela(arvore)
        elif opcao == "5":
            tocarMorse(input("Digite o Morse:\n> "))
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
