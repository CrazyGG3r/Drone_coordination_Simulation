from re import A
import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, radians

font = ['assets/fonts/f1.ttf','assets/fonts/f2.ttf']

class Text:
    def __init__(self, coords, font_size, color, text, fonts=0):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.x = coords[0]
        self.y = coords[1]
        self.font = pygame.font.Font(font[fonts], font_size)
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


def dummy(ac = "None"):
    print("Clicked somehting",random.randint(0,10))


class button:
    def __init__(self, coords, w, h, color,padding, butt_text, function = dummy):
        self.x = coords[0]
        self.y = coords[1]
        self.pad_x = self.x + padding[0]
        self.pad_y = self.y + padding[1]
        self.width = w
        self.height = h
        self.NotHovercolor = color
        self.Hovercolor = []
        for n, a in enumerate(self.NotHovercolor):
            # a = 255 - a
            a -= 50 
            if a <= -1:
                a *= -1
            if a>255:
               a = a -255
            if a == 0:
                continue
            self.Hovercolor.append(a)
        self.Hovercolor = tuple(self.Hovercolor)
        print(self.Hovercolor)
        self.text = None
        self.hover = False
        self.text = butt_text
        self.text.update_coords((self.pad_x,self.pad_y))
        self.action = function
        self.isClicked = False

    def draw(self, screen,):
        if self.hover:
            pygame.draw.rect(screen, self.Hovercolor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.NotHovercolor, (self.x, self.y, self.width, self.height))
        self.text.draw(screen)
        
class CreateDrone:
    def __init__(self, radius, position, speed, destination, name, color):
        self.radius = radius
        self.position = position
        self.speed = speed
        self.des = destination
        self.name = str(name)
        self.color = color
        self.fontColor = (0,190,190)
    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)
       
        name_surface = pygame.font.SysFont(None, 20).render(self.name, True, self.fontColor)
        window.blit(name_surface, (self.position[0] - self.radius, self.position[1] + self.radius + 10))

    
def limit_value(value, min_value, max_value):
    return max(min_value, min(max_value, value))


class CreateEnvironment:
    def __init__(self, screen_center):
        self.screen_center = screen_center
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(screen_center)
        
    # Function to draw grid on xy and xz planes
    def draw_grid(self, size, step):  # Added 'self' as the first parameter
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
    def setup_lighting(self):  # Added 'self' as the first parameter
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
        
        glClearColor(0.0, 0.0, 0.0, 1.0)  # Clear color (black)
        glColor3f(0.0, 1.0, 0.0)  # Drawing color (green)
        
    # Function to handle mouse input for camera control
    def handle_mouse(self):
        sensitivity = 0.1
        mouse_x, mouse_y = pygame.mouse.get_pos()
        delta_x = mouse_x - self.screen_center[0]
        delta_y = mouse_y - self.screen_center[1]

        glRotatef(delta_y * sensitivity, 1, 0, 0)  # Rotate around the x-axis
        glRotatef(delta_x * sensitivity, 0, 1, 0)  # Rotate around the y-axis

        pygame.mouse.set_pos(self.screen_center)
        
    # Handles key press for movement and rotation
    def handle_keys(self):  # Added 'self' as the first parameter
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
    
            
class CreateSpheres:
    def __init__(self,radius,slices,position):
        self.radius=radius
        self.slices=slices
        self.position=position
        self.quadric = gluNewQuadric()
            
    def draw_sphere(self, is_stationary):
        glPushMatrix()
        glTranslatef(*self.position)
        
        if is_stationary:
            glColor3f(1.0, 0.0, 0.0)  # Red color for stationary spheres
        else:
            glColor3f(0.0, 1.0, 0.0)  # Green color for moving spheres
        
        gluSphere(self.quadric, self.radius, self.slices, self.slices)
        glPopMatrix()

def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** 0.5

class CreateParticles:
    def __init__(self, radius, slices, position):
        self.radius = radius
        self.slices = slices
        self.position = position

    def draw_particle(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0.0, 1.0, 0.0)  # Set particle color to green
        quadric = gluNewQuadric()
        gluSphere(quadric, self.radius, self.slices, self.slices)  # Draw sphere using gluSphere
        glPopMatrix()





    
    