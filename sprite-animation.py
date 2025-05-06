import pygame

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hoạt hình di chuyển")

# Tải các file hình ảnh
idle_frames = [
    pygame.image.load(r"knight\Idle (1).png").convert_alpha(),
    pygame.image.load(r"knight\Idle (2).png").convert_alpha(),
    pygame.image.load(r"knight\Idle (3).png").convert_alpha(),
    pygame.image.load(r"knight\Idle (4).png").convert_alpha(),
    pygame.image.load(r"knight\Idle (5).png").convert_alpha(),
]

walk_frames = [
    pygame.image.load(r"knight\Walk (1).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (2).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (3).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (4).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (5).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (6).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (7).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (8).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (9).png").convert_alpha(),
    pygame.image.load(r"knight\Walk (10).png").convert_alpha(),
]

attack_frames = [
    pygame.image.load(r"knight\Attack (1).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (2).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (3).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (4).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (5).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (6).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (7).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (8).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (9).png").convert_alpha(),
    pygame.image.load(r"knight\Attack (10).png").convert_alpha(),
]

explosion_frames = [
    pygame.image.load(r"Explosion\exp1.png").convert_alpha(),
    pygame.image.load(r"Explosion\exp2.png").convert_alpha(),
    pygame.image.load(r"Explosion\exp3.png").convert_alpha(),
    pygame.image.load(r"Explosion\exp4.png").convert_alpha(),
    pygame.image.load(r"Explosion\exp5.png").convert_alpha(),
]



# Thay đổi kích thước các frame
idle_frames = [pygame.transform.scale(frame, (int(frame.get_width() * 0.2), int(frame.get_height() * 0.2))) for frame in idle_frames]
walk_frames = [pygame.transform.scale(frame, (int(frame.get_width() * 0.2), int(frame.get_height() * 0.2))) for frame in walk_frames]
attack_frames = [pygame.transform.scale(frame, (int(frame.get_width() * 0.2), int(frame.get_height() * 0.2))) for frame in attack_frames]
# Biến cho hoạt hình
clock = pygame.time.Clock()
FPS = 60

idle_frame = 0
walk_frame = 0
attack_frame = 0
explosion_frame = 0

running = True
x_pos = WIDTH // 2
y_pos = HEIGHT // 2
speed = 5

player_mode = "idle"
exp_mode = ""

current_frame = 0

# Vòng lặp chính
while running:

    #  check currnet frame
    
    # current_frame += 1
    # if current_frame > 60:
    #     print(f"Current frame: {current_frame}")
    #     current_frame = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                player_mode = "attack"

            if event.key == pygame.K_e:
                exp_mode = "explosion"

            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT \
                 or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_mode = "walk"

        if event.type == pygame.KEYUP:
            player_mode = "idle"


    if player_mode == "walk":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x_pos += speed
        if keys[pygame.K_LEFT]:
            x_pos -= speed
        if keys[pygame.K_UP]:
            y_pos -= speed
        if keys[pygame.K_DOWN]:
            y_pos += speed    


    # Cập nhật frame hoạt hình
    screen.fill((255, 255, 255))  # Nền trắng

    if exp_mode == "explosion":
        screen.blit(explosion_frames[int(explosion_frame)], (x_pos+200, y_pos))
        explosion_frame = explosion_frame + 0.2
        if explosion_frame >= len(explosion_frames):
            explosion_frame = 0
            exp_mode = ""  # Reset chế độ nổ sau khi hoàn thành 

    if player_mode == "idle":
        screen.blit(idle_frames[int(idle_frame)], (x_pos, y_pos))
        idle_frame = idle_frame + 0.1
        if idle_frame >= len(idle_frames):
            idle_frame = 0

    if player_mode == "attack":
        screen.blit(attack_frames[int(attack_frame)], (x_pos, y_pos))
        attack_frame = attack_frame + 0.5
        if attack_frame >= len(attack_frames):
            attack_frame = 0

    if player_mode == "walk":
        screen.blit(walk_frames[int(walk_frame)], (x_pos, y_pos))
        walk_frame = walk_frame + 0.5
        if walk_frame >= len(walk_frames):
            walk_frame = 0
    
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()