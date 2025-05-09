print("Tabuleiro 10 faces, 4,7,10, pares ou impares")

def start_finish(jogadas):
    if jogadas % 2 == 0:
        print("Par! Avance!")
    else:
        print("Impar! Fim!")
    return jogadas

start_finish(4)
start_finish(7)
start_finish(10)
