# falta finalizar o código => protótipo
#caminho preto +2 e vermelho +1

from random import randint

sala = 1
tentativa = 1

while (tentativa <= 7 and sala <=8):
    caminho = float(input("digite o caminho"))
    caminho 
    if (caminho == 1):
        sala = sala + 2
        print("vc esta na sala", sala)
    elif(sala == 8):
        sala = randint(1,5)
        print("sala do portal", sala)
    else:
        sala = sala + 1
        print("vc está na sala", sala)
    tentativa = tentativa + 1

if(sala == 9 and tentativa <= 7):
    print("ganhou")