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

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(mesa_2, (10, 10))
    window.blit(roleta_2, (75,127))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
