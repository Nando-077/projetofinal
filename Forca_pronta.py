#jogo da forca
from random import choice
from time import sleep


palavra_secreta = ['geladeira', 'cadeira', 'casa', 'moradia',
 'churrasco', 'familia', 'ninho', 'teatro','casamento', 'cinema', 'filme',
 'amarelo', 'azul', 'vermelho','sociedade', 'esporte', 'futebol', 'basquete']
  


linhas = []
letras_escolhidas = []
seleciona_palavra = choice(palavra_secreta).lower()
cont = 1

letras_erradas = ''
le = 0

palavra_escolhida = list(seleciona_palavra)

ganhou = False
vidas = 6

#Transforma o tamanho da palavra escolhida em traços
for t in range(0, len(palavra_escolhida)):
  linhas.append('_')


while ganhou == False: 
  acertou = 0 
  print(f'\n♥️{vidas}️\n')
  
  print(f'Letras Erradas: {letras_erradas[:-2].upper()}\n')
  print(f"{'PALAVRA':^14}\n\n")
  
  for t in range(0, len(palavra_escolhida)):
    if ' ' in palavra_escolhida[t]:
      linhas[t] = '-'
    print(linhas[t].upper(), end=' ')
  print('\n')
 
 #Se acabar as vidas, fim de jogo
  if vidas < 1:
    print(f"\n{'GAME OVER':^18}\n\n- Suas vidas acabaram\nA PALAVRA ERA {seleciona_palavra.upper()}")
    break
    
  #Input 
  letra = input('Letra: ').lower().strip()
  savle = letra
  print('\n')
  
  #Verificação
  detect_espaço = savle.isspace()
  detect_letra = savle.isalpha()
  
   #Tranforma os traços em letras

  for t in range(0, len(palavra_escolhida)):
    if palavra_escolhida[t] in letra:
      linhas[t] = palavra_escolhida[t]
      acertou = acertou + 1
 
  #Tira vida caso a letra n esteja na palavra
  if acertou < 1 and savle not in letras_escolhidas:
    print('\n' * 5)
    print(f"- A letra '{savle.upper()}' não está na palavra \n\n{'-1♥️':^37}","\n" * 6)   
    sleep(2)
    vidas -= 1    
    letras_erradas += savle + ', '
  else:
    print('\n' * 5)
  
  #letras ja usadas
  if savle in letras_escolhidas:
    print(f"- A letra '{savle.upper()}' já foi usada", "\n" * 5)
    sleep(3)
  else:  
    letras_escolhidas.append(savle)
    
#Decide vitória
  if not '_' in linhas:
    for t in range(0, len(palavra_escolhida)):
      print(linhas[t].upper(), end=' ')
    print('\n')

    print(f'PARABÉNS VOCÊ ACERTOU A PALAVRA: \n{seleciona_palavra.upper()}\n\n')
    ganhou = True
