import pygame

## from pygame.locals import *
import random

## EDGE_COLOR = (51, 173, 255)
EDGE_COLOR = (143, 189, 212)

class Cell(pygame.sprite.Sprite):
    def __init__(self, game, pos, num):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        
        self.num = num
        self.color = self.getColor()
    
        self.parent = 0

        self.image = pygame.Surface([10,10])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
        self.alive = False
        self.prev_alive = [False, False]
        self.edge = False

        self.a_neighbors = []
        self.d_neighbors = []
        self.w = self.game.WIDTH

        self.n = (num - self.w) - 1  ## num - 75 ## nord   
        ## self.n = (num - 74) - 1  ## num - 75 ## nord   
        self.e = (num + 1) - 1   ## num      ## east
        self.s = (num + self.w) - 1  ## num + 73 ## south        
        ## self.s = (num + 74) - 1  ## num + 73 ## south        
        self.w = (num - 1) - 1   ## num - 2  ## west
        self.ne = (self.n + 1)   ## num - 74 ## nord-east
        self.se = (self.s + 1)   ## num + 74 ## south-east
        self.nw = (self.n - 1)   ## num - 76 ## nord-west
        self.sw = (self.s - 1)   ## num + 72 ## south-west

        self.cell_list = [
            self.n,
            self.e,
            self.s,
            self.w,
            self.ne,
            self.se,
            self.nw,
            self.sw]

        self.game.cells.append(self)
    def getColor(self):
        value = [i for i in range(100,255,25)]
        r = random.choice(value)
        g = random.choice(value)
        b = random.choice(value)
        return (r,g,b)
        
        
    def die(self):
        self.alive = False

    def live(self):
        self.alive = True
 
    def update(self):
        if not self.edge:
            self.a_neighbors = []
            self.d_neighbors = []
            neighbors = [self.game.cells[cell] for cell in self.cell_list]

            for n in neighbors:
                if n.alive:
                    self.a_neighbors.append(True)
                else:
                    self.d_neighbors.append(True)   

            if not self.game.startGame:
                    
                if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(self.game.mpos):
                    self.alive = True
                    self.image.fill(self.color)                                       
                    
                if pygame.mouse.get_pressed()[2] and self.rect.collidepoint(self.game.mpos)and self.alive:
                    self.image.fill((0,0,0))
                    self.alive = False
                    
                if self.alive:
                    self.image.fill(self.color)
            else:
                if self.alive:
                    self.image.fill(self.color)
                    
                if not self.alive:
                    self.image.fill((0, 0, 0))
                    
        else:
            self.image.fill(EDGE_COLOR)
            