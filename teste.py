import random

#Variáveis:
cor_sorteio = ''
saldo = 1000
i = 1

# CONSTRUÇÃO DA LISTA DE NÚMEROS DA ROLETA
lista_vermelho = []
lista_preto = []
while i <= 36:
    if i % 2 == 0:
        lista_vermelho.append(i)
    elif i % 2 != 0:
        lista_preto.append(i)
    i += 1

#CÓDIGO DO JOGO

while saldo > 0:

# Mensagem inicial:

    print('Seja bem vindo a ROLETA!')
    print(' ')
    print('=================================================================================')
    print(' ')
    print('Aqui você pode apostar em uma cor ou em um número')
    print('Os números pares são os VERMELHOS')
    print('Os números ímpares são os PRETOS')
    print('Você também pode realizar uma aposta no número 0, que oferece grandes recompensas')
    print(' ')
    print('=================================================================================')
    print('Seu saldo é {}'.format(saldo))
    
# Fase inicial:

    cor_ou_numero = input('Quer apostar em um número ou em uma cor?')
    if cor_ou_numero == 'cor':
        cor_escolha = input('vermelho ou preto?')
    elif cor_ou_numero == 'numero':
        escolha_jogador = int(input('Escolha um número de 0 a 36'))
    valor_aposta = int(input('Quanto quer apostar?'))

# Analise do sorteio: 

    if valor_aposta <= saldo:

        sorteio = random.randint(0,36)

        #Cor do sorteio:
        if sorteio in lista_preto:
            cor_sorteio = 'preto'
        elif sorteio in lista_vermelho:
            cor_sorteio = 'vermelho'

# Ganho ou Perda:

        # Se o jogador escolher um número:
        if cor_ou_numero == 'numero':
            print('O número sorteado foi{}'.format(sorteio))
            if sorteio == escolha_jogador and sorteio != 0:
                print('Parabéns, você ganhou{}'.format(valor_aposta * 10))
                saldo += 10 * valor_aposta
    
            if sorteio == 0 and escolha_jogador == 0:
                print('Parabéns, você ganhou{}'.format(valor_aposta * 20))
                saldo += 20 * valor_aposta
            else:
                print('Você perdeu{}'.format(valor_aposta))
                saldo -= valor_aposta


        # Se o jogador escolher uma cor
        elif cor_ou_numero == 'cor':
            print('A cor sorteada foi{}'.format(cor_sorteio))
            if  cor_escolha == cor_sorteio:
                print('Parabéns, você ganhou{}'.format(valor_aposta *2))
                saldo += 2 * valor_aposta
            else:
                print('Você perdeu{}'.format(valor_aposta))
                saldo -= valor_aposta
        
        print(saldo)