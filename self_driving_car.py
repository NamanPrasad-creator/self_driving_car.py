# Import the pygame library
import pygame

# Initialize pygame
pygame.init()

# Create a window with specified width and height
window = pygame.display.set_mode((1200, 400))

# Load the track image and car image
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')

# Scale the car image to the desired size
car = pygame.transform.scale(car, (30, 60))

# Set the starting position for the car
car_x = 155
car_y = 300

# Define the focal distance for the camera
focal_dis = 25

# Set initial camera offsets
cam_x_offset = 0
cam_y_offset = 0

# Set the initial driving direction
direction = 'up'

# Control for the drive loop
drive = True

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Start the main driving loop
while drive:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False  # Exit the loop if the window is closed

    # Set the frame rate to 60 frames per second
    clock.tick(60)

    # Calculate the camera's position relative to the car
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15

    # Get pixel colors in different directions to detect road boundaries
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]

    # Print color values (for debugging purposes)
    print(up_px, right_px, down_px)

    # Change direction based on pixel color values
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)

    # Move the car based on the current direction if the road is clear
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2

    # Draw the track and car on the window
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))

    # Draw a green circle to represent the camera point
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)

    # Update the display with all changes
    pygame.display.update()
