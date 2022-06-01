import numpy as np
import random

#variaves
saldo = 1000


#criando a lista de numeros do grafico
grafico = np.arange (0.00,10.00,0.01)


# Jogo
#iniciando jogo
while saldo > 0:
    print('Seja bem vindo ao crash!')
    print(' ')
    print('=================================================================================')
    print(' ')
    print('Aqui sua aposta multiplica segundo quanto o seu carro anda!')
    print('Porem seu carro pode bater')
    print('e quando isso acontece todo o dinheiro apostado é perdido')
    print(' ')
    print('=================================================================================')
    print('Seu saldo é {}'.format(saldo))
    print(' ')

#Aposta
    print('Quanto será apostado?') 
    aposta = int(input('aposta:')) 

    if aposta <= saldo:
        saldo = saldo - aposta

        print('Qual distancia será percorrida pelo carro antes de bater?')
        distancia = float(input('distancia:'))

        #sorteio de até onde o carro irá

        
        index = random.randint(0, len(grafico) - 1)
        batida = grafico[index]

        #vencer ou perder

        if distancia <= batida:
            saldo = saldo + aposta * distancia
            print('Você conseguiu !!!!')
            print('Seu novo saldo é de {}'.format(saldo))
        elif saldo <= 0:
            print ('GAME OVER')
        else:
            print('O carro bateu')
            print('Seu novo saldo é de {}'.format(saldo))

