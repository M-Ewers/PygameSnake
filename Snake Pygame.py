import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis = pygame.display.set_mode((600, 400), pygame.RESIZABLE)

pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

surface = pygame.display.get_surface()
dis_width = surface.get_width()
dis_height = surface.get_height()

font_style = pygame.font.SysFont("microsoftsansserif", 25)
score_font = pygame.font.SysFont("microsoftsansserif", 20)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

# sets a font and location for a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])

# sets a font and location for a message that appears underneath message()
def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3.1, dis_height / 2])

# This is the opening screen that plays before the game starts
def gameStart():
    game_start = True
    while game_start:
        dis.fill(black)
        message("Let's Play Snake!", white)
        message2("Press enter to Play!", white)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_start = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        # Game over Screen
        while game_close:
            dis.fill(black)
            message("You Lost! ", white)
            message2("C - Play Again", white)
            mesg = font_style.render("Q - Quit", True, white)
            dis.blit(mesg, [dis_width / 3.1, dis_height / 1.7])
            Your_score((Length_of_snake - 1) * 100)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
# Handles the controls ------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
# End of control Block -------------------------------------------------
        # This sets a game over for going out of bounds
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # this sets the movement for the snake
        x1 += x1_change
        y1 += y1_change
        # fills the screen black and sets the food on there the first time
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        # this creates the snake head and assigns it as the first object to the snake_list
        snake_head = [x1, y1]
        snake_List.append(snake_head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                del snake_List[-1]

        our_snake(snake_block, snake_List)
        Your_score((Length_of_snake - 1) * 100)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameStart()
gameLoop()