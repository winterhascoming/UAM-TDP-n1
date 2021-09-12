from random import randint
sala = 1
tentativa=1 
caminho = float(input("digite o caminho escolhido"))
if(caminho == 1):
        print("Você escolheu o caminho preto")
        sala = sala + 2
        print("vc esta na sala", sala)
elif(sala == 8):
        sala = randint(1,5)
        print("sala do portal", sala)
else:
        print("Você escolheu o caminho preto")
        sala = sala + 1
        print("vc está na sala", sala)
