import pygame
from random import randint
from pathlib import Path
from particula import Particula

FPS=60
lista_particulas=[]
WIDTH=1280
HEIGHT=720
dt=0
FUNDO=(0, 140, 70)
menu=1
nparticulas=''
raio=''
running=True
clock=pygame.time.Clock()
typing_nparticulas=False
typing_raio=False
error=False

pygame.init()
icon=str(Path(__file__).resolve().parent)+'\\Imagens\\icon.png'
icon=pygame.image.load(icon)
pygame.display.set_icon(icon)
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simulador de Colisões')
title_font=pygame.font.SysFont('freesansbold', 75)
text_font=pygame.font.SysFont('freesansbold', 58)
title='Simulador de Colisões Elásticas'
nparticulas_text='Número de particulas:'
raio_text='Raio das particulas:'
description_1='Preencha ambos os campos e'
description_2='pressione Enter'
error_text='Diminua o raio e/ou o número de particulas'
nparticulas_rect=pygame.Rect(905,250,115,60)
raio_rect=pygame.Rect(870,330,115,60)
typing_color=pygame.Color('gray30')
resting_color=pygame.Color('gray0')

def number(key):
    if (key==pygame.K_0 or key==pygame.K_KP0 or 
        key==pygame.K_1 or key==pygame.K_KP1 or 
        key==pygame.K_2 or key==pygame.K_KP2 or 
        key==pygame.K_3 or key==pygame.K_KP3 or 
        key==pygame.K_4 or key==pygame.K_KP4 or 
        key==pygame.K_5 or key==pygame.K_KP5 or 
        key==pygame.K_6 or key==pygame.K_KP6 or 
        key==pygame.K_7 or key==pygame.K_KP7 or 
        key==pygame.K_8 or key==pygame.K_KP8 or 
        key==pygame.K_9 or key==pygame.K_KP9):
        return True
    else:
        return False

while running and menu:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            running=False 
        if event.type==pygame.MOUSEBUTTONDOWN: 
            if nparticulas_rect.collidepoint(event.pos): 
                typing_nparticulas=True
            else:
                typing_nparticulas=False
            if raio_rect.collidepoint(event.pos):
                typing_raio=True
            else:
                typing_raio=False
        if event.type==pygame.KEYDOWN:
            if typing_nparticulas:
                if event.key==pygame.K_BACKSPACE:
                    nparticulas=nparticulas[:-1]
                elif len(nparticulas)<3 and number(event.key):
                    nparticulas+=event.unicode
                elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    typing_nparticulas=False
                    typing_raio=True
            if typing_raio:
                if event.key==pygame.K_BACKSPACE:
                    raio=raio[:-1]
                elif len(raio)<3 and number(event.key):
                    raio+=event.unicode
                elif len(raio)>0 and len(nparticulas)>0 and (event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER):
                    if int(raio)*int(nparticulas)<WIDTH and 2*int(raio)<HEIGHT and 2*int(raio)<HEIGHT-2*int(raio): 
                        menu=False
                    else:
                        error=True

    screen.fill(FUNDO)

    if typing_nparticulas:
        color_nparticulas=typing_color
    else:
        color_nparticulas=resting_color
    pygame.draw.rect(screen, color_nparticulas, nparticulas_rect)
    pygame.draw.rect(screen, (0,0,0), nparticulas_rect, 2)
    text=text_font.render(nparticulas, True, (255, 255, 255))
    screen.blit(text, (nparticulas_rect.x+6, nparticulas_rect.y+2))
    text=text_font.render(nparticulas_text, True, (255, 255, 255))
    screen.blit(text, (nparticulas_rect.x-640, nparticulas_rect.y+2))

    if typing_raio:
        color_raio=typing_color
    else:
        color_raio=resting_color
    pygame.draw.rect(screen, color_raio, raio_rect)
    pygame.draw.rect(screen, (0,0,0), raio_rect, 2)
    text=text_font.render(raio, True, (255, 255, 255))
    screen.blit(text, (raio_rect.x+5, raio_rect.y+2))
    text=text_font.render(raio_text, True, (255, 255, 255))
    screen.blit(text, (raio_rect.x-580, raio_rect.y+2))

    text=title_font.render(title, True, (255, 255, 255))
    screen.blit(text, (640-text.get_rect().width/2, 10))

    text=text_font.render(description_1, True, (255, 255, 255))
    screen.blit(text, (640-text.get_rect().width/2, 550))
    text=text_font.render(description_2, True, (255, 255, 255))
    screen.blit(text, (640-text.get_rect().width/2, 620))

    if(error):
        text=text_font.render(error_text, True, pygame.Color('red2'))
        screen.blit(text, (640-text.get_rect().width/2, 400))
    
    pygame.display.flip()

if not menu:
    nparticulas=int(nparticulas)
    raio=int(raio)

    for i in range(nparticulas):
        lista_particulas.append(Particula(randint(raio, WIDTH-raio), randint(raio, HEIGHT-raio), randint(-500, 500), randint(-500, 500), raio, randint(0, 255), randint(0, 255), randint(0, 255)))

    while running:
        dt=clock.tick(FPS)/1000
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                running=False    

        screen.fill(FUNDO)

        for i in range(len(lista_particulas)):
            particula_i=lista_particulas[i]
            for j in range(i+1, len(lista_particulas)):
                particula_j=lista_particulas[j]
                dist=particula_i.colisao(particula_j)
                if(dist>0):
                    particula_i.colisao_particula(particula_j,dist)
            particula_i.atualizar(dt, HEIGHT, WIDTH, screen)

        pygame.display.flip()
        
pygame.quit()