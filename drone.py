import pygame
import sys
import random
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
        self.drones = []  
        for _ in range(quantity):  
            self.drones.append(CreateDrone(10, [random.randint(0, window_width), random.randint(0, window_height)], 2, False))
        #Creating Destination
        self.destination = CreateDrone(5, [700, 300], 0, True)
            
    def run(self):
        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Move drones towards the destination
            for drone in self.drones:
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

                # Boundary checking to keep drones within the window
                drone.position[0] = limit_value(drone.position[0], drone.radius, window_width - drone.radius)
                drone.position[1] = limit_value(drone.position[1], drone.radius, window_height - drone.radius)

            # Clear the window
            window.fill(WHITE)

            # Draw drones
            for drone in self.drones:
                drone.draw(window, GREEN)

            # Draw destination
            self.destination.draw(window, RED)

            # Update the display
            pygame.display.flip()

            # Control the frame rate
            pygame.time.Clock().tick(60)
            
test = Drone(2)
test.run()

# Quit Pygame
pygame.quit()
sys.exit()
