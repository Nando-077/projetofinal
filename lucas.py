import pygame
pygame.init()
import time

# ----- Gera tela principal
window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Roleta')

#------- Input
text_ = ''
font = pygame.font.SysFont(None, 30)
img = font.render(text_, True, (200,200,200))

rect = img.get_rect()
rect.topleft = (528, 523)
cursor = pygame.Rect(rect.topright, (3, rect.height))

# ----- Inicia estruturas de dados
game = True

# ------ Carregar a mesa da roleta
mesa_1 = pygame.image.load('mesafinal.png').convert()
mesa_2 = pygame.transform.scale(mesa_1, (1000, 500))

# ------ Carregar a roleta
roleta_1 = pygame.image.load('roletafinal_.gif').convert()
roleta_2 = pygame.transform.scale(roleta_1,(250,250))

# Base do texto
base1 = pygame.image.load('basef.png').convert()
base2 = pygame.transform.scale(base1,(1000,150))

# Texto da tela inicial
font = pygame.font.SysFont(None, 30)
text = font.render('Quer apostar em uma COR (2x) ou NÚMERO (10x)?', True, (0, 0, 0))
text2 = font.render('Quanto quer apostar?', True,(0,0,0))
text3 = font.render('Seu saldo é:', True,(0,0,0))

# ===== Loop principal =====
while game:   
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

#------- Texto variável
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(text_)>0:
                            text_ = text_[:-1]
                    else:
                        text_ += event.unicode
                    img = font.render(text_, True, (0,0,0))
                    rect.size=img.get_size()
                    cursor.topleft = rect.topright

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(mesa_2, (0, 0))
    window.blit(roleta_2, (65,117))
    window.blit(base2,(0,500))

    #------ Texto não variavel
    window.blit(text, (25, 520))
    window.blit(text2,(25,545))
    window.blit(text3,(25,590))

    # ----- Texto Variável
    window.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(window, (0,0,0), cursor)


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
