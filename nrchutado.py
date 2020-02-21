import random
import os
erros=0
sorteado=random.randrange(0,1000000)
jogador=int(input("Digite seu numero: "))
while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("ERRO, o numero é maior")
        print(jogador)
    elif(sorteado<jogador):
        print("ERRO, o numero é menor")
        print(jogador)
    erros+=1
    jogador=int(input("Digite seu numero: "))
    print("Número " + str(jogador) +", você acertou em " +str(erros+1)+ " tentativas")
