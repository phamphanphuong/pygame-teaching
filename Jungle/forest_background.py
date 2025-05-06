import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 432



# variables
scroll = 0
bgSpeed = 5
maxWidthCount = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Forest Randam")

bg_images = []
for i in range(1, 6):
    bg_images.append(pygame.image.load(f"Assets\Bg\plx-{i}.png").convert_alpha())
bg_width = bg_images[0].get_width()
    
def drawBackground():
    for i in range(0,maxWidthCount):
        speed = 1
        for bg in bg_images:
            screen.blit(bg, (bg_width * i  - scroll* speed, 0))
            speed += 0.1

ground_image = pygame.image.load("Assets\Bg\ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_width = ground_image.get_width()

def drawGround():
    for i in range(0,maxWidthCount*2):
        screen.blit(ground_image, (ground_width * i - scroll, SCREEN_HEIGHT - ground_image.get_height()))

run = True
while run:
    clock.tick(FPS)  # Control the frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_RIGHT] and scroll < bg_width * (maxWidthCount-1):
        scroll += bgSpeed
    if keys[pygame.K_LEFT] and scroll > 0:
        scroll -= bgSpeed
   

    # Draw the background images
    drawBackground()
    drawGround()

    # screen.fill((173, 216, 230))  
    # for i in range(5):
    #     screen.blit(bg_images[4], (bg_width*i - scroll, 0))
    
    
    pygame.display.flip()  # Update the display

pygame.quit()

