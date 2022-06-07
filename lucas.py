def roleta_1 (saldo):
    
    import pygame
    import time
    import random
    from menu import menu

    pygame.init()

    # ----- Variáveis
    choice_cn = "" 
    choice_a = ''
    choice_cn = "" 
    start = ''
    saldo = 1000
    i = 0
    contador = 0
    c = 0
    lista = ['VERMELHO','PRETO']
    ganhou = ''

    # ----- Funções

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

    #------------ Texto da tela inicial

    #------------Não sei
    VOP = ''
    img = font.render(VOP, True, (200,200,200))
    rect = img.get_rect()
    rect.topleft = (418, 522)
    cursor = pygame.Rect(rect.topright, (3, rect.height))

    #------------- Textos
    text0 = font.render('Quer apostar no VERMELHO ou PRETO?', True, (0, 0, 0))
    text1 = font.render('Quanto quer apostar?', True,(0,0,0))
    text2 = font.render('Seu saldo é: {}'.format( saldo), True,(0,0,0))
    text3 = font2.render('|100 = (1)|  |200 = (2)|  |300 = (3)|  |400 = (4)|  |500 = (5)|  |600 = (6)|  |700 = (7)|  |800 = (8)|  |900 = (9)|  |1000 = (0)|', True, (0,0,0))
    text4 = font.render('VERMELHO',True,(200,0,0))
    text5 = font.render('PRETO',True,(0,0,0))
    text6 = font.render('Aperte ESPAÇO para girar!', True,(0,0,0))

    #-------------- Números
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
                elif event.key == pygame.K_9:
                    choice_a = 900

                elif event.key == pygame.K_SPACE:
                    start = 1
                    girando = True
                    sorteou = False
                    ti = time.time()

                elif event.key == pygame.K_LSHIFT:
                    menu()

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
        window.blit(text2,(25,600))
        window.blit(text3,(25, 570))
        window.blit(text6,(700,600))

        # ----- Texto Variavel
        if choice_cn == "":
            img = font.render(VOP, True, (0,0,0))
            rect.size=img.get_size()
            cursor.topleft = rect.topright
            window.blit(img, rect)

            if time.time() % 1 > 0.5:
                pygame.draw.rect(window, (0,0,0), cursor)

        elif choice_cn=="VERMELHO":
            window.blit(text4,(420,522))
        elif choice_cn == "PRETO":
            window.blit(text5,(420,522 ))
        
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

    # Iniciando o Jogo: 
        if start != '':

            window.blit(base2,(0,500))

                # Texto parte nova
            texto7 = font.render('Você escolheu: {}'.format(choice_cn), True,(0,0,0))
            texto8 = font.render('Você apostou: {}'.format(choice_a), True, (0,0,0))   
            texto9 = font.render('A roleta está girando..',True,(0,0,0))

            if sorteou == False:

                sorteio = random.choice(lista)

                if sorteio == choice_cn:
                    saldo += choice_a * 2
                    texto11 = font.render('Você ganhou: {}'.format(choice_a*2), True, (0,0,0))

                else: 
                    saldo -= choice_a
                    texto11 = font.render('Você perdeu: {}'.format(choice_a), True, (0,0,0))

                sorteou = True

            window.blit(texto7,(25,522))
            window.blit(texto8,(25,545))
            window.blit(texto9,(25,570))
            
            if time.time() - ti > 2.5:
                
                texto10 = font.render('A roleta sorteou: {}'.format(sorteio), True,(0,0,0))
                window.blit(texto10,(25,597))
                pygame.draw.rect(window,(255,255,255), pygame.Rect(25,570,525,25))

            else:
                if time.time() % 1 > 0.5:
                    pygame.draw.rect(window,(0,0,0),(229,583,3,3),0)
            
            if time.time() - ti > 4:
                window.blit(texto11,(700,522))
                texto12 = font.render('Novo saldo: {}'.format(saldo), True, (0,0,0))
                window.blit(texto12,(700, 545))



                


            
            



        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

    return (saldo)
