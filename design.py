import pygame
pygame.init()



class Square:
    def __init__(self,coords,l,color,ra):
        self.l = l
        self.color = color
        self.coords = coords
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.angle = 100
        self.surface = pygame.Surface((self.l,self.l))
        self.RotationalSpeed = ra
        # def draw(self,screen):
        #     self.surface.fill(self.color)
        #     self.surface = pygame.transform.rotate(self.surface,self.angle)
        #     screen.blit(self.surface,self.coords)
        #     self.angle+=0.0001
        
    def draw(self, screen):
        
        square_surface = pygame.Surface((self.l, self.l), pygame.SRCALPHA)
        square_surface.fill(self.color)
        rotated_surface = pygame.transform.rotate(square_surface, self.angle)
        rect = rotated_surface.get_rect(center=self.coords)
        screen.blit(rotated_surface, rect.topleft)
        self.angle += self.RotationalSpeed  

    def rotate(self,):
        pass
        # pygame.draw.rect(screen,self.color,(self.x, self.y, self.l, self.l))



