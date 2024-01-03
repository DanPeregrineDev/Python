import pygame

pygame.init()

# Game window

width = 1920 / 2 #800
height = 1080 / 2 #600
title = "Tennis"
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

clock = pygame.time.Clock()

GENERAL_VELOCITY = 2
BACKGROUND = 31, 31, 31

# Player

player_file = "images/racket1.png"
speedx_player = 0
speedy_player = GENERAL_VELOCITY
player_image = pygame.image.load(player_file)
rect_player = player_image.get_rect()
rect_player.topleft = (0, 300)

# CPU

cpu_file = "images/racket2.png"
speedx_cpu = 0
speedy_cpu = GENERAL_VELOCITY
cpu_image = pygame.image.load(cpu_file)
rect_cpu = cpu_image.get_rect()
rect_cpu.topleft = ((width - 30), 300)

# Ball

ball_file = "images/ball.png"
speedx_ball = GENERAL_VELOCITY
speedy_ball = GENERAL_VELOCITY
ball_image = pygame.image.load(ball_file)
rect_ball = ball_image.get_rect()
rect_ball.topleft = ((width / 2), 300)

run = True

while run:
    # Player Logic
    rect_player = rect_player.move(speedx_player, speedy_player)

    # Ball Logic
    rect_ball = rect_ball.move(speedx_ball, speedy_ball)

    # Detect Collisions
    # Ball - Window Borders
    if rect_ball.top <= 0 or rect_ball.top + rect_ball.height > height:
        speedy_ball = speedy_ball * -1

    # Rackets - Window Borders
    if rect_player.top <= 0 or rect_player.top + rect_player.height > height:
        speedy_player = speedy_player * -1
    if rect_cpu.top <= 0 or rect_cpu.top + rect_cpu.height > height:
        speedy_cpu = speedy_cpu * -1

    # Ball - Rackets
    if rect_ball.colliderect(rect_player) or rect_ball.colliderect(rect_cpu):
        speedx_ball = speedx_ball * -1

    # CPU Moviment
    if rect_ball.top < rect_cpu.top:
        speedy_cpu = -GENERAL_VELOCITY
    if rect_ball.top > rect_cpu.top:
        speedy_cpu = GENERAL_VELOCITY
    rect_cpu = rect_cpu.move(speedx_cpu, speedy_cpu)

    # Display
    window.fill(BACKGROUND)

    # Display Player
    window.blit(player_image, rect_player)

    # Display CPU
    window.blit(cpu_image, rect_cpu)

    # Display Ball
    window.blit(ball_image, rect_ball)

    # Update
    pygame.display.flip()

    clock.tick(120)

    # Read Inputs
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            # Up key
            if event.key == pygame.K_UP:
                speedy_player = -GENERAL_VELOCITY

            # Down key
            if event.key == pygame.K_DOWN:
                speedy_player = GENERAL_VELOCITY

            # Esc key
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run = False

        # If window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False