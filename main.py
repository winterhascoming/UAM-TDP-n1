import random

def main ():
    tentativas = 1
    sala = 1
    vermelho = 1
    preto = 2
    lista = [1,2,3,4,5]
    portal = random.choice(lista)

    while (tentativas <=7 ):
        escolhido = float(input("Qual será o caminho escolhido? \n"))
        if escolhido == 1:
            sala = sala + vermelho
            print("Você está na sala:", sala)
        elif sala == 8:
            sala = sala + portal
            print("Você está na sala:", sala)
        else:
            sala = sala + preto
            print("Você está na sala:", sala)
        tentativas = tentativas + 1
        print("Essa é sua", tentativas, "ª tentativa")
main()