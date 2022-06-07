import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo')

game = True

image = pygame.image.load('rua real.png').convert_alpha()
carro1 = pygame.image.load('carrinho 1.png').convert_alpha()
policia = pygame.image.load('carrinho 2.png').convert_alpha()
carro3 = pygame.image.load('carrinho 3.png').convert_alpha()
meucarro = pygame.image.load('meu carro.png').convert_alpha()
explosao = pygame.image.load('explosão.png').convert_alpha()
chegada = pygame.image.load('chegada.png').convert_alpha()

#Texto
font = pygame.font.SysFont(None, 48)
quit_ = font.render('RETURN', True, (0, 0, 0))


while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # posição do mouse
    mx, my = pygame.mouse.get_pos()

    # ----- Gera saídas
    window.fill((50, 255, 50))
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    window.blit(image, (0,0))


    #carrinhos
    carro1 = pygame.transform.scale(carro1, (100, 50))
    policia = pygame.transform.scale(policia, (100, 50))
    carro3 = pygame.transform.scale(carro3, (100, 50))

    #fila 1
    window.blit(carro3, (50,225))
    window.blit(carro1, (500,225))
    #fila 2
    window.blit(carro1, (100,290))
    window.blit(carro3, (700,290))
    #fila 3
    window.blit(carro1, (75,370))
    window.blit(carro1, (500,370))
    #fila 4
    window.blit(carro1, (230,450))
    window.blit(carro1, (750,450))
    # Botão de quit
    cor = (255, 255, 255)
    cor_l = (20, 20, 20)
    vertices_q = [(10, 10), (10, 50), (200, 50), (200, 10)]
    pygame.draw.polygon(window, cor, vertices_q)
    window.blit(quit_, (40, 15))
    verticess = [(0,700), (0, 520), (1000, 520), (1000, 700)]
    pygame.draw.polygon(window, cor_l, verticess)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados



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

