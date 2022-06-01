import pygame
pygame.init()
import time

# ----- Variáveis
choice_cn = "" 
choice_a = ''
saldo = 1000
i = 0

# ----- Funções
# ----- Lista VOP
lista_vermelho = []
lista_preto = []

while i <= 36:

    if i % 2 == 0:
        lista_vermelho.append(i)
    elif i % 2 != 0:
        lista_preto.append(i)

    i += 1

# ----- Gera tela principal
window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Roleta')

# ----- Inicia estruturas de dados
game = True

# ------ Carregar a mesa da roleta
mesa_1 = pygame.image.load('mesafinal.png').convert()
mesa_2 = pygame.transform.scale(mesa_1, (1000, 500))

# ------ Carregar a roleta
roleta_1 = pygame.image.load('roletafinal_.gif').convert()
roleta_2 = pygame.transform.scale(roleta_1,(250,250))

# Base do texto
base1 = pygame.image.load('basen.png').convert()
base2 = pygame.transform.scale(base1,(1000,150))

# Fontes
font = pygame.font.SysFont(None, 28)
font2 = pygame.font.SysFont(None,25)

#Texto da tela inicial

VOP = ''
img = font.render(VOP, True, (200,200,200))
rect = img.get_rect()
rect.topleft = (425, 520)
cursor = pygame.Rect(rect.topright, (3, rect.height))
text0 = font.render('Quer apostar no VERMELHO ou PRETO?', True, (0, 0, 0))
text1 = font.render('Quanto quer apostar?', True,(0,0,0))
text2 = font.render('Seu saldo é:', True,(0,0,0))
text3 = font2.render('|100 = (1)|  |200 = (2)|  |300 = (3)|  |400 = (4)|  |500 = (5)|  |600 = (6)|  |700 = (7)|  |800 = (8)|  |900 = (9)|  |1000 = (0)|', True, (0,0,0))
text4 = font.render('VERMELHO',True,(0,0,0))
text5 = font.render('PRETO',True,(0,0,0))
a100 = font.render('100', True,(0,0,0))
a200 = font.render('200', True,(0,0,0))
a300 = font.render('300', True,(0,0,0))
a400 = font.render('400', True,(0,0,0))
a500 = font.render('500', True,(0,0,0))
a600 = font.render('600', True,(0,0,0))
a700 = font.render('700', True,(0,0,0))
a800 = font.render('800', True,(0,0,0))
a900 = font.render('900', True,(0,0,0))
a1000 = font.render('1000', True,(0,0,0))

choice_cn = "" 
# ===== Loop principal =====
while game:

    if saldo < 0:
        game = False   

    # ----- Trata eventos
    for event in pygame.event.get():

        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

#------- Texto variável
        if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:
                        if len(VOP)>0:
                            VOP = VOP[:-1]

                    elif event.key == pygame.K_RETURN:
                        if VOP == 'vermelho':
                            choice_cn="VERMELHO"
                        elif VOP == 'preto':
                            choice_cn="PRETO"

                    elif event.key == pygame.K_0:
                        choice_a = 1000
                    elif event.key == pygame.K_1:
                        choice_a = 100
                    elif event.key == pygame.K_2:
                        choice_a = 200
                    elif event.key == pygame.K_3:
                        choice_a = 300
                    elif event.key == pygame.K_4:
                        choice_a = 400
                    elif event.key == pygame.K_5:
                        choice_a = 500    
                    elif event.key == pygame.K_6:
                        choice_a = 600
                    elif event.key == pygame.K_7:
                        choice_a = 700
                    elif event.key == pygame.K_8:
                        choice_a = 800
                    elif event.key == pygame.K_0:
                        choice_a = 900
                    else:
                        VOP += event.unicode
                    
    
                    

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(mesa_2, (0, 0))
    window.blit(roleta_2, (65,117))
    window.blit(base2,(0,500))

    #------ Texto não variavel
    window.blit(text0, (25, 522))
    window.blit(text1,(25,545))
    window.blit(text2,(25,610))
    window.blit(text3,(25, 580))

    # ----- Texto Variavel
    if choice_cn == "":
        img = font.render(VOP, True, (0,0,0))
        rect.size=img.get_size()
        cursor.topleft = rect.topright
        window.blit(img, rect)

        if time.time() % 1 > 0.5:
            pygame.draw.rect(window, (0,0,0), cursor)

    elif choice_cn=="VERMELHO":
        window.blit(text4,(425,522))
    elif choice_cn == "PRETO":
        window.blit(text5,(425,522 ))

    # ----- Escolha da aposta
    if choice_a != '':
        pygame.draw.rect(window, (255,255,255), pygame.Rect(25, 570, 900, 30))
        if choice_a == 100:
            window.blit(a100,(25,570))
        elif choice_a == 200:
            window.blit(a200,(25,570))
        elif choice_a == 300:
            window.blit(a300,(25,570))
        elif choice_a == 400:
            window.blit(a400,(25,570))
        elif choice_a == 500:
            window.blit(a500,(25,570))
        elif choice_a == 600:
            window.blit(a600,(25,570))
        elif choice_a == 700:
            window.blit(a700,(25,570))
        elif choice_a == 800:
            window.blit(a800,(25,570))
        elif choice_a == 900:
            window.blit(a900,(25,570))
        elif choice_a == 1000:
            window.blit(a1000,(25,570))




    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
