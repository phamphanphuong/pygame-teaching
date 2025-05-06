import pygame
import random
import os
import math
import time
import sys


# Initialize Pygame
pygame.init()
# Set up the screen
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Phương Đẹp Trai")
pygame.display.set_icon(pygame.image.load(r"knight\Idle (1).png").convert_alpha())
# Set up the clock
clock = pygame.time.Clock()
# Set up the font
font = pygame.font.Font(None, 36)
# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Set up the background
background = pygame.image.load(r"background.png").convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
# Set up the player
player_image = pygame.image.load(r"knight\Idle (1).png").convert_alpha()
player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * 0.2), int(player_image.get_height() * 0.2)))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)
# Set up the player speed
player_speed = 5
# Set up the player direction
player_direction = "right"
# Set up the player state
player_state = "idle"
# Set up the player animation frames
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

