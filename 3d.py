import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, radians
import random

# Function to draw grid on xy and xz planes
def draw_grid(size, step):
    glBegin(GL_LINES)
    for x in range(-size, size + 1, step):
        glVertex3f(x, 0, -size)
        glVertex3f(x, 0, size)
    for z in range(-size, size + 1, step):
        glVertex3f(-size, 0, z)
        glVertex3f(size, 0, z)
    glEnd()

    glBegin(GL_LINES)
    for x in range(-size, size + 1, step):
        glVertex3f(x, -size, 0)
        glVertex3f(x, size, 0)
    for y in range(-size, size + 1, step):
        glVertex3f(-size, y, 0)
        glVertex3f(size, y, 0)
    glEnd()

# Function to handle lighting
def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    light_ambient = [0.2, 0.2, 0.2, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]
    light_position = [2.0, 2.0, 2.0, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

# Function to handle mouse input for camera control
def handle_mouse():
    sensitivity = 0.1
    mouse_x, mouse_y = pygame.mouse.get_pos()
    delta_x = mouse_x - screen_center[0]
    delta_y = mouse_y - screen_center[1]

    glRotatef(delta_y * sensitivity, 1, 0, 0)  # Rotate around the x-axis
    glRotatef(delta_x * sensitivity, 0, 1, 0)  # Rotate around the y-axis

    pygame.mouse.set_pos(screen_center)

def handle_keys():
    # Handles key press for movement and rotation
    keys = pygame.key.get_pressed()
    move_speed = 0.1
    rotate_speed = 1

    if keys[K_w]:
        glTranslatef(0, 0, move_speed)
    if keys[K_s]:
        glTranslatef(0, 0, -move_speed)
    if keys[K_a]:
        glTranslatef(move_speed, 0, 0)
    if keys[K_d]:
        glTranslatef(-move_speed, 0, 0)
    if keys[K_q]:
        glTranslatef(0, move_speed, 0)
    if keys[K_e]:
        glTranslatef(0, -move_speed, 0)

# Function to draw a solid sphere
def draw_sphere(quadric, radius, slices, position):
    glPushMatrix()
    glTranslatef(*position)
    gluSphere(quadric, radius, slices, slices)
    glPopMatrix()

# Function to calculate the distance between two points
def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** 0.5

def main():
    # Initialize Pygame and OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, -1.0, -10.0)

    # Set up lighting
    setup_lighting()
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Clear color (black)
    glColor3f(0.0, 1.0, 0.0)  # Drawing color (green)

    clock = pygame.time.Clock()

    # Define screen center for mouse re-centering
    global screen_center
    screen_center = (display[0] // 2, display[1] // 2)

    # Hide the mouse cursor and center it
    pygame.mouse.set_visible(False)
    pygame.mouse.set_pos(screen_center)

    # Define GLUquadric object for solid sphere
    sphere_quadric = gluNewQuadric()

    # Define properties for moving drones
    num_drones = 9
    drones = [{"radius": 0.5, "slices": 100, "position": (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))} for i in range(num_drones)]

    # Define properties for the stationary sphere at coordinates (10, 10, 10)
    stationary_sphere = {"radius": 1, "slices": 100, "position": (8, 8, 8)}

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        handle_keys()
        handle_mouse()  # Handle mouse input for camera control
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the grid
        draw_grid(10, 1)

        # Update and draw moving drones
        for drone in drones:
            # Calculate the direction towards the stationary sphere
            direction = [(stationary_sphere["position"][i] - drone["position"][i]) for i in range(3)]
            # Normalize the direction vector
            direction_length = sum(map(lambda x: x ** 2, direction)) ** 0.5
            direction = [x / direction_length for x in direction]
            # Update the position towards the stationary sphere
            new_position = [drone["position"][i] + direction[i] * 0.04 for i in range(3)]

            # Check for collisions with other drones
            for other_drone in drones:
                if other_drone != drone and distance(new_position, other_drone["position"]) < 2:
                    # Move away from the other drone
                    new_position = [new_position[i] + (new_position[i] - other_drone["position"][i]) * 0.04 for i in range(3)]

            # Update the drone's position
            drone["position"] = new_position

            # Draw the moving solid sphere (drone)
            draw_sphere(sphere_quadric, drone["radius"], drone["slices"], drone["position"])

        # Draw the stationary solid sphere at (10, 10, 10)
        draw_sphere(sphere_quadric, stationary_sphere["radius"], stationary_sphere["slices"], stationary_sphere["position"])

        # Update the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
