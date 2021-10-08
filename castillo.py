import pygame
import random

AZULNOCHE = (9, 35, 67)
VERDEPASTO = (17, 99, 67)
VERDE = (10, 255, 10)
BLANCO = (222, 224, 200)
GRIS = (186, 186, 177)
GrisCastillo = (158, 158, 158)
NEGRO = (2, 3, 3)
ROJO = (255, 0, 0)
CELESTE = [135, 206, 250]



Centro = []
for i in range(15):
    Centro.append([random.randrange(50, 390), random.randrange(0, 200)])

pygame.init()
Dimensiones = (400, 500)
Pantalla = pygame.display.set_mode(Dimensiones)
pygame.display.set_caption("CASTILLO")

lista_lluvia = []

Terminar = False
reloj = pygame.time.Clock()

while not Terminar:
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
    #manejo de eventos
    #La lógica del juego
    #Codigo de dibujo
    Pantalla.fill((255, 255, 255))

    pygame.draw.rect(Pantalla, AZULNOCHE, [0, 0, 400, 300], 0)
    pygame.draw.rect(Pantalla, VERDEPASTO, [0, 300, 400, 300], 0)
    pygame.draw.circle(Pantalla, BLANCO, [25, 25], 20, 0)
    pygame.draw.circle(Pantalla, GRIS, [15, 15], 4, 1)
    pygame.draw.circle(Pantalla, GRIS, [36, 24], 3, 1)
    pygame.draw.circle(Pantalla, GRIS, [24, 35], 5, 1)
    
    for y in range(0, 195, 7):
        for x in range(0, 398, 4):
            pygame.draw.line(Pantalla, VERDE, [x, 310 + y], [x + 2, 305 + y], 1)

    for i in range(2):
        x = random.randrange(0, 500)
        y = random.randrange(0, 300)
        lista_lluvia.append([x, y])

    for i in range(len(lista_lluvia)):
        pygame.draw.circle(Pantalla, CELESTE, lista_lluvia[i], 1)
        #lista_lluvia[i][1] += 1
        if lista_lluvia[i][1] > 200:
            y = random.randrange (2, 100)
            lista_lluvia[i][0] = y
            x = random.randrange (0, 200)
            lista_lluvia[i][0] = x
            reloj.tick(5)
             
           
    #---Castillo---
    for x in range(0, 70, 20):
        pygame.draw.rect(Pantalla, GrisCastillo, [290 + x, 220, 10, 10])
        pygame.draw.rect(Pantalla, NEGRO, [290 + x, 220, 10, 10], 1)
    pygame.draw.rect(Pantalla, GrisCastillo, [250, 200, 40, 105], 0)
    pygame.draw.rect(Pantalla, NEGRO, [250, 200, 40, 105], 2)
    pygame.draw.rect(Pantalla, NEGRO, [262, 210, 16, 16], 0)
    pygame.draw.rect(Pantalla, GrisCastillo, [290, 230, 70, 75], 0)
    pygame.draw.rect(Pantalla, NEGRO, [290, 230, 70, 75], 2)
    pygame.draw.rect(Pantalla, GrisCastillo, [360, 200, 40, 105], 0)
    pygame.draw.rect(Pantalla, NEGRO, [360, 200, 40, 105], 2)
    pygame.draw.rect(Pantalla, NEGRO, [372, 210, 16, 16], 0)
    pygame.draw.polygon(Pantalla, ROJO, [[248, 200], [270, 178], [292, 200]])
    pygame.draw.polygon(Pantalla, ROJO, [[358, 200], [380, 178], [402, 200]])
    pygame.draw.circle(Pantalla, NEGRO, [325, 270], 15, 0)
    pygame.draw.circle(Pantalla, NEGRO, [325, 270], 15, 2)
    pygame.draw.rect(Pantalla, NEGRO, [310, 270, 30, 30], 0)
    pygame.draw.rect(Pantalla, NEGRO, [310, 270, 30, 30], 1)
    pygame.draw.circle(Pantalla, NEGRO, [325, 270], 13, 0)
    #fuente
    Fuente = pygame.font.Font(None, 25)
    Texto = Fuente.render("ERASE UNA VEZ.....", True, BLANCO)
    Pantalla.blit(Texto, [250, 10])
    pygame.display.flip()
    reloj.tick(20)
pygame.quit()
