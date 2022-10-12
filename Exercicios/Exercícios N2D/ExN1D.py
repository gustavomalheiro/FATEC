# JOGNA1 - Entrega N1.C - Dominickie Peres Ferreira, Gustavo Malheiro, Gustavo Martins Ferrari, Lucas Lessa Macedo
import pygame
from pygame.locals import *
from sys import exit

Arq = open("dados2.txt", "r")

s = Arq.readline().strip()
s = s.split("|")

LarTela = int(s[0])
AltTela = int(s[1])

cor = Arq.readline().strip()
cor = cor.split("|")
CorFundo = (int(cor[0]), int(cor[1]), int(cor[2]))

s = Arq.readline().strip()
Linhas = []
while  s != '':
    s = s.split("|")
    for i in range(len(s)):
        s[i] = int(s[i])
    Linhas.append(s)
    s = Arq.readline().strip()
Arq.close()

pygame.init()
tela = pygame.display.set_mode((LarTela, AltTela))
pygame.display.set_caption("JOGNA1 – Entrega N1.D")

while True:
    tela.fill(CorFundo)

    for l in Linhas:
        Inicial = (l[0], l[1])
        Final = (l[2], l[3])
        CorLinha = (l[4], l[5], l[6])
        Espessura = (l[7])
        pygame.draw.line(tela, CorLinha, Inicial, Final, Espessura)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
