# Fuente: https://www.glowscript.org/docs/VPythonDocs/camera.html

from vpython import *
from time import sleep


# Parametros de ventana
w_text = "Lorem ipsum."
w_title = "Título va acá."
w_height = 400
w_width = 700


# Inicialización de aspectos visuales de la ventana
scene.title = w_title
scene.caption = w_text
scene.height = w_height
scene.width = w_width

scene.autoscale = True  # Zoom automático de la cámara para calzar todo

# Ordinariamente el usuario puede mover la cámara a gusto, por lo cual 
# se requiere bloquear manualmente
scene.userzoom = False  # Bloquear zoom
scene.userspin = False  # Bloquear rotación
scene.userpan = False  # Bloquear movimiento lineal


# Declaración el objeto a mostrar
example = box(  
    color=color.white, length=4, width=4,
    height=4
)

delta = 10

while w_width < 900:

    rate(500)  # Ritmo  de refrescamiento 

    w_height = w_height + delta
    w_width = w_width + delta

    # Durante la ejecución del programa, pueden actualizar valores a gusto
    scene.height = w_height
    scene.width = w_width

    # Además, existe una función para tiempo de espera
    sleep(0.5)


# La visualización se cierra al terminar el programa,
# por tanto hay que evitar que esto ocurra.
while True:  
    rate(500)