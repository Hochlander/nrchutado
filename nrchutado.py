import random
import os
palpites=[]
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu numero: "))
while(sorteado!=jogador):
    os.system('cls')
    print ("palpites que já foram: ") 
    for i in palpites:
        print(i)
    if(sorteado>jogador):
        print("ERRO, o numero é maior")
        print(jogador)
    elif(sorteado<jogador):
        print("ERRO, o numero é menor")
        print(jogador)
    erros+=1
    palpites.append(jogador)
    
    jogador=int(input("Digite seu numero: "))
    print("Número " + str(jogador) +", você acertou em " +str(erros+1)+ " tentativas")
