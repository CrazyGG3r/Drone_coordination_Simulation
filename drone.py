import pygame
import sys
import random
import math
from classes import CreateDrone, limit_value,button,Text
from settings import * 
import design as d
import colors as cc
# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moving Drones")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = cc.colorlist[12]

class Drone:
    def __init__(self, quantity):
        #Creating Drones
        self.drones = []  # Corrected the variable name
        for i in range(quantity):  # Use underscore (_) for unused variable
            self.drones.append(CreateDrone(10, [random.randint(0, window_width), random.randint(0, window_height)], 2, False,i,GREEN))
        #Creating Destination
        self.destination = CreateDrone(5, [700, 300], 0, True,'Destination',RED)
         
    def check(self,drone):
        # If the destination is to the right of the drone, move right
        if drone.position[0] < self.destination.position[0]:
            drone.position[0] += drone.speed
        # If the destination is to the left of the drone, move left
        elif drone.position[0] > self.destination.position[0]:
            drone.position[0] -= drone.speed
        # If the destination is below the drone, move down
        if drone.position[1] < self.destination.position[1]:
            drone.position[1] += drone.speed
        # If the destination is above the drone, move up
        elif drone.position[1] > self.destination.position[1]:
            drone.position[1] -= drone.speed
            
         # Avoid collisions with other drones
        for other_drone in self.drones:
            if other_drone != drone:
                distance = math.sqrt((drone.position[0] - other_drone.position[0]) ** 2 + (drone.position[1] - other_drone.position[1]) ** 2)
                min_distance = drone.radius + other_drone.radius + 5  # Add a buffer distance for safety
                if distance < min_distance:
                    # Drones are too close, adjust position
                    dx = drone.position[0] - other_drone.position[0]
                    dy = drone.position[1] - other_drone.position[1]
                    angle = math.atan2(dy, dx)
                    new_x = other_drone.position[0] + math.cos(angle) * min_distance
                    new_y = other_drone.position[1] + math.sin(angle) * min_distance
                    drone.position = [new_x, new_y]
                    
        # Boundary checking to keep drones within the window
        drone.position[0] = limit_value(drone.position[0], drone.radius, window_width - drone.radius)
        drone.position[1] = limit_value(drone.position[1], drone.radius, window_height - drone.radius)

def drones(window):
    bgg = d.Background(window,10,2)  
    trail = d.Trailsquare(5)
    test = Drone(9)      
    
    t1 = Text((0,0),30,(0,0,0),"Change to threeD",3)
    
    button
    b1 = button((100 ,500),300,40,(0,0,0),(10,5),t1,)
    all_butts = [b1]
    
    running = True
    while running:
        clicked_buttons = []
        # Event handling
        window.fill(background_color)
        bgg.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return
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
        for a in clicked_buttons:
            a.action(window)
            a.isClicked = False
        for drone in test.drones:
            test.check(drone)
            
    
        
        
        trail.update(pygame.mouse.get_pos())
        trail.draw(window)
    
        for drone in test.drones:
            drone.draw(window)
    
        for a in all_butts:
            a.draw(window)
        test.destination.draw(window)
        
        # Update the display
        pygame.display.flip()
    
        # Control the frame rate
        # pygame.time.Clock().tick(60)
    
    
    # Quit Pygame
    pygame.quit()
    sys.exit()
