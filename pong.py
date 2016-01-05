#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Versió del videojoc arcade PONG

# importa les llibreries necesaries de Python necessàries pel joc
import pygame
from pygame.locals import *
import time
import math
import random

# defineix les constants
AMPLADA = 600
ALTURA = 400
DRETA = 1
ESQUERRA = 2
PILOTA_RADI = 20
PALA_AMPLADA = 8
PALA_ALTURA = 80
MEITAT_PALA_AMPLADA = PALA_AMPLADA / 2
MEITAT_PALA_ALTURA = PALA_ALTURA / 2

# defineix les variables globals
posicio_pilota = [AMPLADA/ 2, ALTURA / 2]
velocitat_pilota = [1.0,0.0]
posicio_pala1 = []
velocitat_pala1 = 0.0
posicio_pala2 = []
velocitat_pala2 = 0.0
punts1 = 0
punts2 = 0
verd = pygame.Color(0, 255, 0)
groc = pygame.Color(255, 255, 0)
blanc = pygame.Color(255, 255, 255)
negre = pygame.Color(0, 0, 0)

# Crea una nova partida i col·loca tots els objectes al seu lloc d'inci, reinicia els punts...
def nova_partida():
    global posicio_pala1, posicio_pala2, velocitat_pala1, velocitat_pala2
    global punts1, punts2

    # Posa les pales (1 i 2) al centre del de la seva zona i posem la velocitat inicial a 0
    posicio_pala1 = [MEITAT_PALA_AMPLADA, ALTURA / 2]
    velocitat_pala1 = 0.0
    posicio_pala2 = [(AMPLADA - MEITAT_PALA_AMPLADA), ALTURA / 2]
    velocitat_pala2 = 0.0

    # Reinicia els marcadors a 0
    punts1 = 0
    punts2 = 0

    # Utilitza un valor aleatori entre 1(dreta) i 2(esquerra) per a que la pilota començi amb una direccio aleatoria
    direccio = random.randint(1,2)
    crear_pilota(direccio)

# dibuixa al marc tots els objectes del videojoc
def dibuixar(canvas):
    global punts1, punts2, posicio_pala1, posicio_pala2, ball_pos, velocitat_pilota, velocitat_pala1, velocitat_pala2

    # Neteja el canvas omplint-lo de color negre
    canvas.fill(negre)

    # dibuixa la línia del centre i les línies laterals
    pygame.draw.line(canvas, blanc, [AMPLADA / 2, 0],[AMPLADA / 2, ALTURA], 1,)
    pygame.draw.line(canvas, blanc, [PALA_AMPLADA, 0],[PALA_AMPLADA, ALTURA], 1,)
    pygame.draw.line(canvas, blanc, [AMPLADA - PALA_AMPLADA, 0],[AMPLADA - PALA_AMPLADA, ALTURA], 1,)

    # dibuixa els marcadors
    text_draw = fontJoc.render(str(punts1), True, verd)
    canvas.blit(text_draw, (450, 150))
    text_draw = fontJoc.render(str(punts2), True, verd)
    canvas.blit(text_draw, (150, 150))

    # actualitza la posició de la pilota
    if (posicio_pilota[1] <= PILOTA_RADI): #Rebot cap amunt
        velocitat_pilota[1] = abs(velocitat_pilota[1])
    elif (posicio_pilota[1] >= (ALTURA - PILOTA_RADI)): #Rebot cap avall
        velocitat_pilota[1] = - abs(velocitat_pilota[1])
    posicio_pilota[0] += velocitat_pilota[0] / 60.0
    posicio_pilota[1] += velocitat_pilota[1] / 60.0

    # dibuixa la pilota
    pygame.draw.circle(canvas, verd, [int(posicio_pilota[0]), int(posicio_pilota[1])], PILOTA_RADI)
    pygame.draw.circle(canvas, groc, [int(posicio_pilota[0]), int(posicio_pilota[1])], (PILOTA_RADI - 5))

    # actualitza la velocitat de les pales (vertical) i manté les pales ditre dels límits de la pantalla
    if (posicio_pala1[1] <= MEITAT_PALA_ALTURA and velocitat_pala1 < 0):
        velocitat_pala1 = 0
    elif (posicio_pala1[1] >= ALTURA - MEITAT_PALA_ALTURA and velocitat_pala1 > 0):
        velocitat_pala1 = 0
    posicio_pala1[1] += velocitat_pala1

    if (posicio_pala2[1] <= MEITAT_PALA_ALTURA and velocitat_pala2 < 0):
        velocitat_pala2 = 0
    elif (posicio_pala2[1] >= ALTURA - MEITAT_PALA_ALTURA and velocitat_pala2 > 0):
        velocitat_pala2 = 0
    posicio_pala2[1] += velocitat_pala2

    # dibuixa les pales
    pygame.draw.polygon(canvas, verd, [(posicio_pala1[0] - MEITAT_PALA_AMPLADA, posicio_pala1[1] - MEITAT_PALA_ALTURA), (posicio_pala1[0] + MEITAT_PALA_AMPLADA, posicio_pala1[1] - MEITAT_PALA_ALTURA ), (posicio_pala1[0] + MEITAT_PALA_AMPLADA, posicio_pala1[1] + MEITAT_PALA_ALTURA ), (posicio_pala1[0] - MEITAT_PALA_AMPLADA, posicio_pala1[1] + MEITAT_PALA_ALTURA)])
    pygame.draw.polygon(canvas, groc, [(posicio_pala1[0] - MEITAT_PALA_AMPLADA, posicio_pala1[1] - MEITAT_PALA_ALTURA), (posicio_pala1[0] + MEITAT_PALA_AMPLADA, posicio_pala1[1] - MEITAT_PALA_ALTURA ), (posicio_pala1[0] + MEITAT_PALA_AMPLADA, posicio_pala1[1] + MEITAT_PALA_ALTURA ), (posicio_pala1[0] - MEITAT_PALA_AMPLADA, posicio_pala1[1] + MEITAT_PALA_ALTURA)], 1)
    pygame.draw.polygon(canvas, verd, [(posicio_pala2[0] - MEITAT_PALA_AMPLADA, posicio_pala2[1] - MEITAT_PALA_ALTURA), (posicio_pala2[0] + MEITAT_PALA_AMPLADA, posicio_pala2[1] - MEITAT_PALA_ALTURA ), (posicio_pala2[0] + MEITAT_PALA_AMPLADA, posicio_pala2[1] + MEITAT_PALA_ALTURA ), (posicio_pala2[0] - MEITAT_PALA_AMPLADA, posicio_pala2[1] + MEITAT_PALA_ALTURA)])
    pygame.draw.polygon(canvas, groc, [(posicio_pala2[0] - MEITAT_PALA_AMPLADA, posicio_pala2[1] - MEITAT_PALA_ALTURA), (posicio_pala2[0] + MEITAT_PALA_AMPLADA, posicio_pala2[1] - MEITAT_PALA_ALTURA ), (posicio_pala2[0] + MEITAT_PALA_AMPLADA, posicio_pala2[1] + MEITAT_PALA_ALTURA ), (posicio_pala2[0] - MEITAT_PALA_AMPLADA, posicio_pala2[1] + MEITAT_PALA_ALTURA)], 1)

    # determina quan les pales i la pilota es toquen
    if posicio_pilota[0] >= (AMPLADA - (PALA_AMPLADA + PILOTA_RADI)):
        if posicio_pilota[1] >= (posicio_pala2[1] - MEITAT_PALA_ALTURA) and posicio_pilota[1] <= (posicio_pala2[1] + MEITAT_PALA_ALTURA):
            velocitat_pilota[0] = - velocitat_pilota[0] * 1.1
        else:
            crear_pilota(ESQUERRA)
            punts2 = punts2 + 1

    if posicio_pilota [0] <= (PALA_AMPLADA + PILOTA_RADI):
        if posicio_pilota[1] >= (posicio_pala1[1] - MEITAT_PALA_ALTURA) and posicio_pilota[1] <= (posicio_pala1[1] + MEITAT_PALA_ALTURA):
            velocitat_pilota[0] = - velocitat_pilota[0] * 1.1
        else:
            crear_pilota(DRETA)
            punts1 = punts1 + 1

# crea una pilota amb la direcció indicada al centre de la pantalla
def crear_pilota(direccio):
    global posicio_pilota, velocitat_pilota

    # Col·loca la pilota al centre de la pantalla
    posicio_pilota = [AMPLADA/ 2, ALTURA / 2]

    # Assigna velocitat aleatòria en funció de la direcció
    if direccio == DRETA:
        velocitat_pilota = [random.randrange(120, 240),random.randrange(-60, 180)]
    else:
        velocitat_pilota = [-random.randrange(120, 240),random.randrange(-60, 180)]

# Callbacks pels esdeveniments
# Es prem una tecla: Escull l'acció segons la tecla
def tecla_premuda(tecla):
    global jugant
    global velocitat_pala1, velocitat_pala2
    if tecla == 119:
        velocitat_pala1 = -4
    elif tecla == 115:
        velocitat_pala1 = 4
    elif tecla == 273:#38:
        velocitat_pala2 = -4
    elif tecla == 274:
        velocitat_pala2 = 4
    elif tecla == 114:
        nova_partida()
    elif tecla == 27:
        jugant = False

# Es deixa de premer una tecla: atura les pales
def tecla_deixada(tecla):
    global velocitat_pala1, velocitat_pala2
    if tecla == 119:
        velocitat_pala1 = 0
    elif tecla == 115:
        velocitat_pala1 = 0
    elif tecla == 273:#38:
        velocitat_pala2 = 0
    elif tecla == 274:
        velocitat_pala2 = 0

##################################################
##    Programa Principal                        ##
##################################################

# Crea el marc del joc i inicialitzar la llibreria
canvas = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Pong")
pygame.init()

# Inicia el temporitzador per gestionar els FPS del joc
temporitzador = pygame.time.Clock()


# Posa una pantalla amb info sobre el joc
canvas.fill(negre)
fontJoc = pygame.font.Font(pygame.font.match_font('comic sans ms'), 20)
s = "Jugador 1: w --> Amunt    s --> Avall "
text_draw = fontJoc.render(s, True, blanc)
canvas.blit(text_draw, (60, 60))
s = "Jugador 2: Cursor Up --> Amunt    Cursor Down --> Avall "
text_draw = fontJoc.render(s, True, blanc)
canvas.blit(text_draw, (60, 90))
s = "R --> Reiniciar    Escape --> Sortir "
text_draw = fontJoc.render(s, True, blanc)
canvas.blit(text_draw, (60, 140))
s.encode('utf-8')
s = u"Prem una tecla per comen\u00E7ar!"
text_draw = fontJoc.render(s, True, blanc)
canvas.blit(text_draw, (60, 180))
pygame.display.update()

# Bucle fins que es premi una tecla
mostrant = True
while mostrant:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            mostrant = False
    temporitzador.tick(60)

# Neteja el canvas i canvia el tipus de lletra pel joc
canvas.fill(negre)
fontJoc = pygame.font.Font(pygame.font.match_font('comic sans ms'), 50)

# Inicia la partida i el dibuixa el canvas
nova_partida()
dibuixar(canvas)
pygame.display.update()

# Bucle infinit pel joc fins que es tanca la finestra o es prem escape
jugant = True
while jugant:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Tancar la finestra
            jugant = False
        elif event.type == pygame.KEYDOWN:
            tecla_premuda(event.key)
        elif event.type == pygame.KEYUP:
            tecla_deixada(event.key)

    dibuixar(canvas)
    pygame.display.update()

    # Temporitzador: Fa que el joc vagi a 60 FPS
    temporitzador.tick(60)

# Fí del bucle: surt del joc
pygame.quit ()
