import pygame
import random
import time

game = True

pygame.init()

font = pygame.font.SysFont(None, 28)

palavra_secreta = 'sublime'
#palavra_secreta = ['sublime', 'sentido','futebol','refutar','cordial','estupro','coragem','erudito','exilado','racismo','preciso','impacto']
lista_x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lista_p =[(175,185),(210,185),(245,185),(280,185),(315,185),(350,185),(385,185)]
i = 0
c = 0
start = ''
VOP = ''
choice_a = ''
 
window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Cofre')

text0 = font.render('Chute uma letra:', True, (0, 0, 0))
texta = font.render('A', True, (0, 0, 0))
textb = font.render('B', True, (0, 0, 0))
textc = font.render('C', True, (0, 0, 0))
textd = font.render('D', True, (0, 0, 0))
texte = font.render('E', True, (0, 0, 0))
textf = font.render('F', True, (0, 0, 0))
textg = font.render('G', True, (0, 0, 0))
texth = font.render('H', True, (0, 0, 0))
texti = font.render('I', True, (0, 0, 0))
textj = font.render('J', True, (0, 0, 0))
textk = font.render('K', True, (0, 0, 0))
textl = font.render('L', True, (0, 0, 0))
textm = font.render('M', True, (0, 0, 0))
textn = font.render('N', True, (0, 0, 0))
texto = font.render('O', True, (0, 0, 0))
textp = font.render('P', True, (0, 0, 0))
textq = font.render('Q', True, (0, 0, 0))
textr = font.render('R', True, (0, 0, 0))
texts = font.render('S', True, (0, 0, 0))
textt = font.render('T', True, (0, 0, 0))
textu = font.render('U', True, (0, 0, 0))
textv = font.render('V', True, (0, 0, 0))
textw = font.render('W', True, (0, 0, 0))
textx = font.render('X', True, (0, 0, 0))
texty = font.render('Y', True, (0, 0, 0))
textz = font.render('Z', True, (0, 0, 0))

lista_l = [texta,textb,textc,textd,texte,textf,textg,texth,texti,textj,textk,textl,textm,textn,texto,textp,textq,textr,texts,textt,textu,textv,textw,textx,texty,textz]

cofre = pygame.image.load('cofre.png').convert()
cofre2 = pygame.transform.scale(cofre, (650, 650))
t = pygame.transform.scale(cofre,(20,20))

base = pygame.image.load('base_l.png').convert()
base2 = pygame.transform.scale(base,(350,850))

img = font.render(VOP, True, (200,200,200))
rect = img.get_rect()
rect.topleft = (850, 522)
cursor = pygame.Rect(rect.topright, (3, rect.height))

while game:

    seleciona_palavra = random.choice(palavra_secreta)
    digitando = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(VOP)>0:
                    VOP = VOP[:-1]

            elif event.key == pygame.K_RETURN:
                choice_a = VOP
                start = 1
            else:
                VOP += event.unicode
            
    window.fill((255, 255, 255))  # Preenche com a cor branca

    window.blit(cofre2, (0, 0))
    window.blit(base2,(650,0))
    window.blit(text0, (690, 522))

    if choice_a == "":

        img = font.render(choice_a, True, (0,0,0))
        rect.size=img.get_size()
        cursor.topleft = rect.topright
        window.blit(img, rect)
        
        if time.time() % 1 > 0.5:
            pygame.draw.rect(window, (0,0,0), cursor)

    if start == 1:
        if choice_a in seleciona_palavra:
            while i <= len(seleciona_palavra):
                if seleciona_palavra[i] == choice_a:
                    posicao = lista_p[i]
                i += 1
            while c <= len(lista_l):
                if choice_a == lista_x[c]:
                    texto = lista_l[c]
                c += 1
            window.blit(texto,posicao)




    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados