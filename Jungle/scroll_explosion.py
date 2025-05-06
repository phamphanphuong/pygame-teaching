import pygame
import math
pygame.init()

clock = pygame.time.Clock()
FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 547

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrolling Background")

#  load images
# explosion
explosion_time = pygame.time.get_ticks()
explosion_speed = 10
explosion_index = 0
explosion_cooldown = 1000

explosion_images = [pygame.image.load(f"Assets/Explosion/exp{i}.png").convert_alpha() for i in range(1, 6)]
def explosion(x, y):
    global explosion_index, explosion_time
    now = pygame.time.get_ticks()
    if now - explosion_time > explosion_cooldown:
        explosion_index += 1
        if explosion_index >= len(explosion_images):
            explosion_index = 0
    screen.blit(explosion_images[explosion_index], (x, y))

    print(explosion_index)

# background
bg = pygame.image.load("Assets/Bg/sky.png").convert()
bg = pygame.transform.scale_by(bg, 0.5)
bg_width, bg_height = bg.get_size()
bg_rect = bg.get_rect()

scroll = 0
scroll_speed = 0.5
tiles = math.ceil(SCREEN_WIDTH / bg.get_width()) + 1

def drawBackground():
    for i in range(tiles):
        screen.blit(bg, (bg_width * i - scroll, 0))
        pygame.draw.rect(screen, (0, 0, 0), bg_rect, 1)
   
# health bar
def drawHealthBar(ratio):
    width = 200
    height = 20
    x = 10
    y = 10

    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.draw.rect(screen, GREEN, (x , y , width * ratio, height))
    # pygame.draw.rect(screen, (0, 0, 0), (x + 2, y + 2, width - 4, height - 4), 1)

# Player
playerImage = pygame.image.load("Assets\Character\sprites\idle.gif")
def drawPlayer(x, y):
    screen.blit(playerImage, (x,y))

run = True
while run:
    clock.tick(FPS)  # Control the frame rate

     #  Draw the background images
    drawBackground()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # explosion
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x, y = pygame.mouse.get_pos()
                # start explosion at mouse position
                screen.blit(explosion_images[explosion_index], (x, y))
                explosion_index += 1
                if explosion_index >= len(explosion_images):
                    explosion_index = 0

                

    # scroll += scroll_speed
    # if scroll > bg_width:
    #     scroll = 0

   

  
    
    # Draw the health bar
    drawHealthBar(0.8)

    # Draw the player
    drawPlayer(300, 300)
    
    pygame.display.flip()  # Update the display

pygame.quit()