import numpy as np
import pygame
from random import randint
from math import sqrt

#Índices NumPy
x=0
y=1

class Particula:        
    def __init__(self, X, Y, vx, vy, raio, R, G, B):
        self.pos=np.array([float(X),float(Y)])
        self.vel=np.array([float(vx),float(vy)])
        self.raio=raio
        self.R=R
        self.G=G
        self.B=B
    def draw(self, screen):
        pygame.draw.circle(screen, (self.R, self.G, self.B), (self.pos[x], self.pos[y]), self.raio)
    def atualiza_pos(self, dt):
        self.pos[x]=round(self.pos[x]+self.vel[x]*dt)
        self.pos[y]=round(self.pos[y]+self.vel[y]*dt)
    def colisao(self, outra): 
        dist=sqrt(pow(self.pos[x]-outra.pos[x], 2)+pow(self.pos[y]-outra.pos[y], 2))
        if dist<=(self.raio+outra.raio) and dist>0:
            return dist
        return 0
    def colisao_particula(self, outra, dist):
        v1_atual=self.vel
        v2_atual=outra.vel
        self.vel=self.vel-np.inner(v1_atual-v2_atual, self.pos-outra.pos)*(self.pos-outra.pos)/(pow(dist,2))
        outra.vel=outra.vel-np.inner(v2_atual-v1_atual,outra.pos-self.pos)*(outra.pos-self.pos)/(pow(dist,2))
                
        #Corrigindo a posição da partícula após a colisão para evitar sobreposição:
        direcao_colisao=(self.pos-outra.pos)/dist
        sobreposicao=(self.raio+outra.raio)-dist
        self.pos=self.pos+direcao_colisao*(sobreposicao / 2)
        outra.pos=outra.pos- direcao_colisao*(sobreposicao/2)
    def colisao_parede(self, height, width):
        if self.pos[x]+self.raio>width:
            self.pos[x]=width-self.raio
            self.vel[x]*=-1
        elif self.pos[x]-self.raio<0:
            self.pos[x]=self.raio
            self.vel[x]*=-1
        if self.pos[y]+self.raio>height:
            self.pos[y]=height-self.raio
            self.vel[y]*=-1
        elif self.pos[y]-self.raio<0:
            self.pos[y]=self.raio
            self.vel[y]*=-1
    def atualizar(self, dt, height, width, screen):
        self.colisao_parede(height, width)
        self.atualiza_pos(dt)
        self.draw(screen)
