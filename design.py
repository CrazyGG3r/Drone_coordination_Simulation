import pygame
pygame.init()
import random as r 


class Square:
    def __init__(self,coords,l,color,ra):
        self.l = l
        self.color = color
        self.coords = coords
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.angle = r.randint(0,360)
        self.surface = pygame.Surface((self.l,self.l))
        self.RotationalSpeed = ra
        
    def draw(self, screen):  
        square_surface = pygame.Surface((self.l, self.l), pygame.SRCALPHA)
        square_surface.fill(self.color)
        rotated_surface = pygame.transform.rotate(square_surface, self.angle)
        rect = rotated_surface.get_rect(center=self.coords)
        screen.blit(rotated_surface, rect.topleft)
        self.angle += self.RotationalSpeed  
    def updateCoord(self,coords):
        self.coords = coords
    def rotate(self,):
        pass
        # pygame.draw.rect(screen,self.color,(self.x, self.y, self.l, self.l))


class Trailsquare:
    def __init__(self,size,):
        self.size = size
        self.trail = {}
        self.maxsize = 10
        self.createTrail()
    
    def update(self,mouse):
        keeys = list(self.trail.keys())
        previous = mouse
        for a in keeys:
            curr = self.trail[a]
            self.trail[a] = previous
            previous = curr
            
            
    def createTrail(self):
        choice = [-1.1]
        for a in range(self.size):
            coo = (0,0)
            coloro = (r.randint(150,255),r.randint(150,255),r.randint(150,255))
            raa = r.randint(0,100)/1000
            raa = r.choice(choice) * raa
            self.trail[Square(coo,r.randint(10,self.maxsize),coloro,raa)] = (0,0)
        print(self.trail)
    
    def draw(self, screen):
        for a in self.trail:
            a.updateCoord(self.trail[a])
            a.draw(screen)