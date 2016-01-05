# Versió del videojoc arcade PONG

#importació les llibreries necesaries de Python que necesitarem per a fer funcionar el joc
import simplegui
import random

# definició de les constants
AMPLADA = 600
ALÇADA = 400
DRETA = 1
ESQUERRA = 2
RADI_PILOTA = 20
PALA_AMPLADA = 8
PALA_ALÇADA = 80
MEITAT_PALA_AMPLADA = PALA_AMPLADA / 2
MEITAT_PALA_ALÇADA = PALA_ALÇADA / 2

#definició de les variables globals
posicio_pilota = [AMPLADA/ 2, ALÇADA / 2]
velocitat_pilota = [1,0]
posicio_pala1 = []
velocitat_pala1 = 0.0
posicio_pala2 = []
velocitat_pala2 = 0.0
punts1 = 0
punts2 = 0

#Aquesta funció es carrega al crear una nova partida i col·loca tots els objectes al seu lloc d'inci, reinicia els punts...
def nova_partida():
    global posicio_pala1, posicio_pala2, velocitat_pala1, velocitat_pala2
    global punts1, punts2
    #Posem les pales (1 i 2) al centre del de la seva zona i posem la velocitat inicial a 0
    posicio_pala1 = [MEITAT_PALA_AMPLADA, ALÇADA / 2]
    velocitat_pala1 = 0.0
    posicio_pala2 = [(AMPLADA - MEITAT_PALA_AMPLADA), ALÇADA / 2]
    velocitat_pala2 = 0.0
    #Reiniciem els marcadors a 0
    punts1 = 0
    punts2 = 0
    #utilitzem un valor aleatori entre 1(dreta) i 2(esquerra) per a que la pilota començi amb una direccio aleatoria
    direccio = random.randint(1,2)
    #Quan comença una nova partida es crida a la funció crear_pilota per a que aquesta aparegui a la pantalla
    crear_pilota(direccio)


#Aquesta funció s'encarrega de dibuixar al marc tots els objectes del videojoc
def dibuixar(canvas):
    global punts1, punts2, posicio_pala1, posicio_pala2, ball_pos, velocitat_pilota, velocitat_pala1, velocitat_pala2

    # dibuix de la línia del centre i de les línies laterals
    canvas.draw_line([AMPLADA / 2, 0],[AMPLADA / 2, ALÇADA], 1, "White")
    canvas.draw_line([PALA_AMPLADA, 0],[PALA_AMPLADA, ALÇADA], 1, "White")
    canvas.draw_line([AMPLADA - PALA_AMPLADA, 0],[AMPLADA - PALA_AMPLADA, ALÇADA], 1, "White")

    # dibuix dels marcadors
    canvas.draw_text(str(punts1),(450, 150), 50, "Green")
    canvas.draw_text(str(punts2),(150, 150), 50, "Green")

    # actualització de la posició de la pilota
    posicio_pilota[0] += velocitat_pilota[0] / 60
    posicio_pilota[1] += velocitat_pilota[1] / 60

    if posicio_pilota[1] <= RADI_PILOTA:
        velocitat_pilota[1] = - velocitat_pilota[1]
    elif posicio_pilota[1] >= (ALÇADA - RADI_PILOTA):
        velocitat_pilota[1] = - velocitat_pilota[1]

    # dibuixar pilota
    canvas.draw_circle(posicio_pilota, RADI_PILOTA, 5, 'Yellow' , 'Green')

    #actualitzar la velocitat de les pales (vertical) i mantenir les pales ditre dels límits de la pantalla
    posicio_pala1[1] += velocitat_pala1
    posicio_pala2[1] += velocitat_pala2

    if posicio_pala1[1] <= MEITAT_PALA_ALÇADA:
        velocitat_pala1 = 0
    elif posicio_pala1[1] >= ALÇADA - MEITAT_PALA_ALÇADA:
        velocitat_pala1 = 0

    if posicio_pala2[1] <= MEITAT_PALA_ALÇADA:
        velocitat_pala2 = 0
    elif posicio_pala2[1] >= ALÇADA - MEITAT_PALA_ALÇADA:
        velocitat_pala2 = 0

    # dibuixar les pales
    canvas.draw_polygon([(posicio_pala1[0] - MEITAT_PALA_AMPLADA, posicio_pala1[1] - MEITAT_PALA_ALÇADA), (posicio_pala1[0] + MEITAT_PALA_AMPLADA, posicio_pala1[1] - MEITAT_PALA_ALÇADA ), (posicio_pala1[0] + MEITAT_PALA_AMPLADA, posicio_pala1[1] + MEITAT_PALA_ALÇADA ), (posicio_pala1[0] - MEITAT_PALA_AMPLADA, posicio_pala1[1] + MEITAT_PALA_ALÇADA)], 1, 'Green', 'Yellow')
    canvas.draw_polygon([(posicio_pala2[0] - MEITAT_PALA_AMPLADA, posicio_pala2[1] - MEITAT_PALA_ALÇADA), (posicio_pala2[0] + MEITAT_PALA_AMPLADA, posicio_pala2[1] - MEITAT_PALA_ALÇADA ), (posicio_pala2[0] + MEITAT_PALA_AMPLADA, posicio_pala2[1] + MEITAT_PALA_ALÇADA ), (posicio_pala2[0] - MEITAT_PALA_AMPLADA, posicio_pala2[1] + MEITAT_PALA_ALÇADA)], 1, 'Green', 'Yellow')

    #determinar quan les pales i la pilota es toquen
    if posicio_pilota[0] >= (AMPLADA - (PALA_AMPLADA + RADI_PILOTA)):
        if posicio_pilota[1] >= (posicio_pala2[1] - MEITAT_PALA_ALÇADA) and posicio_pilota[1] <= (posicio_pala2[1] + MEITAT_PALA_ALÇADA):
            velocitat_pilota[0] = - velocitat_pilota[0] * 1.1
        else:
            crear_pilota(ESQUERRA)
            punts2 = punts2 + 1

    if posicio_pilota [0] <= (PALA_AMPLADA + RADI_PILOTA):
        if posicio_pilota[1] >= (posicio_pala1[1] - MEITAT_PALA_ALÇADA) and posicio_pilota[1] <= (posicio_pala1[1] + MEITAT_PALA_ALÇADA):
            velocitat_pilota[0] = - velocitat_pilota[0] * 1.1
        else:
            crear_pilota(DRETA)
            punts1 = punts1 + 1

#Aquesta funció crea una pilota amb una direcció i velocitat aleatores al centre de la pantalla
def crear_pilota(direccio):
    global posicio_pilota, velocitat_pilota
    #Col·loquem la pilota al centre de la pantalla
    posicio_pilota = [AMPLADA/ 2, ALÇADA / 2]

    if direccio == DRETA:
        velocitat_pilota = [random.randrange(120, 240),random.randrange(-60, 180)]
    else:
        velocitat_pilota = [-random.randrange(120, 240),random.randrange(-60, 180)]

# Definició dels esdeveniments
#Aquesta funció s'encarrega de detectar quan es prem una tecla i de moure les pales
def tecla_premuda(tecla):
    global velocitat_pala1, velocitat_pala2
    if tecla == 87:
        velocitat_pala1 = -4
    elif tecla == 83:
        velocitat_pala1 = 4
    elif tecla == 38:
        velocitat_pala2 = -4
    elif tecla == 40:
        velocitat_pala2 = 4

#Aquesta funció detecta quan es deixa de premer la tecla i atura les pales
def tecla_deixada(tecla):
    global velocitat_pala1, velocitat_pala2
    if tecla == 87:
        velocitat_pala1 = 0
    elif tecla == 83:
        velocitat_pala1 = 0
    elif tecla == 38:
        velocitat_pala2 = 0
    elif tecla == 40:
        velocitat_pala2 = 0

# crear el marc del joc
frame = simplegui.create_frame("Pong", AMPLADA, ALÇADA)
frame.set_draw_handler(dibuixar)
frame.set_keydown_handler(tecla_premuda)
frame.set_keyup_handler(tecla_deixada)
frame.add_button("Reiniciar", nova_partida)

# iniciar la partida i el marc
nova_partida()
frame.start()
