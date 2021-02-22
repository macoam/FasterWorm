from OpenGL.GL import *
from glew_wish import *
import glfw
import random
from math import *
import sys

#Posiciones
posX_gusano = 0.0
posY_gusano = 0.0

deltaPosX = -0.1
deltaPosY = 0.0

posX_alimento1 = random.uniform(-0.85,0.85)
posY_alimento1 = random.uniform(-0.85,0.85)
posX_alimento2 = 0.0
posY_alimento2 = 0.0
posX_alimento3 = 0.0
posY_alimento3 = 0.0
posX_alimento4 = 0.0
posY_alimento4 = 0.0
posX_alimento5 = 0.0
posY_alimento5 = 0.0
posX_alimento6 = 0.0
posY_alimento6 = 0.0
posX_alimento7 = 0.0
posY_alimento7 = 0.0
posX_alimento8 = 0.0
posY_alimento8 = 0.0
posX_alimento9 = 0.0
posY_alimento9 = 0.0
posX_alimento10 = 0.0
posY_alimento10 = 0.0

posX_gusanito1 = -0.7
posY_gusanito1 = 0.6
posX_gusanito2 = 0.1
posY_gusanito2 = -0.1
posX_gusanito3 = 0.6
posY_gusanito3 = -0.7
posX_gusanito4 = -0.7
posY_gusanito4 = -0.6
posX_gusanito5 = 0.7
posY_gusanito5 = 0.6

#Condiciones
condicionMovXP = False
condicionMovXN = False
condicionMovYP = False
condicionMovYN = False

#Movimiento
tiempo = 0.0
tiempoAnterior = 0.0
velocidad = 0.3
velocidadGusanitos = velocidad * 0.5
#Colisiones
colisionAlimento = 0
colisionPerder = False

#score
score = -1

def checar_colisiones():
    global colisionPerder
    global colisionAlimento

    global posX_alimento1
    global posY_alimento1
    global posX_alimento2 
    global posY_alimento2 
    global posX_alimento3
    global posY_alimento3
    global posX_alimento4
    global posY_alimento4
    global posX_alimento5
    global posY_alimento5
    global posX_alimento6 
    global posY_alimento6 
    global posX_alimento7
    global posY_alimento7
    global posX_alimento8
    global posY_alimento8
    global posX_alimento9
    global posY_alimento9
    global posX_alimento10
    global posY_alimento10

    global posX_gusanito1
    global posX_gusanito2
    global posX_gusanito3
    global posX_gusanito4
    global posX_gusanito5
    global posY_gusanito4
    global posY_gusanito5

    global velocidad
    global score

    if posX_gusano + 0.05 > 1.0:
        colisionPerder = True
        posX_alimento3 = random.uniform(-0.85,0.85)
        posY_alimento3 = random.uniform(-0.85,0.85)
    elif posX_gusano - 0.05 < -1.0:
        colisionPerder = True
        posX_alimento3 = random.uniform(-0.85,0.85)
        posY_alimento3 = random.uniform(-0.85,0.85)
    elif posY_gusano + 0.05 > 1.0:
        colisionPerder = True
        posX_alimento3 = random.uniform(-0.85,0.85)
        posY_alimento3 = random.uniform(-0.85,0.85)
    elif posY_gusano - 0.05 < -1.0:
        colisionPerder = True
        posX_alimento3 = random.uniform(-0.85,0.85)
        posY_alimento3 = random.uniform(-0.85,0.85)
    else:
        colisionPerder = False

    if posX_gusanito1 + 0.01 > 1.0:
        posX_gusanito1 = -1.05
    if posX_gusanito2 + 0.01 < -1.0:
        posX_gusanito2 = 1.05
    if posX_gusanito3 + 0.01 > 1.0:
        posX_gusanito3 = -1.05

    if posY_gusanito4 + 0.01 > 1.0:
        posY_gusanito4 = -1.05
        posX_gusanito4 = -0.8
    if posY_gusanito5 - 0.01 < -1.0:
        posY_gusanito5 = 1.05
        posX_gusanito5 = 0.7


    if posX_gusano + 0.05 > posX_alimento1 - 0.05 and posX_gusano - 0.05 < posX_alimento1 + 0.05 and posY_gusano + 0.05 > posY_alimento1 - 0.05 and posY_gusano - 0.05 < posY_alimento1 + 0.05:
        colisionAlimento = 1
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = random.uniform(-0.85,0.85)
        posY_alimento2 = random.uniform(-0.85,0.85)
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento2 - 0.05 and posX_gusano - 0.05 < posX_alimento2 + 0.05 and posY_gusano + 0.05 > posY_alimento2 - 0.05 and posY_gusano - 0.05 < posY_alimento2 + 0.05:
        colisionAlimento = 2
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = random.uniform(-0.85,0.85)
        posY_alimento3 = random.uniform(-0.85,0.85)
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento3 - 0.05 and posX_gusano - 0.05 < posX_alimento3 + 0.05 and posY_gusano + 0.05 > posY_alimento3 - 0.05 and posY_gusano - 0.05 < posY_alimento3 + 0.05:
        colisionAlimento = 3
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = random.uniform(-0.85,0.85)
        posY_alimento4 = random.uniform(-0.85,0.85)
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento4 - 0.05 and posX_gusano - 0.05 < posX_alimento4 + 0.05 and posY_gusano + 0.05 > posY_alimento4 - 0.05 and posY_gusano - 0.05 < posY_alimento4 + 0.05:
        colisionAlimento = 4
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = random.uniform(-0.85,0.85)
        posY_alimento5 = random.uniform(-0.85,0.85)
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento5 - 0.05 and posX_gusano - 0.05 < posX_alimento5 + 0.05 and posY_gusano + 0.05 > posY_alimento5 - 0.05 and posY_gusano - 0.05 < posY_alimento5 + 0.05:
        colisionAlimento = 5
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = random.uniform(-0.85,0.85)
        posY_alimento6 = random.uniform(-0.85,0.85)
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento6 - 0.05 and posX_gusano - 0.05 < posX_alimento6 + 0.05 and posY_gusano + 0.05 > posY_alimento6 - 0.05 and posY_gusano - 0.05 < posY_alimento6 + 0.05:
        colisionAlimento = 6
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = random.uniform(-0.85,0.85)
        posY_alimento7 = random.uniform(-0.85,0.85)
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento7 - 0.05 and posX_gusano - 0.05 < posX_alimento7 + 0.05 and posY_gusano + 0.05 > posY_alimento7 - 0.05 and posY_gusano - 0.05 < posY_alimento7 + 0.05:
        colisionAlimento = 7
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = random.uniform(-0.85,0.85)
        posY_alimento8 = random.uniform(-0.85,0.85)
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento8 - 0.05 and posX_gusano - 0.05 < posX_alimento8 + 0.05 and posY_gusano + 0.05 > posY_alimento8 - 0.05 and posY_gusano - 0.05 < posY_alimento8 + 0.05:
        colisionAlimento = 8
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = random.uniform(-0.85,0.85)
        posY_alimento9 = random.uniform(-0.85,0.85)
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento9 - 0.05 and posX_gusano - 0.05 < posX_alimento9 + 0.05 and posY_gusano + 0.05 > posY_alimento9 - 0.05 and posY_gusano - 0.05 < posY_alimento9 + 0.05:
        colisionAlimento = 9
        posX_alimento1 = -1.5
        posY_alimento1 = -1.5
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = random.uniform(-0.85,0.85)
        posY_alimento10 = random.uniform(-0.85,0.85)
        velocidad += 0.05
        score += 1

    elif posX_gusano + 0.05 > posX_alimento10 - 0.05 and posX_gusano - 0.05 < posX_alimento10 + 0.05 and posY_gusano + 0.05 > posY_alimento10 - 0.05 and posY_gusano - 0.05 < posY_alimento10 + 0.05:
        colisionAlimento = 0
        posX_alimento1 = random.uniform(-0.85,0.85)
        posY_alimento1 = random.uniform(-0.85,0.85)
        posX_alimento2 = -1.5
        posY_alimento2 = -1.5
        posX_alimento3 = -1.5
        posY_alimento3 = -1.5
        posX_alimento4 = -1.5
        posY_alimento4 = -1.5
        posX_alimento5 = -1.5
        posY_alimento5 = -1.5
        posX_alimento6 = -1.5
        posY_alimento6 = -1.5
        posX_alimento7 = -1.5
        posY_alimento7 = -1.5
        posX_alimento8 = -1.5
        posY_alimento8 = -1.5
        posX_alimento9 = -1.5
        posY_alimento9 = -1.5
        posX_alimento10 = -1.5
        posY_alimento10 = -1.5
        velocidad += 0.05
        score += 1
    
def actualizar(window):
    global tiempo
    global tiempoAnterior
    global velocidad
    global velocidadGusanitos
    global posX_gusano
    global posY_gusano
    global posX_gusanito1
    global posY_gusanito1
    global posX_gusanito2
    global posY_gusanito2
    global posX_gusanito3
    global posY_gusanito3
    global posX_gusanito4
    global posY_gusanito4
    global posX_gusanito5
    global posY_gusanito5
    global deltaPosX
    global deltaPosY
    global condicionMovXP
    global condicionMovXN
    global condicionMovYP
    global condicionMovYN

    tiempo = glfw.get_time()
    deltatime = tiempo - tiempoAnterior
    movimiento = velocidad * deltatime
    movGusanitos = velocidadGusanitos * deltatime

    posX_gusanito1 = posX_gusanito1 + movGusanitos
    posX_gusanito2 = posX_gusanito2 - movGusanitos
    posX_gusanito3 = posX_gusanito3 + movGusanitos

    posX_gusanito4 = posX_gusanito4 + movGusanitos
    posY_gusanito4 = posY_gusanito4 + movGusanitos
    posX_gusanito5 = posX_gusanito5 - movGusanitos
    posY_gusanito5 = posY_gusanito5 - movGusanitos

    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

    if estado_tecla_derecha == glfw.PRESS:
        condicionMovXP = True
        condicionMovXN = False
        condicionMovYP = False
        condicionMovYN = False
    if estado_tecla_izquierda == glfw.PRESS:
        condicionMovXN = True
        condicionMovXP = False
        condicionMovYP = False
        condicionMovYN = False
    if estado_tecla_arriba== glfw.PRESS:
        condicionMovYP = True
        condicionMovXP = False
        condicionMovXN = False
        condicionMovYN = False
    if estado_tecla_abajo== glfw.PRESS:
        condicionMovYN = True
        condicionMovXP = False
        condicionMovXN = False
        condicionMovYP = False

    if condicionMovXP == True:
        posX_gusano = posX_gusano + movimiento
        deltaPosX = -0.1
        deltaPosY = 0.0
    if condicionMovXN == True:
        posX_gusano = posX_gusano - movimiento
        deltaPosX = 0.1
        deltaPosY = 0.0
    if condicionMovYP == True:
        posY_gusano = posY_gusano + movimiento
        deltaPosX = 0.0
        deltaPosY = -0.1
    if condicionMovYN == True:
        posY_gusano = posY_gusano - movimiento
        deltaPosX = 0.0
        deltaPosY = 0.1

    tiempoAnterior = tiempo
    checar_colisiones()

def dibujarEspinas():
    glPushMatrix()
    glScalef(1.0,1.0,1.0)
    glColor3f(0.2,0.6,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.1,0.9,0.0)
    glVertex3f(-0.95,0.85,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-0.95,0.75,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-0.95,0.65,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-0.95,0.55,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-0.95,0.45,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-0.95,0.35,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-0.95,0.25,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-0.95,0.15,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-0.95,0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glVertex3f(-1.1,-0.9,0.0)
    glVertex3f(-0.95,-0.85,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-0.95,-0.75,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-0.95,-0.65,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-0.95,-0.55,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-0.95,-0.45,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-0.95,-0.35,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-0.95,-0.25,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-0.95,-0.15,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-0.95,-0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glScalef(1.0,1.0,1.0)
    glRotatef(90,0,0,1)
    glColor3f(0.2,0.6,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.1,0.9,0.0)
    glVertex3f(-0.95,0.85,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-0.95,0.75,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-0.95,0.65,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-0.95,0.55,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-0.95,0.45,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-0.95,0.35,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-0.95,0.25,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-0.95,0.15,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-0.95,0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glVertex3f(-1.1,-0.9,0.0)
    glVertex3f(-0.95,-0.85,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-0.95,-0.75,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-0.95,-0.65,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-0.95,-0.55,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-0.95,-0.45,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-0.95,-0.35,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-0.95,-0.25,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-0.95,-0.15,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-0.95,-0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glScalef(1.0,1.0,1.0)
    glRotatef(180,0,0,1)
    glColor3f(0.2,0.6,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.1,0.9,0.0)
    glVertex3f(-0.95,0.85,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-0.95,0.75,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-0.95,0.65,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-0.95,0.55,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-0.95,0.45,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-0.95,0.35,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-0.95,0.25,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-0.95,0.15,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-0.95,0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glVertex3f(-1.1,-0.9,0.0)
    glVertex3f(-0.95,-0.85,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-0.95,-0.75,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-0.95,-0.65,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-0.95,-0.55,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-0.95,-0.45,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-0.95,-0.35,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-0.95,-0.25,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-0.95,-0.15,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-0.95,-0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glScalef(1.0,1.0,1.0)
    glRotatef(-90,0,0,1)
    glColor3f(0.2,0.6,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.1,0.9,0.0)
    glVertex3f(-0.95,0.85,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-1.1,0.8,0.0)
    glVertex3f(-0.95,0.75,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-1.1,0.7,0.0)
    glVertex3f(-0.95,0.65,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-1.1,0.6,0.0)
    glVertex3f(-0.95,0.55,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-1.1,0.5,0.0)
    glVertex3f(-0.95,0.45,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-1.1,0.4,0.0)
    glVertex3f(-0.95,0.35,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-1.1,0.3,0.0)
    glVertex3f(-0.95,0.25,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-1.1,0.2,0.0)
    glVertex3f(-0.95,0.15,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-1.1,0.1,0.0)
    glVertex3f(-0.95,0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glVertex3f(-1.1,-0.9,0.0)
    glVertex3f(-0.95,-0.85,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-1.1,-0.8,0.0)
    glVertex3f(-0.95,-0.75,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-1.1,-0.7,0.0)
    glVertex3f(-0.95,-0.65,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-1.1,-0.6,0.0)
    glVertex3f(-0.95,-0.55,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-1.1,-0.5,0.0)
    glVertex3f(-0.95,-0.45,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-1.1,-0.4,0.0)
    glVertex3f(-0.95,-0.35,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-1.1,-0.3,0.0)
    glVertex3f(-0.95,-0.25,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-1.1,-0.2,0.0)
    glVertex3f(-0.95,-0.15,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-1.1,-0.1,0.0)
    glVertex3f(-0.95,-0.05,0.0)
    glVertex3f(-1.1,0.0,0.0)
    glEnd()
    glPopMatrix()

def dibujarFondo():
    glPushMatrix()
    glTranslatef(-0.55,0.55,0.0)
    glScalef(0.1,0.1,0.1)
    glColor3f(0.25,0.15,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, -1.0, 0.0)
    glVertex3f(-0.5, -1.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.45,0.65,0.0)
    glScalef(0.05,0.05,0.05)
    glColor3f(0.25,0.15,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.2, 0.9, 0.0)
    glVertex3f(0.8, 0.1, 0.0)
    glVertex3f(0.45, -1.0, 0.0)
    glVertex3f(-0.55, -1.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.8, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.3,0.1,0.0)
    glScalef(0.075,0.075,0.075)
    glColor3f(0.25,0.15,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.15, 0.8, 0.0)
    glVertex3f(0.7, 0.4, 0.0)
    glVertex3f(0.9, 0.0, 0.0)
    glVertex3f(0.25, -0.5, 0.0)
    glVertex3f(0.0, -0.9, 0.0)
    glVertex3f(-0.4, -0.7, 0.0)
    glVertex3f(-0.5, 0.4, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.1,-0.85,0.0)
    glScalef(0.1,0.1,0.1)
    glRotatef(45,0,0,1)
    glColor3f(0.25,0.15,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, -1.0, 0.0)
    glVertex3f(-0.5, -1.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.25,0.05,0.0)
    glScalef(0.05,0.05,0.05)
    glRotatef(15,0,0,1)
    glColor3f(0.25,0.15,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.2, 0.9, 0.0)
    glVertex3f(0.8, 0.1, 0.0)
    glVertex3f(0.45, -1.0, 0.0)
    glVertex3f(-0.55, -1.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.8, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.75,-0.35,0.0)
    glScalef(0.075,0.075,0.075)
    glRotatef(85,0,0,1)
    glColor3f(0.25,0.15,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.15, 0.8, 0.0)
    glVertex3f(0.7, 0.4, 0.0)
    glVertex3f(0.9, 0.0, 0.0)
    glVertex3f(0.25, -0.5, 0.0)
    glVertex3f(0.0, -0.9, 0.0)
    glVertex3f(-0.4, -0.7, 0.0)
    glVertex3f(-0.5, 0.4, 0.0)
    glEnd()
    glPopMatrix()



    glPushMatrix()
    glTranslatef(0.35,-0.75,0.0)
    glScalef(0.08,0.08,0.08)
    glColor3f(0.3,0.3,0.3)
    glRotatef(30,0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.35,-0.45,0.0)
    glScalef(0.05,0.05,0.1)
    glColor3f(0.3,0.3,0.3)
    glRotatef(30,0,0,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*1.5,sin(angulo)*0.8,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.35,0.75,0.0)
    glScalef(0.08,0.08,0.08)
    glColor3f(0.3,0.3,0.3)
    glRotatef(-70,0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.65,0.85,0.0)
    glScalef(0.05,0.05,0.1)
    glColor3f(0.3,0.3,0.3)
    glRotatef(-20,0,0,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*1.5,sin(angulo)*0.8,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.88,0.05,0.0)
    glScalef(0.08,0.08,0.08)
    glColor3f(0.3,0.3,0.3)
    glRotatef(-10,0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.65,0.85,0.0)
    glScalef(0.05,0.05,0.1)
    glColor3f(0.3,0.3,0.3)
    glRotatef(-20,0,0,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*1.5,sin(angulo)*0.8,0.0)
    glEnd()
    glPopMatrix()

def dibujarAlimentos():
    global posX_alimento1
    global posY_alimento1
    global posX_alimento2
    global posY_alimento2
    global posX_alimento3
    global posY_alimento3
    global posX_alimento4
    global posY_alimento4
    global posX_alimento5
    global posY_alimento5
    global posX_alimento6 
    global posY_alimento6 
    global posX_alimento7
    global posY_alimento7
    global posX_alimento8
    global posY_alimento8
    global posX_alimento9
    global posY_alimento9
    global posX_alimento10
    global posY_alimento10

    #naranja
    glPushMatrix()
    glTranslatef(posX_alimento1, posY_alimento1, 0.0)
    if colisionAlimento == 0:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.9,0.6,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo),0.0)
    glEnd()
    glColor3f(0.7,0.7,0.5)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.15+0.55,sin(angulo)*0.15+0.55,0.0)
    glEnd()
    glPopMatrix()

    #limon
    glPushMatrix()
    glTranslatef(posX_alimento2, posY_alimento2, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.8,0.9,0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.85,sin(angulo)*0.75,0.0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.0,0.0,0.0)
    glVertex3f(-0.7,0.2,0.0)
    glVertex3f(-0.7,-0.2,0.0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(1.0,0.0,0.0)
    glVertex3f(0.7,0.2,0.0)
    glVertex3f(0.7,-0.2,0.0)
    glEnd()
    glPopMatrix()

    #cereza
    glPushMatrix()
    glTranslatef(posX_alimento3, posY_alimento3, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.5,0.1,0.2)
    glBegin(GL_QUADS)
    glVertex3f(-0.55,-0.5,0.0)
    glVertex3f(-0.45,-0.5,0.0)
    glVertex3f(0.45,0.8,0.0)
    glVertex3f(0.55,0.8,0.0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f(0.45,0.8,0.0)
    glVertex3f(0.55,0.8,0.0)
    glVertex3f(0.45,-0.8,0.0)
    glVertex3f(0.55,-0.8,0.0)
    glEnd()
    glColor3f(0.7,0.1,0.2)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.35-0.5,sin(angulo)*0.35-0.5,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.35+0.5,sin(angulo)*0.35-0.5,0.0)
    glEnd()
    glPopMatrix()

    #pepino
    glPushMatrix()
    glTranslatef(posX_alimento4, posY_alimento4, 0.0)
    glRotate(45,0,0,1)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.1,0.4,0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.35,sin(angulo)*1.3,0.0)
    glEnd()
    glPopMatrix()

    #manzana
    glPushMatrix()
    glTranslatef(posX_alimento5, posY_alimento5, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
         glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.3,0.1,0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.0,1.1,0.0)
    glVertex3f(0.1,1.1,0.0)
    glVertex3f(-0.35,-0.5,0.0)
    glVertex3f(-0.25,-0.5,0.0)
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.7-0.2,sin(angulo)*0.9-0.1,0.0)
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.7+0.2,sin(angulo)*0.9-0.1,0.0)
    glEnd()
    glPopMatrix()

    #pera
    glPushMatrix()
    glTranslatef(posX_alimento6, posY_alimento6, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.3,0.1,0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.0,1.1,0.0)
    glVertex3f(0.1,1.1,0.0)
    glVertex3f(-0.35,-0.5,0.0)
    glVertex3f(-0.25,-0.5,0.0)
    glEnd()
    glColor3f(0.6,0.9,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.5,sin(angulo)*0.6+0.1,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.6,sin(angulo)*0.6-0.3,0.0)
    glEnd()
    glPopMatrix()

    #zanahoria
    glPushMatrix()
    glTranslatef(posX_alimento7, posY_alimento7, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.9,0.6,0.0)
    glBegin(GL_POLYGON)
    for x in range(181):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.7,sin(angulo)*0.7-1.0,0.0)
    glEnd()
    glColor3f(0.5,0.8,0.0)
    glBegin(GL_QUADS)
    glVertex3f(-0.3,1.0,0.0)
    glVertex3f(-0.4,0.4,0.0)
    glVertex3f(0.0,-0.3,0.0)
    glVertex3f(0.0,0.4,0.0)
    glEnd()
    glColor3f(0.3,0.5,0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.2,1.0,0.0)
    glVertex3f(-0.1,0.4,0.0)
    glVertex3f(0.0,-0.3,0.0)
    glVertex3f(0.3,0.4,0.0)
    glEnd()
    glPopMatrix()

    #Flor
    glPushMatrix()
    glTranslatef(posX_alimento8, posY_alimento8, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.2,0.4,0.0)
    glVertex3f(0.15,0.4,0)
    glVertex3f(-0.15,0.4,0)
    glVertex3f(0.0,-1.0,0)
    glEnd()
    glColor3f(0.9,0.2,0.1)
    glBegin(GL_POLYGON)
    glVertex3f(0.0,-0.3,0)
    glVertex3f(0.3,0.1,0)
    glVertex3f(0.15,0.4,0)
    glVertex3f(-0.15,0.4,0)
    glVertex3f(-0.3,0.1,0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(0.3,0.1,0)
    glVertex3f(0.15,0.4,0)
    glVertex3f(0.8,0.6,0)
    glVertex3f(0.15,0.4,0)
    glVertex3f(-0.15,0.4,0)
    glVertex3f(0.0,1.0,0)
    glVertex3f(-0.3,0.1,0)
    glVertex3f(-0.15,0.4,0)
    glVertex3f(-0.8,0.6,0)
    glEnd()
    glPopMatrix()

    #Rabano
    glPushMatrix()
    glTranslatef(posX_alimento9, posY_alimento9, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.05,0.05,0.05)
    if colisionAlimento == 9:
        glScalef(0.0,0.0,0.0)
    glColor3f(0.8,0.0,0.3)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.6,sin(angulo)*0.6-0.2,0.0)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.6,-0.2,0.0)
    glVertex3f(0.0,-1.0,0.0)
    glVertex3f(0.6,-0.2,0.0)
    glEnd()
    glColor3f(0.5,0.8,0.0)
    glBegin(GL_QUADS)
    glVertex3f(-0.3,1.0,0.0)
    glVertex3f(-0.4,0.7,0.0)
    glVertex3f(0.0,0.4,0.0)
    glVertex3f(0.0,0.7,0.0)
    glEnd()
    glColor3f(0.3,0.5,0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.2,1.0,0.0)
    glVertex3f(-0.1,0.7,0.0)
    glVertex3f(0.0,0.4,0.0)
    glVertex3f(0.3,0.7,0.0)
    glEnd()
    glPopMatrix()

    #uvas
    glPushMatrix()
    glTranslatef(posX_alimento10, posY_alimento10, 0.0)
    if colisionAlimento == 0:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 1:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 2:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 3:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 4:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 5:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 6:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 7:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 8:
        glScalef(0.0,0.0,0.0)
    if colisionAlimento == 9:
        glScalef(0.05,0.05,0.05)
    glColor3f(0.3,0.1,0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.0,1.0,0)
    glVertex3f(0.2,1.0,0)
    glVertex3f(0.1,0.2,0)
    glVertex3f(0.0,0.2,0)
    glEnd()
    glColor3f(0.6,0.2,0.6)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.25,sin(angulo)*0.25-0.65,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.25+0.25,sin(angulo)*0.25-0.2,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.25-0.25,sin(angulo)*0.25-0.2,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.25+0.5,sin(angulo)*0.25+0.25,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.25,sin(angulo)*0.25+0.25,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.25-0.5,sin(angulo)*0.25+0.25,0.0)
    glEnd()
    glPopMatrix()

def dibujarGusanitos():
    global posX_gusanito1
    global posY_gusanito1
    global posX_gusanito2
    global posY_gusanito2
    global posX_gusanito3
    global posY_gusanito3
    global posX_gusanito4
    global posY_gusanito4
    global posX_gusanito5
    global posY_gusanito5

    #gusanito1
    #cabeza1
    glPushMatrix()
    glTranslatef(posX_gusanito1, posY_gusanito1, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(-90,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()
    #cuerpo
    glPushMatrix()
    glTranslatef(posX_gusanito1 - 0.02, posY_gusanito1 , 0.0)
    glScalef(0.01,0.01,0.01)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_QUADS)
    glVertex3f(-1,1,0)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()
    glPopMatrix()
    #cola
    glPushMatrix()
    glTranslatef(posX_gusanito1 - 0.04, posY_gusanito1, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(90,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()

    #gusanito2
    #cabeza1
    glPushMatrix()
    glTranslatef(posX_gusanito2, posY_gusanito2, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(-90,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()
    #cuerpo
    glPushMatrix()
    glTranslatef(posX_gusanito2 - 0.02, posY_gusanito2 , 0.0)
    glScalef(0.01,0.01,0.01)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_QUADS)
    glVertex3f(-1,1,0)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()
    glPopMatrix()
    #cola
    glPushMatrix()
    glTranslatef(posX_gusanito2 - 0.04, posY_gusanito2, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(90,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()

    
    #gusanito3
    #cabeza1
    glPushMatrix()
    glTranslatef(posX_gusanito3, posY_gusanito3, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(-90,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()
    #cuerpo
    glPushMatrix()
    glTranslatef(posX_gusanito3 - 0.02, posY_gusanito3 , 0.0)
    glScalef(0.01,0.01,0.01)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_QUADS)
    glVertex3f(-1,1,0)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()
    glPopMatrix()
    #cola
    glPushMatrix()
    glTranslatef(posX_gusanito3 - 0.04, posY_gusanito3, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(90,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()

    
    #gusanito4
    #cabeza
    glPushMatrix()
    glTranslatef(posX_gusanito4, posY_gusanito4, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(-45,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()
    #cuerpo
    glPushMatrix()
    glTranslatef(posX_gusanito4 - 0.012, posY_gusanito4 -0.012, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(-45,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_QUADS)
    glVertex3f(-1,1,0)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()
    glPopMatrix()
    #cola
    glPushMatrix()
    glTranslatef(posX_gusanito4 - 0.025, posY_gusanito4-0.025, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(135,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()

    #gusanito5
    #cabeza
    glPushMatrix()
    glTranslatef(posX_gusanito5, posY_gusanito5, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(135,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()
    #cuerpo
    glPushMatrix()
    glTranslatef(posX_gusanito5 + 0.012, posY_gusanito5 + 0.012, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(45,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_QUADS)
    glVertex3f(-1,1,0)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()
    glPopMatrix()
    #cola
    glPushMatrix()
    glTranslatef(posX_gusanito5 + 0.025, posY_gusanito5 + 0.025, 0.0)
    glScalef(0.01,0.01,0.01)
    glRotate(-45,0,0,1)
    glColor3f(0.8,0.2,0.3)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()
def dibujarGusano():
    global posX_gusano
    global posY_gusano
    global deltaPosX
    global deltaPosY
    global colisionAlimento
    global condicionMovXP
    global condicionMovXN
    global condicionMovYP
    global condicionMovYN

    #cabeza
    glPushMatrix()
    glTranslatef(posX_gusano, posY_gusano, 0.0)
    glScalef(0.05,0.05,0.05)
    if condicionMovXP == True:
        glRotatef(-90,0,0,1)
    elif condicionMovXN == True:
        glRotatef(90,0,0,1)
    elif condicionMovYP == True:
        glRotatef(0,0,0,1)
    elif condicionMovYN == True:
        glRotatef(180,0,0,1)
    else:
        glRotatef(-90,0,0,1)
    glColor3f(0.9,0.8,0.1)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    #ojos
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.45+0.5,sin(angulo)*0.45-0.6,0.0)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.3+0.5,sin(angulo)*0.3-0.45,0.0)
    glEnd()
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.45-0.5,sin(angulo)*0.45-0.6,0.0)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo)*0.3-0.5,sin(angulo)*0.3-0.45,0.0)
    glEnd()
    glPopMatrix()
    #cuerpo
    glPushMatrix()
    glTranslatef(posX_gusano + deltaPosX, posY_gusano + deltaPosY, 0.0)
    glScalef(0.05,0.05,0.05)
    glColor3f(0.9,0.8,0.1)
    glBegin(GL_QUADS)
    glVertex3f(-1,1,0)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()
    glPopMatrix()
    #cola
    glPushMatrix()
    glTranslatef(posX_gusano + deltaPosX * 2, posY_gusano + deltaPosY * 2, 0.0)
    glScalef(0.05,0.05,0.05)
    if condicionMovXP == True:
        glRotatef(90,0,0,1)
    elif condicionMovXN == True:
        glRotatef(-90,0,0,1)
    elif condicionMovYP == True:
        glRotatef(180,0,0,1)
    elif condicionMovYN == True:
        glRotatef(0,0,0,1)
    else:
        glRotatef(90,0,0,1)
    glColor3f(0.9,0.8,0.1)
    glBegin(GL_POLYGON)
    for x in range(180):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo),sin(angulo)-1.03,0.0)
    glEnd()
    glPopMatrix()

def dibujar():
    dibujarFondo()
    dibujarEspinas()
    dibujarGusanitos()
    dibujarAlimentos()
    dibujarGusano()

def main():
    #global tiempo
    #global tiempoAnterior
    global posX_gusano
    global posY_gusano

    global colisionPerder
    #serpienteLista = []
    
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Gusano", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    #Establecer callback de evento de teclado
    #glfw.set_key_callback(window, key_callback)
    #tiempo = glfw.get_time()
    #tiempoAnterior = glfw.get_time()
    
    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.3,0.2,0.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #Actualizar valores de la app
        actualizar(window)
        #Dibujar
        dibujar()

        if colisionPerder == True:
            print("Tu score fue de: ", score)
            sys.exit()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()