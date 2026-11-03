"""Reprodução sonora do código Morse (ponto extra). Usa só a biblioteca padrão."""
import io
import math
import struct
import sys
import wave

FREQUENCIA_HZ = 700
TAXA_AMOSTRAGEM = 44100
UNIDADE_SEGUNDOS = 0.08  # duração de um ponto


def gerarTom(duracaoSegundos, comSom=True):
    totalAmostras = int(TAXA_AMOSTRAGEM * duracaoSegundos)
    amostras = bytearray()
    for indice in range(totalAmostras):
        valor = math.sin(2 * math.pi * FREQUENCIA_HZ * indice / TAXA_AMOSTRAGEM) if comSom else 0.0
        amostras += struct.pack("<h", int(valor * 16000))
    return bytes(amostras)


def gerarAudioMorse(mensagemMorse):
    """Regras de tempo: ponto=1, traço=3, entre símbolos=1, entre letras=3, entre palavras=7."""
    silencioUnidade = gerarTom(UNIDADE_SEGUNDOS, comSom=False)
    audio = bytearray()
    for simbolo in mensagemMorse.strip():
        if simbolo == ".":
            audio += gerarTom(UNIDADE_SEGUNDOS) + silencioUnidade
        elif simbolo == "-":
            audio += gerarTom(UNIDADE_SEGUNDOS * 3) + silencioUnidade
        elif simbolo == " ":
            audio += silencioUnidade * 2
        elif simbolo == "/":
            audio += silencioUnidade * 2
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as arquivoWav:
        arquivoWav.setnchannels(1)
        arquivoWav.setsampwidth(2)
        arquivoWav.setframerate(TAXA_AMOSTRAGEM)
        arquivoWav.writeframes(bytes(audio))
    return buffer.getvalue()


def tocarMorse(mensagemMorse):
    audioWav = gerarAudioMorse(mensagemMorse)
    if sys.platform.startswith("win"):
        import winsound
        winsound.PlaySound(audioWav, winsound.SND_MEMORY)
    else:
        nomeArquivo = "morse.wav"
        with open(nomeArquivo, "wb") as arquivo:
            arquivo.write(audioWav)
        print(f"Áudio salvo em '{nomeArquivo}' (reprodução automática só no Windows).")
