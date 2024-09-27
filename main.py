import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
IMAGE_WIDTH, IMAGE_HEIGHT = 300, 300
BG_COLOR = (58, 58, 58)  # Grey background

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My First Game Screen")

# Load and scale the image
image = pygame.image.load('your_image.png')  # Replace 'your_image.png' with the path to your image file
image = pygame.transform.scale(image, (IMAGE_WIDTH, IMAGE_HEIGHT))

# Calculate the position to center the image
image_x = (WINDOW_WIDTH - IMAGE_WIDTH) // 2
image_y = (WINDOW_HEIGHT - IMAGE_HEIGHT) // 2

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background color
    screen.fill(BG_COLOR)

    # Draw the image at the calculated position
    screen.blit(image, (image_x, image_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
