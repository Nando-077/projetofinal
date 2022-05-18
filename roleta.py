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
            if sorteio == escolha_jogador and sorteio != 0:
                saldo += 10 * valor_aposta
            if sorteio == 0 and escolha_jogador == 0:
                saldo += 20 * valor_aposta
            else:
                saldo -= valor_aposta  

        # Se o jogador escolher uma cor
        elif cor_ou_numero == 'cor':
            if  cor_escolha == cor_sorteio:
                saldo += 2 * valor_aposta
            else:
                saldo -= valor_aposta
        
        print(saldo)