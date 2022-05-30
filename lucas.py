import pygame
pygame.init()

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
base1 = pygame.image.load('basef.png').convert()
base2 = pygame.transform.scale(base1,(1000,150))

# Texto da tela inicial
font = pygame.font.SysFont(None, 30)
text = font.render('Seja bem-vindo a roleta', True, (0, 0, 0))
text2 = font.render('Na roleta você pode apostar em uma COR (2x) ou em um NÚMERO (10x)', True,(0,0,0))
text3 = font.render('Aperte a BARRA DE ESPAÇO para começar!', True,(0,0,0))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(mesa_2, (0, 0))
    window.blit(roleta_2, (65,117))
    window.blit(base2,(0,500))

    #------ TEXTo
    window.blit(text, (25, 520))
    window.blit(text2,(25,545))
    window.blit(text3,(25,590))
   
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
