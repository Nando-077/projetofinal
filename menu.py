def menu():
    import pygame

    from crash import crash

    pygame.init()

    #Variavel
    saldo = 1000

    WIDTH = 1000
    HEIGHT = 700
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Jogo')

    game = True

    crash_00 = pygame.image.load('crash.jpeg').convert_alpha()
    roleta_00 = pygame.image.load('roleta.jpeg').convert_alpha()
    window.blit(crash_00, (100,225))
    window.blit(roleta_00, (50,225))


    #Texto
    font = pygame.font.SysFont(None, 48)
    quit_ = font.render('RETURN', True, (0, 0, 0))


    while game:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:  #nando
                    crash(saldo)
                    


                elif event.key == pygame.K_2:  #japa
                    import lucas
                    lucas.roleta_1(saldo)
                    



        # posição do mouse
        #mx, my = pygame.mouse.get_pos()

        # ----- Gera saídas
        window.fill((20, 20, 20))
        verticess_2 = [(25,100), (25, 600), (450, 600), (450, 100)]
        verticess_3 = [(550,100), (550, 600), (975, 600), (975, 100)]
        cor_l = (255, 255, 255)
        pygame.draw.polygon(window, cor_l, verticess_2)
        pygame.draw.polygon(window, cor_l, verticess_3)

        font = pygame.font.SysFont(None, 50)
        jogo_1 = font.render('1', True, (0, 0, 0))
        jogo_3 = font.render('2', True, (0, 0, 0))
        window.blit(jogo_1, (225, 100))
        window.blit(jogo_3, (775, 100))

        quadrado = [(750,10), (750, 50), (975, 50), (975, 10)]
        cor_s = (255, 255, 0)
        pygame.draw.polygon(window, cor_s, quadrado)
        grana = font.render('saldo: {} '.format(saldo), True, (0, 0, 0))
        window.blit(grana, (775, 20))
        

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()