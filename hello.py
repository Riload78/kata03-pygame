import pygame
pygame.init()
## Creacion de la ventana del juego
pantalla = pygame.display.set_mode((800,600))

metronomo = pygame.time.Clock()


# Titulo de pantalla
pygame.display.set_caption('Hola Mundo')
game_over =  False
azul = 0
# Montar el bucle principal
while game_over == False:
    metronomo.tick(60)

    ## vaciar el buffer de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        
    azul += 1
    if azul > 255:
        azul = 0
        
    # color de pantalla
    pantalla.fill((0,0,azul))
    # mostrar en pantalla
    pygame.display.flip()