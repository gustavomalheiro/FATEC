# JOGNA1 - Entrega N1.C - Grupo 8 - Dominickie Peres Ferreira, Gustavo Malheiro, Gustavo Martins Ferrari, Lucas Lessa de Macedo

import pygame
from pygame.locals import *

lista_cores = []
CorJogador1 = (200, 200, 250) #As dimensões são todas divisiveis por 15 [- 20]
CorJogador1S = (150, 150, 200)
CorJogador2 = (250, 250, 200)
CorJogador2S = (200, 200, 150)
CorJogador3 = (250, 200, 200)
CorJogador3S = (200, 150, 150)
CorJogador4 = (200, 250, 200)
CorJogador4S = (150, 200, 150)

# adicionando cores principais em listas
lista_cores.append(CorJogador1)
lista_cores.append(CorJogador2)
lista_cores.append(CorJogador3)
lista_cores.append(CorJogador4)

Preto = (0, 0, 0)
Branco = (255, 255, 255)
pygame.init() 
tela = pygame.display.set_mode((640, 640), 0, 32)
pygame.display.set_caption('LUDO - time8')
fim = False

relogio = pygame.time.Clock()

x = 0 # azul
y = 1 # amarela
z = 2 # vermelha 
w = 3 # verde

while not fim:
    relogio.tick(2)

    tela.fill(Branco)
    pygame.draw.rect(tela,CorJogador1, (40 + 20, 280 + 20, 240, 40))#parte colorida de andar
    pygame.draw.rect(tela,CorJogador1, (40 + 20, 240 + 20, 40, 40))
    pygame.draw.rect(tela,CorJogador2, (280 + 20, 40 + 20, 40, 240))
    pygame.draw.rect(tela,CorJogador2, (320 + 20, 40 + 20, 40, 40))
    pygame.draw.rect(tela,CorJogador4, (320 + 20, 280 + 20, 240, 40))
    pygame.draw.rect(tela,CorJogador4, (520 + 20, 320 + 20, 40, 40))
    pygame.draw.rect(tela,CorJogador3, (280 + 20, 320 + 20, 40, 240))
    pygame.draw.rect(tela,CorJogador3, (240 + 20, 520 + 20, 40, 40))
    j = 0
    while j < 3:
        i = 0
        while i < 30:
            pygame.draw.line(tela, Preto, (0 + 20, 0 + 20 + (i*40)), (640 - 20, 0 + 20 + (i*40)), 1)
            pygame.draw.line(tela, Preto, (0 + 20 + (i*40), 0 + 20), (0 + 20 + (i*40), 640 - 20), 1)#grade de linhas
            i += 1
        j += 1
    
    # logica para a animcação
    if x > 3:
        x = 0
    elif y > 3:
        y = 0
    elif z > 3:
        z = 0
    elif w > 3:
        w = 0

    if x == 0:
       x = 0
       y = 1
       z = 2
       w = 3
    elif y == 0:
       x = 3
       y = 0
       z = 1
       w = 2 
    elif z == 0:
       x = 2
       y = 3
       z = 0
       w = 1
    elif w == 0:
       x = 1
       y = 2
       z = 3
       w = 0
    
    pygame.draw.rect(tela,lista_cores[x], (0 + 20, 0 + 20, 240, 240))#area colorida dos jogadores
    pygame.draw.rect(tela,lista_cores[w], (360 + 20, 0 + 20, 240, 240))
    pygame.draw.rect(tela,lista_cores[y], (0 + 20, 360 + 20, 240, 240))
    pygame.draw.rect(tela,lista_cores[z], (360 + 20, 360 +20, 240, 240))
    pygame.draw.rect(tela,Preto, (0 + 20, 0 + 20, 240, 240), 1)
    pygame.draw.rect(tela,Preto, (360 + 20, 0 + 20, 240, 240), 1)
    pygame.draw.rect(tela,Preto, (0 + 20, 360 + 20, 240, 240), 1)
    pygame.draw.rect(tela,Preto, (360 + 20, 360 +20, 240, 240), 1)

    pygame.draw.rect(tela, Branco, (40 + 20, 40 + 20, 160, 160))#area branca dos jogadores
    pygame.draw.rect(tela, Preto, (40 + 20, 40 + 20, 160, 160), 1)
    pygame.draw.rect(tela, Branco, (400 + 20, 40 + 20, 160, 160))
    pygame.draw.rect(tela, Preto, (400 + 20, 40 + 20, 160, 160), 1)
    pygame.draw.rect(tela, Branco, (40 + 20, 400 + 20, 160, 160))
    pygame.draw.rect(tela, Preto, (40 + 20, 400 + 20, 160, 160), 1)
    pygame.draw.rect(tela, Branco, (400 + 20, 400 + 20, 160, 160))
    pygame.draw.rect(tela, Preto, (400 + 20, 400 + 20, 160, 160), 1)

    pygame.draw.rect(tela, CorJogador1, (40 + 30, 40 + 30, 60, 60)) #casas da peças; 10 de contorno /4
    pygame.draw.rect(tela, CorJogador1, (120 + 30, 40 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador1, (40 + 30, 120 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador1, (120 + 30, 120 + 30, 60, 60))
    pygame.draw.rect(tela, Preto, (40 + 30, 40 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (120 + 30, 40 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (40 + 30, 120 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (120 + 30, 120 + 30, 60, 60), 1)

    pygame.draw.rect(tela, CorJogador2, (400 + 30, 40 + 30, 60, 60)) #adiciona (2*o quadrado de andar) em cada uma das coordenadas e 10 pelo contorno
    pygame.draw.rect(tela, CorJogador2, (480 + 30, 40 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador2, (400 + 30, 120 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador2, (480 + 30, 120 + 30, 60, 60))
    pygame.draw.rect(tela, Preto, (400 + 30, 40 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (480 + 30, 40 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (400 + 30, 120 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (480 + 30, 120 + 30, 60, 60), 1)

    pygame.draw.rect(tela, CorJogador3, (40 + 30, 400 + 30, 60, 60)) 
    pygame.draw.rect(tela, CorJogador3, (120 + 30, 400 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador3, (40 + 30, 480 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador3, (120 + 30, 480 + 30, 60, 60))
    pygame.draw.rect(tela, Preto, (40 + 30, 400 + 30, 60, 60), 1) 
    pygame.draw.rect(tela, Preto, (120 + 30, 400 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (40 + 30, 480 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (120 + 30, 480 + 30, 60, 60), 1)

    pygame.draw.rect(tela, CorJogador4, (400 + 30, 400 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador4, (480 + 30, 400 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador4, (400 + 30, 480 + 30, 60, 60))
    pygame.draw.rect(tela, CorJogador4, (480 + 30, 480 + 30, 60, 60))
    pygame.draw.rect(tela, Preto, (400 + 30, 400 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (480 + 30, 400 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (400 + 30, 480 + 30, 60, 60), 1)
    pygame.draw.rect(tela, Preto, (480 + 30, 480 + 30, 60, 60), 1)

    pygame.draw.polygon(tela, CorJogador1, ((240 + 20, 240 + 20), (240 + 20, 360 + 20), (300 + 20, 300 + 20)), 0)#triângulos centro e contorno
    pygame.draw.lines(tela, Preto, True, ((240 + 20, 240 + 20), (240 + 20, 360 + 20), (300 + 20, 300 + 20)),1)
    pygame.draw.polygon(tela, CorJogador2, ((360 + 20, 360 + 20), (360 + 20, 240 + 20), (300 + 20, 300 + 20)), 0)
    pygame.draw.lines(tela, Preto, True, ((360 + 20, 360 + 20), (360 + 20, 240 + 20), (300 + 20, 300 + 20)),1)
    pygame.draw.polygon(tela, CorJogador3, ((360 + 20, 360 + 20), (240 + 20, 360 + 20), (300 + 20, 300 + 20)), 0)
    pygame.draw.lines(tela, Preto, True, ((360 + 20, 360 + 20), (240 + 20, 360 + 20), (300 + 20, 300 + 20)),1)
    pygame.draw.polygon(tela, CorJogador4, ((240 + 20, 240 + 20), (360 + 20, 240 + 20), (300 + 20, 300 + 20)), 0)
    pygame.draw.lines(tela, Preto, True, ((240 + 20, 240 + 20), (360 + 20, 240 + 20), (300 + 20, 300 + 20)),1)

    pygame.draw.circle(tela, CorJogador1S, (80 + 20, 80 + 20), 20) #Peças
    pygame.draw.circle(tela, CorJogador1S, (160 + 20, 80 + 20), 20)
    pygame.draw.circle(tela, CorJogador1S, (80 + 20, 160 + 20), 20)
    pygame.draw.circle(tela, CorJogador1S, (160 + 20, 160 + 20), 20)
    pygame.draw.circle(tela, Preto, (80 + 20, 80 + 20), 20, 1) #Jogador 1
    pygame.draw.circle(tela, Preto, (160 + 20, 80 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (80 + 20, 160 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (160 + 20, 160 + 20), 20, 1)

    pygame.draw.circle(tela, CorJogador3S, (80 + 20, 440 + 20), 20)
    pygame.draw.circle(tela, CorJogador3S, (160 + 20, 440 + 20), 20)
    pygame.draw.circle(tela, CorJogador3S, (80 + 20, 520 + 20), 20)
    pygame.draw.circle(tela, CorJogador3S, (160 + 20, 520 + 20), 20)
    pygame.draw.circle(tela, Preto, (80 + 20, 440 + 20), 20, 1) #Jogador 3
    pygame.draw.circle(tela, Preto, (160 + 20, 440 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (80 + 20, 520 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (160 + 20, 520 + 20), 20, 1)

    pygame.draw.circle(tela, CorJogador2S, (440 + 20, 80 + 20), 20)
    pygame.draw.circle(tela, CorJogador2S, (520 + 20, 80 + 20), 20)
    pygame.draw.circle(tela, CorJogador2S, (440 + 20, 160 + 20), 20)
    pygame.draw.circle(tela, CorJogador2S, (520 + 20, 160 + 20), 20)
    pygame.draw.circle(tela, Preto, (440 + 20, 80 + 20), 20, 1) #Jogador 2
    pygame.draw.circle(tela, Preto, (520 + 20, 80 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (440 + 20, 160 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (520 + 20, 160 + 20), 20, 1)

    pygame.draw.circle(tela, CorJogador4S, (440 + 20, 440 + 20), 20)
    pygame.draw.circle(tela, CorJogador4S, (440 + 20, 520 + 20), 20)
    pygame.draw.circle(tela, CorJogador4S, (520 + 20, 440 + 20), 20)
    pygame.draw.circle(tela, CorJogador4S, (520 + 20, 520 + 20), 20)
    pygame.draw.circle(tela, Preto, (440 + 20, 440 + 20), 20, 1) #Jogador 4
    pygame.draw.circle(tela, Preto, (440 + 20, 520 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (520 + 20, 440 + 20), 20, 1)
    pygame.draw.circle(tela, Preto, (520 + 20, 520 + 20), 20, 1)

    pygame.draw.polygon(tela, CorJogador3S, ((240 + 20, 560 + 20), (240 + 20, 520 + 20), (240 + 12 + 20, 520 + 15 + 20), (260 + 20, 520 + 20), (280 - 12 + 20, 520 + 15 + 20), (280 + 20, 520 + 20), (280 + 20, 560 + 20)), 0)
    pygame.draw.lines(tela, Preto, True, ((240 + 20, 560 + 20), (240 + 20, 520 + 20), (252 + 20, 535 + 20), (260 + 20, 520 + 20), (268 + 20, 535 + 20), (280 + 20, 520 + 20), (280 + 20, 560 + 20)),1)

    pygame.draw.polygon(tela, CorJogador1S, ((40 + 20, 280 + 20), (40 + 20, 240 + 20), (40 + 12 + 20, 240 + 15 + 20), (40 + 20 + 20, 240 + 20), (80 - 12 + 20, 240 + 15 + 20), (80 + 20, 240 + 20), (80 + 20, 280 + 20)), 0)
    pygame.draw.lines(tela, Preto, True, ((40 + 20, 280 + 20), (40 + 20, 240 + 20), (40 + 12 + 20, 240 + 15 + 20), (40 + 20 + 20, 240 + 20), (80 - 12 + 20, 240 + 15 + 20), (80 + 20, 240 + 20), (80 + 20, 280 + 20)),1)

    pygame.draw.polygon(tela, CorJogador2S, ((320 + 20, 80 + 20), (320 + 20, 40 + 20), (320 + 12 + 20, 40 + 15 + 20), (320 + 20 + 20, 40 + 20), (360 - 12 + 20, 40 + 15 + 20), (360 + 20, 40 + 20), (360 + 20, 80 + 20)), 0)
    pygame.draw.lines(tela, Preto, True, ((320 + 20, 80 + 20), (320 + 20, 40 + 20), (320 + 12 + 20, 40 + 15 + 20), (320 + 20 + 20, 40 + 20), (360 - 12 + 20, 40 + 15 + 20), (360 + 20, 40 + 20), (360 + 20, 80 + 20)),1)

    pygame.draw.polygon(tela, CorJogador4S, ((520 + 20, 360 + 20), (520 + 20, 320 + 20), (520 + 12 + 20, 320 + 15 + 20), (520 + 20 + 20, 320 + 20), (560 - 12 + 20, 320 + 15 + 20), (560 + 20, 320 + 20), (560 + 20, 360 + 20)), 0)
    pygame.draw.lines(tela, Preto, True, ((520 + 20, 360 + 20), (520 + 20, 320 + 20), (520 + 12 + 20, 320 + 15 + 20), (520 + 20 + 20, 320 + 20), (560 - 12 + 20, 320 + 15 + 20), (560 + 20, 320 + 20), (560 + 20, 360 + 20)),1)
    
    #j = 0
    #while j < 1:
    #    i = 0
    #    while i < 2:
    #        pygame.draw.rect(tela, (0, 0, 0), (430+i*80, 430+j, 60, 60), )#i eixo X; j eixo Y (MELHOR IGNORAR)
    #        i += 1
    #        j += 1
    

    pygame.draw.rect(tela, Preto, (0, 0, 640, 640), 20) #bordas
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
          fim = True
    
    x += 1
    y += 1
    z += 1
    w += 1

pygame.display.quit()
