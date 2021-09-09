import random

lista = [1,2,3,4,5]
portal = random.choice(lista)
sala = 1

def myApp():
    tentativas = 1
    sala = 1
    vermelho = 1
    preto = 2

    while (tentativas <=7 ):
        escolhido = float(input("Qual será o caminho escolhido? \n"))
        if escolhido == 1:
            sala = sala + vermelho
            print("Você está na sala:", sala)
        elif sala == 8: #só esta funcionando quando o caminho escolhido estiver no else
            print("Você entrou pelo portal e sua nova sala sera sorteada")
            sala = portal
            print("Sua nova sala é:", sala)
        else:
            sala = sala + preto
            print("Você está na sala:", sala)
        tentativas = tentativas + 1
        print("Essa é sua", tentativas, "ª tentativa")

myApp()

def main():
    myApp

if __name__ == "__main__":
    main()
