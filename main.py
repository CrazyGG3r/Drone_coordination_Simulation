import pygame
import sys
import classes as c
import design as d
import random as r
pygame.init()

window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Drone Coordination")

WHITE = (0,10,10)
offsety = 40
offsetx = 120
butt_h = 30
butt_w = 200
color_butt = (30,100,45)
bf = 1
heading = c.Text((window.get_width() // 4, window.get_height() // 5), 40,(200,200,200) ,"Drone Coordination Simulation",1)
sizefont = 30
t1 = c.Text((0, 0), sizefont, (0, 0, 0), "OPTION",bf)
b1 = c.button(((heading.x + offsetx), (heading.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t1)
t2 = c.Text((0, 0), sizefont, (0, 0, 0), "OPTION",bf)
b2 = c.button((b1.x, (b1.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t2)
t3 = c.Text((0, 0), sizefont, (0, 0, 0), "OPTION",bf)
b3 = c.button((b2.x, (b2.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t3)
t4 = c.Text((0, 0), sizefont, (0, 0, 0), "OPTION",bf)
b4 = c.button((b3.x, (b3.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t4)
all_text = [heading]
all_butts = [b1,b2,b3,b4]


##=-=- backgroufn

squares = []
population = 100
maxsize = 200
choice = [-1,1]
def reset_bg():
    for a in range(100):
        coo = (r.randint(0,window.get_width()),r.randint(0,window.get_height()))
        coloro = (0,r.randint(10,50),r.randint(10,50))
        raa = r.randint(0,100)/600
        raa = r.choice(choice) * raa
        squares.append(d.Square(coo,r.randint(10,maxsize),coloro,raa))
    
reset_bg()




running = True
while running:
    clicked_buttons = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for a in all_butts:
                if a.hover:
                    if not a.isClicked:
                        a.isClicked = True
                        clicked_buttons.append(a)
        if event.type == pygame.MOUSEBUTTONUP:
            for a in all_butts:
                if a.hover:
                    a.isClicked = False
    m = pygame.mouse.get_pos()
    for a in all_butts:
        if m[0] > a.x and m[1] > a.y:
            if m[0] < (a.x + a.width) and m[1] < (a.y + a.height):
                a.hover = True
            else:
                a.hover = False
        else:
            a.hover = False
    for a in clicked_buttons:
        a.action()
    window.fill(WHITE)
    for a in squares:
        a.draw(window)
    for a in all_text:
        a.draw(window)
    for a in all_butts:
        a.draw(window)
    
    pygame.display.flip()


pygame.quit()
sys.exit()
