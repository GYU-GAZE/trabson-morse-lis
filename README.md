# TDE 2 — Código Morse com Árvore Binária (Python)

Resolução de Problemas Estruturados em Computação — Profa. Lisiane Reips

## Como executar

Python 3.8+ (só biblioteca padrão, nada para instalar):

```
python main.py
```

## Estrutura

| Arquivo | Responsabilidade |
|---|---|
| `noMorse.py` | Classe `NoMorse` (caractere, esquerda, direita) |
| `arvoreMorse.py` | Classe `ArvoreMorse`: inserção, decodificação e codificação |
| `visualizadorArvore.py` | Impressão da árvore no console e em janela Tkinter |
| `somMorse.py` | Reprodução sonora do Morse (ponto extra) |
| `main.py` | Menu interativo |

## Requisitos atendidos

1. **Inserção pela heurística Morse** — `ArvoreMorse.inserir` percorre o código: `.` desce à esquerda, `-` desce à direita, criando nós vazios quando necessário.
2. **Decodificação** (Morse → texto) — `decodificarMensagem`, letras separadas por espaço e palavras por ` / `.
   Ex.: `... --- ...` → `SOS`; `.--. ..- -.-. .--. .-.` → `PUCPR`.
3. **Codificação** (texto → Morse) — `codificarMensagem`, buscando o caminho de cada caractere na própria árvore.
4. **Impressão da árvore** — console (árvore deitada + nível a nível) e janela gráfica com Tkinter.
5. **Modularização** — classes e funções separadas por arquivo, nomes em camelCase.
6. **Som** — `somMorse.py` gera um WAV (700 Hz, ponto = 1 unidade, traço = 3) e toca no Windows via `winsound`; em outros sistemas salva `morse.wav`.
