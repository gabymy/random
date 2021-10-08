# Importamos las bibliotecas 
import pygame
import random
from pygame.locals import *
import PIL
 
# Inicializar
pygame.init()

#Variables 
NEGRO = [0, 0, 0]
BLANCO = [255, 255, 255]
GRIS = [105, 105, 105]
CELESTE = [135, 206, 250]

 
#largo y ancho de la pantalla
dimensiones = [800, 600]

#descripcion pantalla 
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Llueve")
#imagen = pygame.image.load("usaresta").convert_alpha()
#pantalla.blit(imagen, (10, 10))
pygame.display.flip()

 
#array vacío
lista_lluvia = []
 
# Iteramos y añadimos lluvia en una ubicación (x,y) aleatoria.
for i in range(250):
    x = random.randrange(0, 600)
    y = random.randrange(0, 800)
    lista_lluvia.append([x, y])
 
reloj = pygame.time.Clock()
 
# Iteramos hasta que el usuario haga click sobre le botón de salida.
hecho = False
while not hecho:
     
    for evento in pygame.event.get():  # El usuario realizó alguna acción.
        if evento.type == pygame.QUIT: # Si el usuario hizo click sobre salir.
            hecho = True # Marcamos que hemos acabado y abandonamos este bucle.
 
    # Establecemos el color de fondo.
    pantalla.fill(NEGRO)
 
    # Procesamos cada copo de la lista.
    for i in range(len(lista_lluvia)):
    
        # Dibujamos el copo de nieve
        pygame.draw.circle(pantalla, CELESTE, lista_lluvia[i], 1)
         
        # Desplazamos un píxel hacia abajo el copo de nieve.
        lista_lluvia[i][1] += 1
         
        # Si el copo se escapa del fondo de la pantalla.
        if lista_lluvia[i][1] > 600:
            # Lo movemos justo encima del todo
            y = random.randrange(-100, -50)
            lista_lluvia[i][1] = y
            # Le damos una nueva ubicación x
            x = random.randrange(0, 800)
            lista_lluvia[i][0] = x
             
    # Avanzamos y actualizamos con lo que hemos dibujado.
    pygame.display.flip()
    reloj.tick(60)
             
# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.

pygame.quit ()
