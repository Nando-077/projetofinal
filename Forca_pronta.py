#jogo da forca
from random import choice
from time import sleep


palavra_secreta = ['sublime', 'cadeira', 'empatia', 'moradia',
 'excesso', 'familia', 'parcial', 'alegria','certeza', 'escasso', 'modesto',
 'amarelo', 'sentido', 'bizarro','ousadia', 'esporte', 'futebol']
  
 
#Seleciona palavra

linhas = []
letras_escolhidas = []
seleciona_palavra = choice(palavra_secreta).lower()
cont = 1

letras_erradas = ''
le = 0

palavra_escolhida = list(seleciona_palavra)

ganhou_jogo = False
vidas = 5

#Transforma o tamanho da palavra escolhida em traços
for t in range(0, len(palavra_escolhida)):
  linhas.append('_')


while ganhou_jogo == False: 
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
  key = letra
  print('\n')
  
  #Verificação
  detect_espaço = key.isspace()
  detect_letra = key.isalpha()
  
   #Tranforma os traços em letras

  for t in range(0, len(palavra_escolhida)):
    if palavra_escolhida[t] in letra:
      linhas[t] = palavra_escolhida[t]
      acertou = acertou + 1
 
#Tira vida caso a letra não esteja na palavra
  if acertou < 1 and key not in letras_escolhidas:
    print('\n' * 5)
    print(f"- A letra '{key.upper()}' não está na palavra \n\n{'-1♥️':^37}","\n" * 6)   
    sleep(2)
    vidas -= 1    
    letras_erradas += key + ', '
  else:
    print('\n' * 5)
  
#Interface
  if vida == 5:

  elif vida == 4:

  elif vida == 3:

  elif vida ==2 :

  elif vida ==1:


 #letras ja usadas
  if key in letras_escolhidas:
    print(f"- A letra '{key.upper()}' já foi usada", "\n" * 5)
    sleep(3)
  else:  
    letras_escolhidas.append(key)
    
#Decide vitória
  if not '_' in linhas: 
    for t in range(0, len(palavra_escolhida)):
      print(linhas[t].upper(), end=' ')
    print('\n')

    print(f'PARABÉNS VOCÊ GANHOU!! ACERTOU A PALAVRA: \n{seleciona_palavra.upper()}\n\n')
    ganhou_jogo = True
