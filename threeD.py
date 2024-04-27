import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from classes import CreateEnvironment, CreateSpheres, distance

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, display[0] / display[1], 0.1, 50.0)
glTranslatef(0.0, -1.0, -10.0)

environment = CreateEnvironment((display[0] // 2, display[1] // 2))
environment.setup_lighting()
clock = pygame.time.Clock()

class ThreeDrone:
    def __init__(self, n):
        self.drones = []
        for i in range(n):
            self.drones.append(CreateSpheres(0.5, 100, (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))))
        self.stationary_sphere = CreateSpheres(1, 100, (8, 8, 8))

    def update(self, drone):
        direction = [(self.stationary_sphere.position[i] - drone.position[i]) for i in range(3)]
        direction_length = sum(map(lambda x: x ** 2, direction)) ** 0.5
        direction = [x / direction_length for x in direction]

        new_position = [drone.position[i] + direction[i] * 0.04 for i in range(3)]

        for other_drone in self.drones:
            if other_drone != drone and distance(new_position, other_drone.position) < 2:
                new_position = [new_position[i] + (new_position[i] - other_drone.position[i]) * 0.04 for i in range(3)]

        drone.position = new_position

def run():
    test = ThreeDrone(9)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        environment.handle_keys()
        environment.handle_mouse()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        environment.draw_grid(10, 1)

        for drone in test.drones:
            test.update(drone)
        
        for drone in test.drones:
            drone.draw_sphere(False)
        test.stationary_sphere.draw_sphere(True)
        

        pygame.display.flip()
        clock.tick(60)
        
run()


