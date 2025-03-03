from vpython import *
from time import sleep
import math


# Parametros de objetos a visualizar
length = 4
side = 4
thick = 4
radius = 2

# La animación se reproduce como normalmente sin importar
box = box(  # Como CILINDRO, si declaro grosor y eso lo toma como elipse
    color=color.magenta,
    length=side,  # eje x
    width=side,  # eje z
    height=thick,  # eje y
    pos= vector(0, 0,0) # Posición de centro de figura, NOTE CLASE TIPO vpython.vector
)

ball = sphere(
    color=color.blue,
    radius=radius
)

# Se puede cambiar aspectos varios durante programa

# Ciclo ejemplo para cambios de color
for i in arange(0,2,1):
    sleep(1)
    box.color = color.cyan
    sleep(1)
    box.color = color.magenta


# Ciclo ejemplo para cambios en posición
deltaX = -0.5
xPos = 0
while abs(xPos) < 5:
    sleep(0.5)
    xPos = deltaX + xPos
    ball.pos = vector(xPos, 0, 0)

deltaX = 0.5
xPos = 0
while abs(xPos) < 5:
    sleep(0.5)
    xPos = deltaX + xPos
    box.pos = vector(xPos, 0, 0)


# Ciclo ejemplo para cambios en ángulo
# Para el CANSAT, será necesario usar cuaterniones:
# Pasar de rotación de dirección del vector al que apunta el dispositivo
# a sus componentes en x, y, z
deltaAxis = 0.1*math.pi
angle = 0
while True:
# Si se requiere determinar: 
#    1. tasa de ejecución de la animación
#    2. ritmo de redraw del display
#    3. ritmo de procesamiento de eventos inputs del usuario
#    Se le debe dar un loop no interrumpible al código

    rate(300)  
    angle = angle + deltaAxis
    z = math.cos(angle)
    y = math.sin(angle)
    box.axis = vector(1, y, z)
    if angle == 2*math.pi:
        angle = 0
