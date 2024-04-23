import pygame
import sys
import random
import math
from classes import CreateDrone, limit_value

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moving Drones")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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
                min_distance = drone.radius + other_drone.radius + 10  # Add a buffer distance for safety
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
        
    test = Drone(9)      
    
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.button == pygame.K_BACKSPACE:
                    return
     
        for drone in test.drones:
            test.check(drone)
            
    
        # Clear the window
        window.fill(WHITE)
    
        # Draw drones
        for drone in test.drones:
            drone.draw(window)
    
        # Draw destination
        test.destination.draw(window)
    
        # Update the display
        pygame.display.flip()
    
        # Control the frame rate
        pygame.time.Clock().tick(60)
    
    
    # Quit Pygame
    pygame.quit()
    sys.exit()
