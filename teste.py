import pygame
from pygame.locals import *
import time
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((1000, 650))

text = 'this text is editable'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)

rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))

running = True
background = GRAY

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size=img.get_size()
            cursor.topleft = rect.topright
    
    screen.fill(background)
    screen.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, RED, cursor)
    pygame.display.update()

pygame.quit()

#------- Input
COR_OU_NUMERO = ''
font = pygame.font.SysFont(None, 30)
img = font.render(COR_OU_NUMERO, True, (200,200,200))
window = 2

#------- Texto variável
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_BACKSPACE:
        if len(COR_OU_NUMERO)>0:
            COR_OU_NUMERO = COR_OU_NUMERO[:-1]
        elif event.key == pygame.K_RETURN:
            TEXTO_COR_OU_NUMERO = font.render('{}'.format(COR_OU_NUMERO),True,(0,0,0))
            window.blit(TEXTO_COR_OU_NUMERO,(100,600))
        else:
            COR_OU_NUMERO += event.unicode
            img = font.render(COR_OU_NUMERO, True, (0,0,0))
            rect.size=img.get_size()
            cursor.topleft = rect.topright

    # ----- Texto Variavel
    window.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(window, (0,0,0), cursor)


