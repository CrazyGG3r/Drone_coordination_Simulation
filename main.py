
import pygame
import sys
import classes as c
import design as d
import random as r
from settings import background_color,settingsaa
import drone as d2
import colors as cc


pygame.init()

window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("TardNet")
pygame.mouse.set_visible(False)

 

population = 100
maxsize = 150
choice = [-1,1]
WHITE = (0,0,0)
offsety = 50
offsetx = 160
butt_h = 40
butt_w = 200
neon  = 150
color_butt = (0,neon,neon)
bf = 3
textcolor = cc.colorlist[12]
heading = c.Text(((window.get_width() // 3.2 )-125, (window.get_height() // 3)-20), 45,textcolor ,"    Drone Coordination Simulation",3)
sizefont = 30
buttpaddx = 0
#0c0c0c,201310,351b15,4a2319,5f2a1e,743223,893a27,9e422c,b34931,c85135,dd593a,f2613f
fcolor = cc.colorlist[2]
t1 = c.Text((0, 0), sizefont, fcolor, "Start",bf)

t3 = c.Text((0, 0), sizefont, fcolor, "Options",bf)
t4 = c.Text((0, 0), sizefont, fcolor, "Credits",bf)
t5 = c.Text((0, 0), sizefont, fcolor, "Exit",bf)

b1 = c.button((((window.get_width() // 3.2 ) + offsetx), ((window.get_height() // 3) + offsety + 10)), butt_w, butt_h, color_butt, (10, 5), t1,d2.drones)
b3 = c.button((b1.x-buttpaddx, (b1.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t3,settingsaa)
b4 = c.button((b3.x-buttpaddx, (b3.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t4,)
b5 = c.button((b4.x-buttpaddx, (b4.y + offsety)), butt_w, butt_h, color_butt, (10, 5), t5,exit)
all_text = [heading]
all_butts = [b1,b3,b4,b5]

def reset_everything():
    global heading
    heading.update_coords(((window.get_width() // 3.2 )-125, (window.get_height() // 3)-20))
    global b1,b3,b4,b5
    b1.update_Coords((((window.get_width() // 3.2 ) + offsetx), ((window.get_height() // 3) + offsety + 10)))
    b3.update_Coords((b1.x-buttpaddx, (b1.y + offsety)))
    b4.update_Coords((b3.x-buttpaddx, (b3.y + offsety)))
    b5.update_Coords((b4.x-buttpaddx, (b4.y + offsety)))





##=-=- backgroufn

bgg = d.Background(window,70,1)
tra = d.Trailsquare(7)
prevwidth = window.get_width()
prevheight = window.get_height()

running = True
while running:
    clicked_buttons = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for a in all_butts:
                if a.hover and not a.isClicked:
                        a.isClicked = True
                        clicked_buttons.append(a)
    m = pygame.mouse.get_pos()
    for a in all_butts:
        if m[0] > a.x and m[1] > a.y:
            if m[0] < (a.x + a.width) and m[1] < (a.y + a.height):
                a.hover = True
            else:
                a.hover = False
        else:
            a.hover = False
    if prevwidth != window.get_width() or prevheight != window.get_height(): #responsiveness
        prevwidth = window.get_width()
        prevheight = window.get_height()
        reset_everything()
    for a in clicked_buttons:
        a.action(window)
        a.isClicked = False
        bgg.reset_bg(window)
        tra.resetTrail()
     
        

    bgg.draw(window)
    
    for a in all_text:
        a.updateColor()
        a.draw(window)
    for a in all_butts:
        a.updateColor()
        a.draw(window)
    
    m = pygame.mouse.get_pos()
    tra.update((m[0],m[1]))
    tra.draw(window)
    pygame.display.flip()


pygame.quit()
sys.exit()
