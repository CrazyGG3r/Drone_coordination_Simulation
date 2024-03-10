import pygame
import sys

pygame.init()

# Set initial window size
window_width =1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Resizable Window")

# Define colors
WHITE = (0,0,0)




# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Fill the window with white color
    window.fill(WHITE)

    # Draw here...

    pygame.display.flip()

pygame.quit()
sys.exit()
