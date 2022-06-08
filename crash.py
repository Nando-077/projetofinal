def crash (saldo):

    from re import A
    import pygame
    import numpy as np
    import random
    import time
    import os
    from menu import menu
    #from pyrsistent import*

    pygame.init()

    #criando a lista de numeros do grafico
    lista = np.arange (0.00,10.00,0.01)

    #variaves
    choice_cn = "" 
    choice_a = ''
    choice_cn = "" 
    start = ''
    i = 0
    contador = 0
    c = 0
    ganhou = ''


    WIDTH = 1000
    HEIGHT = 700
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('crash')

    game = True
    cont = True

    image = pygame.image.load('rua real.png').convert_alpha()
    carro1 = pygame.image.load('carrinho 1.png').convert_alpha()
    policia = pygame.image.load('carrinho 2.png').convert_alpha()
    carro3 = pygame.image.load('carrinho 3.png').convert_alpha()
    meucarro = pygame.image.load('meu carro.png').convert_alpha()
    explosao = pygame.image.load('explosão.png').convert_alpha()
    chegada = pygame.image.load('chegada.png').convert_alpha()

    # Base do texto
    base1 = pygame.image.load('basen.png').convert()
    base2 = pygame.transform.scale(base1,(1000,150))

    # Fontes
    font = pygame.font.SysFont(None, 27)
    font2 = pygame.font.SysFont(None,24)

    #ajustando as imagens
    carro1 = pygame.transform.scale(carro1, (100, 50))
    policia = pygame.transform.scale(policia, (100, 50))
    carro3 = pygame.transform.scale(carro3, (100, 50))
    meucarro = pygame.transform.scale(meucarro, (150, 100))
    explosao = pygame.transform.scale(explosao, (150, 100))

    #resposta 1
    VOP1 = ''
    img = font.render(VOP1, True, (200,200,200))
    rect = img.get_rect()
    rect.topleft = (700, 530)
    cursor = pygame.Rect(rect.topright, (3, rect.height))


    #Texto
    titulo = pygame.font.SysFont(None, 45)
    quit_ = titulo.render('MENU (shift)', True, (0, 0, 0))

    #------------- Textos
    text0 = font.render('Quanto o carro vai andar?', True, (0, 0, 0))
    text1 = font.render('Quanto quer apostar?', True,(0,0,0))
    text2 = font.render('Seu saldo é: {}'.format( saldo), True,(0,0,0))
    text3 = font2.render('|100 = (1)|  |200 = (2)|  |300 = (3)|  |400 = (4)|  |500 = (5)|  |600 = (6)|  |700 = (7)|  |800 = (8)|  |900 = (9)|  |1000 = (0)|', True, (0,0,0))
    text6 = font.render('Aperte ESPAÇO para começar!', True,(0,0,0))

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

    while game:


        if saldo < 0:
            game = False 
            cont = False  


        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                cont = False

    #------- Texto variável
            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_BACKSPACE:
                    if len(VOP1)>0:
                        VOP1 = VOP1[:-1]

                elif event.key == pygame.K_RETURN:
                    choice_cn = VOP1
                    choice_cn = float(choice_cn)

                elif event.key == pygame.K_j:
                    choice_a = 1000
                elif event.key == pygame.K_a:
                    choice_a = 100
                elif event.key == pygame.K_b:
                    choice_a = 200
                elif event.key == pygame.K_c:
                    choice_a = 300
                elif event.key == pygame.K_d:
                    choice_a = 400
                elif event.key == pygame.K_e:
                    choice_a = 500    
                elif event.key == pygame.K_f:
                    choice_a = 600
                elif event.key == pygame.K_g:
                    choice_a = 700
                elif event.key == pygame.K_h:
                    choice_a = 800
                elif event.key == pygame.K_i:
                    choice_a = 900

                elif event.key == pygame.K_SPACE:
                    start = 1
                    girando = True
                    sorteou = False
                    ti = time.time()
                
                elif event.key == pygame.K_LSHIFT:
                    menu(saldo)
                elif event.key == pygame.K_k:
                    from crash import crash
                    crash(saldo)

                else:
                    VOP1 += event.unicode
                        
        
                        

        # ----- Gera saídas
        window.fill((50, 255, 50))
        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
        window.blit(image, (0,0))

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
        vertices_q = [(10, 10), (10, 70), (250, 70), (250, 10)]
        pygame.draw.polygon(window, cor, vertices_q)
        window.blit(quit_, (40, 15))
        verticess = [(0,700), (0, 520), (1000, 520), (1000, 700)]
        pygame.draw.polygon(window, cor_l, verticess)
        window.blit(base2,(0,500))

        #------ Texto não variavel
        window.blit(text0, (25, 522))
        window.blit(text1,(25,550))
        window.blit(text2,(25,600))
        window.blit(text3,(25, 583))
        window.blit(text6,(530,600))

        # ----- Texto Variavel
        if choice_cn == "":
            img = font.render(VOP1, True, (0,0,0))
            rect.size=img.get_size()
            cursor.topleft = rect.topright
            window.blit(img, rect)

            if time.time() % 1 > 0.5:
                pygame.draw.rect(window, (0,0,0), cursor)

        # ----- Escolha da aposta
        if choice_a != '':
            pygame.draw.rect(window, (255,255,255), pygame.Rect(25, 580, 900, 30))
            if choice_a == 100:
                window.blit(a100,(25,575))
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

            text4 = font.render('{}'.format( choice_cn), True,(0,0,0))
            window.blit(text4,(700, 530))
            window.blit(text2,(25,600))
            window.blit(text6,(530,600))
        
        # ----- Escolha da aposta
        #if choice_a != '':
            #pygame.draw.rect(window, (255,0,255), pygame.Rect(25, 580, 900, 30))


    # Iniciando o Jogo: 
        if start != '':

            window.blit(base2,(0,500))

                # Texto parte nova
            texto7 = font.render('Você escolheu: {}'.format(choice_cn), True,(0,0,0))
            texto8 = font.render('Você apostou: {}'.format(choice_a), True, (0,0,0))   
            texto9 = font.render('O carro esta correndo!..',True,(0,0,0))

            if sorteou == False:

                sorteio = random.choice(lista)

                if sorteio >= choice_cn:
                    saldo += (choice_a * choice_cn) - choice_a 
                    x = (choice_a * choice_cn) - choice_a
                    texto11 = font.render('Você ganhou: {}'.format(x), True, (0,0,0))
                    paisagem = True

                if sorteio < choice_cn: 
                    
                    paisagem = False

                    saldo -= choice_a
                    texto11 = font.render('Você perdeu: {}'.format(choice_a), True, (0,0,0))

                    



                sorteou = True

            window.blit(texto7,(25,522))
            window.blit(texto8,(25,545))
            window.blit(texto9,(25,570))
            
            if time.time() - ti > 2.5:
                
                texto10 = font.render('A roleta sorteou: {}'.format(sorteio), True,(0,0,0))
                window.blit(texto10,(25,597))
                #pygame.draw.rect(window,(255,255,255), pygame.Rect(25,570,525,25))

            #else:
                #if time.time() % 1 > 0.5:
                    #pygame.draw.rect(window,(0,0,0),(229,583,3,3),0)
            
            if time.time() - ti > 4:
            
                if paisagem == True:
                    # ----- Gera saídas
                    window.fill((50, 255, 50))
                    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                    window.blit(image, (0,0))


                    #carrinhos
                    meucarro = pygame.transform.scale(meucarro, (150, 100))

                    # chegada
                    window.blit(chegada, (700,215))

                    #fila 2

                    window.blit(meucarro, (700,260))

                    # Botão de quit
                    cor = (255, 255, 255)
                    cor_l = (20, 20, 20)
                    vertices_q = [(10, 10), (10, 50), (200, 50), (200, 10)]
                    pygame.draw.polygon(window, cor, vertices_q)
                    window.blit(quit_, (40, 15))
                    verticess = [(0,700), (0, 520), (1000, 520), (1000, 700)]
                    pygame.draw.polygon(window, cor_l, verticess)

                

                if paisagem == False:
                    # ----- Gera saídas
                    window.fill((50, 255, 50))
                    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                    window.blit(image, (0,0))
                    #carrinhos
                    carro1 = pygame.transform.scale(carro1, (100, 50))
                    policia = pygame.transform.scale(policia, (100, 50))
                    carro3 = pygame.transform.scale(carro3, (100, 50))
                    meucarro = pygame.transform.scale(meucarro, (150, 100))
                    explosao = pygame.transform.scale(explosao, (150, 100))
                    #fila 1
                    window.blit(carro3, (50,225))
                    window.blit(carro1, (500,225))
                    #fila 2
                    window.blit(carro1, (100,290))
                    window.blit(carro3, (700,290))
                    window.blit(meucarro, (300,260))
                    window.blit(policia, (420,290))
                    window.blit(explosao, (360,250))
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
                window.blit(base2,(0,500))
                window.blit(quit_, (40, 15))
                window.blit(texto11,(700,522))
                texto12 = font.render('Novo saldo: {}'.format(saldo), True, (0,0,0))
                window.blit(texto12,(700, 545))
                window.blit(texto7,(25,522))
                window.blit(texto8,(25,545))
                window.blit(texto9,(25,570))
                window.blit(texto10,(25,597))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
    

    # ===== Finalização =====
    #pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

    return (saldo)

    

