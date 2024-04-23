import pygame
import design as d
import classes as c
pygame.init()
background_color = (0,10,10)

def settings11(window):
    bgg =  d.Background(window,200,3)
    tr = d.Trailsquare(20)
    
    running = True
    
    while running:
        window.fill(background_color)
        bgg.draw(window)
        
        clicked_buttons = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                bgg.reset_bg(window)
        tr.update(pygame.mouse.get_pos())
        tr.draw(window)
        pygame.display.flip()
    

#this module contains ui settings




