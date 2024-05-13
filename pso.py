import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from classes import CreateEnvironment, CreateParticles, distance, CreateSpheres

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, display[0] / display[1], 0.1, 50.0)
glTranslatef(0.0, -1.0, -10.0) 

environment = CreateEnvironment((display[0] // 2, display[1] // 2))
environment.setup_lighting()
clock = pygame.time.Clock()

class PSO:
    def __init__(self, n, m):
        self.particles = []
        self.stationary_spheres = []
        self.count=m
        
        i = 0
        while i < m/2:
            j = 0  
            while j < m/2:
                z=j+3
                position = (i, 0, z)
                self.stationary_spheres.append(CreateSpheres(0.5, 100, position))
                j += 2  
            i += 2
        
        i = -m/2
        while i<0:
            j = -m/2  
            while j <0:
                
                position = (i, 0, j)
                self.stationary_spheres.append(CreateSpheres(0.5, 100, position))
                j += 2  
            i += 2
            
            
        

            
        i = 0
        while i < n:
            j=0
            neg_i = -1 * i
            while j < i:
                x = i
                z = neg_i - 2
                position = (x,5,z)
                self.particles.append(CreateParticles(0.1, 10, position))  # Set parameters for particles
                j = j+1
                neg_i = neg_i + 2
            i = i+1

    

    def update(self, particle):
        if len(self.stationary_spheres) == 0:
            return

        for stationary_sphere in self.stationary_spheres:
            if (particle.position[0] - stationary_sphere.position[0]) ** 2 + (particle.position[2] - stationary_sphere.position[2]) ** 2 < 0.5:
                self.stationary_spheres.remove(stationary_sphere)
                return

        closest_sphere = self.stationary_spheres[0]
        self.stationary_spheres[0].assigned=True
        for stationary_sphere in self.stationary_spheres:
            if distance(particle.position, stationary_sphere.position) < distance(particle.position, closest_sphere.position) and stationary_sphere.assigned==False:
                closest_sphere = stationary_sphere
                stationary_sphere.assigned=True

        direction = [(closest_sphere.position[i] - particle.position[i]) for i in range(3)]
        direction_length = sum(map(lambda x: x ** 2, direction)) ** 0.5
        direction = [x / direction_length for x in direction]

        new_position = [particle.position[i] + direction[i] * 0.04 for i in range(3)]

        for other_particle in self.particles:
            if other_particle != particle and distance(new_position, other_particle.position) < 2:
                new_position = [new_position[i] + (new_position[i] - other_particle.position[i]) * 0.04 for i in range(3)]

        particle.position = [new_position[0], particle.position[1], new_position[2]]  # Only update x and z coordinates

def run():
    swarm = PSO(4, 10)  
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        environment.handle_keys()
        environment.handle_mouse()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        environment.draw_grid(10, 1)

        for stationary_sphere in swarm.stationary_spheres:
            stationary_sphere.draw_sphere(True)

        for particle in swarm.particles:
            swarm.update(particle)
            particle.draw_particle()

        pygame.display.flip()
        clock.tick(60)

run()