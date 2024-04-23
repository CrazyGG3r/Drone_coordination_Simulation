import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the main display surface
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Define square properties
square_size = 50  # Size of the square (width and height)
square_color = (255, 0, 0)  # Red color

# Create a surface for the square
square_surface = pygame.Surface((square_size, square_size))
square_surface.fill(square_color)

# Define the square's initial position on the screen
square_x, square_y = 100, 100

# Define the initial rotation angle
angle = 0

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Rotate the square surface
    rotated_square_surface = pygame.transform.rotate(square_surface, angle)
    
    # Calculate the top-left position to blit the rotated surface
    # to keep it centered around the original position
    rect = rotated_square_surface.get_rect(center=(square_x + square_size // 2, square_y + square_size // 2))
    top_left_x = rect.x
    top_left_y = rect.y
    
    # Blit the rotated square surface onto the main display surface at the calculated position
    screen.blit(rotated_square_surface, (top_left_x, top_left_y))
    
    # Increment the angle to rotate the square
    angle += 1
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(60)  # Set the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
