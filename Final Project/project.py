import pygame
import os
import random


WIDTH = 800
HEIGHT = 600
FPS = 30
SIZE = 40
VELOCITY = 5

BLACK = (31, 31, 31)
RED = (186, 4, 0)
GREEN = (138, 193, 73)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

icon = pygame.image.load(os.path.join("Assets", "icon.png"))
background = pygame.image.load(os.path.join("Assets", "background.png"))
menu_background = pygame.image.load(os.path.join("Assets", "menu_backround.png"))
snake_head_image = pygame.image.load(os.path.join("Assets", "snake_head.png"))
food_image = pygame.image.load(os.path.join("Assets", "food.png"))
play_button = pygame.image.load(os.path.join("Assets", "play_button.png"))
play_button_pressed = pygame.image.load(os.path.join("Assets", "play_button_pressed.png"))
quit_button = pygame.image.load(os.path.join("Assets", "quit_button.png"))
quit_button_pressed = pygame.image.load(os.path.join("Assets", "quit_button_pressed.png"))
title = pygame.image.load(os.path.join("Assets", "title.png"))

pygame.display.set_caption("Snake Game")
pygame.display.set_icon(icon)


def draw_window(snake, food):
    screen.blit(background, (0, 0))
    screen.blit(snake.head_image, (snake.rect.x, snake.rect.y))
    screen.blit(food.image, (food.x, food.y))
    pygame.display.flip()



class Snake:
    def __init__(self):
        self.direction = "up"
        self.new_direction = ""
        self.head_rotation = 0
        self.head_image = snake_head_image
        self.rect = pygame.Rect(400, 300, SIZE, SIZE)

    def move_snake(self):
        self.head_image = pygame.transform.rotate(snake_head_image, self.head_rotation)
        match self.direction:
            case "left":
                self.rect.x -= VELOCITY
            case "right":
                self.rect.x += VELOCITY
            case "up":
                self.rect.y -= VELOCITY
            case "down":
                self.rect.y += VELOCITY

    def modify_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.new_direction = "up"
        if keys[pygame.K_s]:
            self.new_direction = "down"
        if keys[pygame.K_a]:
            self.new_direction = "left"
        if keys[pygame.K_d]:
            self.new_direction = "right"

        if not self.rect.x % SIZE and not self.rect.y % SIZE:
            if self.new_direction == "left" and self.direction != "right":
                self.head_rotation = 90
                self.direction = "left"
            if self.new_direction == "right" and self.direction != "left":
                self.head_rotation = 270
                self.direction = "right"
            if self.new_direction == "up" and self.direction != "down":
                self.head_rotation = 0
                self.direction = "up"
            if self.new_direction == "down" and self.direction != "up":
                self.head_rotation = 180
                self.direction = "down"

class Food:
    def __init__(self):
        self.Xpos = [x for x in range(WIDTH) if not x % 40]
        self.Ypos = [y for y in range(HEIGHT) if not y % 40]
        self.image = food_image
        self.x = random.choice(self.Xpos)
        self.y = random.choice(self.Ypos)

    def place_food(self):
        self.x = random.choice(self.Xpos)
        self.y = random.choice(self.Ypos)



def create_button(x,y, button, button_pressed, func):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    screen.blit(button, (x, y))

    if pos[0] > x and pos[0] < x + 300 and pos[1] > y and pos[1] < y + 150:
       screen.blit(button_pressed, (x, y))
       if click[0] == 1:
         func()

def start_game():
    run = True
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        snake.modify_direction()
        snake.move_snake()
        if snake.rect.x == food.x and snake.rect.y == food.y:
            food.place_food()

        draw_window(snake, food)

    pygame.quit()


def start_menu():
    run = True
    while run:
        screen.blit(menu_background, (0, 0))
        screen.blit(title, (WIDTH/2 - 300, 50))
        create_button(WIDTH/2 - 150, HEIGHT/2 - 75, play_button, play_button_pressed, start_game)
        create_button(WIDTH/2 - 150, HEIGHT/2 + 75, quit_button, quit_button_pressed, quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


if __name__ == "__main__":
    start_menu()
