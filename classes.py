import pygame
import random

font = ['assets/fonts/f1.ttf',None]


class Text:
    def __init__(self, coords, font_size, color, text, fonts=None):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.x = coords[0]
        self.y = coords[1]
        self.font = pygame.font.Font(font[1], font_size)
        self.surface = self.font.render(text, True, color)

    def update_text(self, new_text):
        self.text = new_text
        self.surface = self.font.render(new_text, True, self.color)
    def update_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def changecolor(self, color):
        self.color = color


def dummy():
    print("Clicked somehting",random.randint(0,10))


class button:
    def __init__(self, coords, w, h, color,padding, butt_text, function = None):
        self.x = coords[0]
        self.y = coords[1]
        self.pad_x = self.x + padding[0]
        self.pad_y = self.y + padding[1]
        self.width = w
        self.height = h
        self.NotHovercolor = color
        self.Hovercolor = []
        for n, a in enumerate(self.NotHovercolor):
            a = 255 - a
            if a <= -1:
                a *= -1
            self.Hovercolor.append(a)
        self.Hovercolor = tuple(self.Hovercolor)
        print(self.Hovercolor)
        self.text = None
        self.hover = False
        self.text = butt_text
        self.text.update_coords((self.pad_x,self.pad_y))
        self.action = dummy
        self.isClicked = False

    def draw(self, screen,):
        if self.hover:
            pygame.draw.rect(screen, self.Hovercolor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.NotHovercolor, (self.x, self.y, self.width, self.height))
        self.text.draw(screen)