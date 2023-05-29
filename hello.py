import pygame

## Creacion de la ventan del juego
pantalla = pygame.display.set_mode((800,600))

# Titulo de pantalla
pygame.display.set_caption('Hola Mundo')
game_over =  False
# Montar el bucle principal
while True:
    ## vaciar el buffer de eventos
    for evento in pygame.get():
        if evento.type == pygame.QUIT:
            game_over = True
        
    # color de pantalla
    pantalla.fill((0,0,255))
    # mostrar en pantalla
    pygame.display.flip()