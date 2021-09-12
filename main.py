from random import randint

print("\nCaro herói que ousa enfrentar esta Dungeon\nVocê deve chegar a 9ª Sala para vencer este desafio\nPorém você só possui 7 movimentos\nBoa sorte, você irá precisar!!!\n")

def myApp():

    sala = 1
    tentativas = 1

    while (sala <= 8 and tentativas <=7 ):

        print("\nVocê esta na sala:", sala, "\nEste é seu", tentativas,"º movimento")
        escolhido = int(input("\nEscolha seu caminho:\n\n[1] - Caminho Vermelho\n[2] - Caminho Preto\n"))

        if (sala == 6 and escolhido == 1):
            print("\nBom parece que temos um probleminha, o caminho Vermelho está fechado dessa sala\nParece que você irá pelo caminho Preto mesmo...\n")
            sala = sala + 1

        elif (sala == 8 and escolhido == 2):
            sala = 1
            sala = randint(1,5)
            print("Wow parece que você acaba de atravessar por um portal que te levou para a sala:", sala, "\n")
            
        if (escolhido > 2):
            print("\nBem parece que você escolheu uma parede como caminho meu caro herói, certeza que essa é sua escolha?\nDeveria voltar aos caminhos marcados de Preto e Vermelho para que possa prosseguir!")
            break
        
        if (escolhido < 1):
            print("\nBem parece que você escolheu uma parede como caminho meu caro herói, certeza que essa é sua escolha?\nDeveria voltar aos caminhos marcados de Preto e Vermelho para que possa prosseguir!")
            break
    
        sala = sala + escolhido
        tentativas = tentativas + 1

    if (sala == 9 and tentativas <=7 ):
        print("\nParabéns herói, você venceu este desafio e chegou a sala 9!!!\n")
        
    if (tentativas >= 8):
        print("\nInfelizmente seus movimentos acabaram meu caro herói\nAgora você está condenado a enfrentar os próximos que se julgam capazes de superar este desafio!\n")

myApp()

def main():
    myApp

if __name__ == "__main__":
    main()
