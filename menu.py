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
                    saldo = crash(saldo)
                    


                elif event.key == pygame.K_2:  #japa
                    import lucas
                    saldo = lucas.roleta_1(saldo)
                    



        # posição do mouse
        #mx, my = pygame.mouse.get_pos()

        # ----- Gera saídas
        window.fill((20, 20, 20))
        crash_00 = pygame.image.load('crash.jpeg').convert_alpha()
        roleta_00 = pygame.image.load('roleta.jpeg').convert_alpha()
        roleta_00 = pygame.transform.scale(roleta_00,(400,400))
        crash_00 = pygame.transform.scale(crash_00,(400,400))
        window.blit(crash_00, (550,200))
        window.blit(roleta_00, (50,200))

        blase = pygame.image.load('crash.jpeg').convert_alpha()
        blase = pygame.transform.scale(blase,(250,250))
        window.blit(blase, (10,10))

        font = pygame.font.SysFont(None, 50)


        quadrado = [(750,10), (750, 50), (975, 50), (975, 10)]
        cor_s = (255, 255, 0)
        pygame.draw.polygon(window, cor_s, quadrado)
        grana = font.render('saldo: {} '.format(saldo), True, (0, 0, 0))
        window.blit(grana, (775, 20))
        

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()