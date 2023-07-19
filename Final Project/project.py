import pygame
import os
import random


WIDTH = 800
HEIGHT = 800
FPS = 30
CELL_SIZE = 40
CELL_NUMBER = 20


class Snake:
    def __init__(self):
        self.direction = pygame.math.Vector2(0, -1)
        self.new = False
        self.body = [
            pygame.math.Vector2(10, 10),
            pygame.math.Vector2(10, 11),
            pygame.math.Vector2(10, 12),
        ]
        

    def move_snake(self):
        if self.new:
            body_copy = self.body[:]
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new = False

    def draw_snake(self):
        self.update_head_image()
        self.update_tail_image()
        for i, part in enumerate(self.body):
            part_rect = pygame.Rect(
                int(part.x * CELL_SIZE), int(part.y * CELL_SIZE), CELL_SIZE, CELL_SIZE
            )
        
            if i == 0 :
                screen.blit(self.head, part_rect)
            elif i == len(self.body) - 1:
                screen.blit(self.tail, part_rect)
            else:
                prev_part = self.body[i - 1] - part
                next_part = self.body[i + 1] - part

                if prev_part.x == next_part.x:
                    self.mid = body_vert
                elif prev_part.y == next_part.y:
                    self.mid = body_linear
                else:
                    if prev_part.x == -1 and next_part.y == -1 or prev_part.y == -1 and next_part.x == -1:
                        self.mid = corner_ul
                    if prev_part.x == -1 and next_part.y == 1 or prev_part.y == 1 and next_part.x == -1:
                        self.mid = corner_dl
                    if prev_part.x == 1 and next_part.y == -1 or prev_part.y == -1 and next_part.x == 1:
                        self.mid = corner_ur
                    if prev_part.x == 1 and next_part.y == 1 or prev_part.y == 1 and next_part.x == 1:
                        self.mid = corner_dr

                screen.blit(self.mid, part_rect)


    def update_head_image(self):
        relation = self.body[1] - self.body[0]
        if relation == pygame.math.Vector2(1, 0):
            self.head = head_right
        elif relation == pygame.math.Vector2(-1, 0):
            self.head = head_left
        elif relation == pygame.math.Vector2(0, 1):
            self.head = head_up
        elif relation == pygame.math.Vector2(0, -1):
            self.head = head_down

    def update_tail_image(self):
        relation = self.body[-2] - self.body[-1]
        if relation == pygame.math.Vector2(1, 0):
            self.tail = tail_right
        elif relation == pygame.math.Vector2(-1, 0):
            self.tail = tail_left
        elif relation == pygame.math.Vector2(0, 1):
            self.tail = tail_down
        elif relation == pygame.math.Vector2(0, -1):
            self.tail = tail_up



    def add(self):
        self.new = True


class Food:
    def __init__(self):
        self.image = food_image
        self.randomize()

    def draw_food(self):
        food_rect = pygame.Rect(
            int(self.pos.x * CELL_SIZE),
            int(self.pos.y * CELL_SIZE),
            CELL_SIZE,
            CELL_SIZE,
        )
        screen.blit(self.image, food_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.gameover = False

    def update_movement(self):
        self.snake.move_snake()
        self.colisions()
        self.fail()

    def draw_elements(self):
        screen.blit(background, (0, 0))
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()

    def colisions(self):
        if self.snake.body[0] == self.food.pos:
            self.food.randomize()
            self.snake.add()
        for pos in self.snake.body:
            if self.food.pos == pos:
                self.food.randomize()

    def fail(self):
        if (
            self.snake.body[0].x < 0
            or self.snake.body[0].x > CELL_NUMBER - 1
            or self.snake.body[0].y < 0
            or self.snake.body[0].y > CELL_NUMBER - 1
        ):
            self.gameover = True

        for pos in self.snake.body[1:]:
            if self.snake.body[0] == pos:
                self.gameover = True

    def draw_score(self):
        self.score = len(self.snake.body) - 3 
        score_surface_black = score_font.render(f"Score: {self.score}", False, (0, 0, 0))
        score_surface_white = score_font.render(f"Score: {self.score}", False, (255, 255, 255))
        screen.blit(score_surface_black, (23, 23))
        screen.blit(score_surface_white, (20, 20))


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

icon = pygame.image.load(os.path.join("Assets", "icon.png"))
background = pygame.image.load(os.path.join("Assets", "background.png"))
menu_background = pygame.image.load(os.path.join("Assets", "menu_backround.png"))
food_image = pygame.image.load(os.path.join("Assets", "food.png"))
play_button = pygame.image.load(os.path.join("Assets", "play_button.png"))
play_button_pressed = pygame.image.load(
    os.path.join("Assets", "play_button_pressed.png")
)
quit_button = pygame.image.load(os.path.join("Assets", "quit_button.png"))
quit_button_pressed = pygame.image.load(
    os.path.join("Assets", "quit_button_pressed.png")
)
retry_button = pygame.image.load(os.path.join("Assets", "retry_button.png"))
retry_button_pressed = pygame.image.load(
    os.path.join("Assets", "retry_button_pressed.png")
)

title = pygame.image.load(os.path.join("Assets", "title.png"))
over = pygame.image.load(os.path.join("Assets", "over.png"))

head_up = pygame.image.load(os.path.join("Assets", "head_up.png"))
head_down = pygame.image.load(os.path.join("Assets", "head_down.png"))
head_left = pygame.image.load(os.path.join("Assets", "head_left.png"))
head_right = pygame.image.load(os.path.join("Assets", "head_right.png"))

tail_up = pygame.image.load(os.path.join("Assets", "tail_up.png"))
tail_down = pygame.image.load(os.path.join("Assets", "tail_down.png"))
tail_left = pygame.image.load(os.path.join("Assets", "tail_left.png"))
tail_right = pygame.image.load(os.path.join("Assets", "tail_right.png"))

body_vert = pygame.image.load(os.path.join("Assets", "body_vert.png"))
body_linear = pygame.image.load(os.path.join("Assets", "body_linear.png"))

corner_ur = pygame.image.load(os.path.join("Assets", "corner_ur.png"))
corner_ul = pygame.image.load(os.path.join("Assets", "corner_ul.png"))
corner_dr = pygame.image.load(os.path.join("Assets", "corner_dr.png"))
corner_dl = pygame.image.load(os.path.join("Assets", "corner_dl.png"))

score_font = pygame.font.Font(os.path.join("Fonts", "PublicPixel-z84yD.ttf"), 25)

pygame.display.set_caption("Snake Game")
pygame.display.set_icon(icon)



def create_button(x, y, button, button_pressed, func):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    screen.blit(button, (x, y))

    if pos[0] > x and pos[0] < x + 300 and pos[1] > y and pos[1] < y + 150:
        screen.blit(button_pressed, (x, y))
        if click[0] == 1:
            func()


def end_game(score):
    run = True

    while run:
        screen.blit(menu_background, (0, 0))
        screen.blit(over, (WIDTH / 2 - 300, 50))

        score_surface_black = score_font.render(f"Your score was: {score}", False, (0, 0, 0))
        score_surface_white = score_font.render(f"Your score was: {score}", False, (255, 255, 255))
        screen.blit(score_surface_black, (188, 228))
        screen.blit(score_surface_white, (185, 225))

        create_button(
            WIDTH / 2 - 150,
            HEIGHT / 2 - 75,
            retry_button,
            retry_button_pressed,
            start_game,
        )
        create_button(
            WIDTH / 2 - 150, HEIGHT / 2 + 75, quit_button, quit_button_pressed, quit
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()
    quit()


def start_game():
    run = True
    main_game = Main()

    screen_update = pygame.USEREVENT
    pygame.time.set_timer(screen_update, 150)
    

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == screen_update:
                main_game.update_movement()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and main_game.snake.direction.y != 1:
                    main_game.snake.direction = pygame.math.Vector2(0, -1)
                if event.key == pygame.K_s and main_game.snake.direction.y != -1:
                    main_game.snake.direction = pygame.math.Vector2(0, 1)
                if event.key == pygame.K_d and main_game.snake.direction.x != -1:
                    main_game.snake.direction = pygame.math.Vector2(1, 0)
                if event.key == pygame.K_a and main_game.snake.direction.x != 1:
                    main_game.snake.direction = pygame.math.Vector2(-1, 0)
        if main_game.gameover:
            end_game(main_game.score)
        main_game.draw_elements()

        pygame.display.flip()

    pygame.quit()
    quit()


def main():
    run = True

    while run:
        screen.blit(menu_background, (0, 0))
        screen.blit(title, (WIDTH / 2 - 300, 50))
        create_button(
            WIDTH / 2 - 150,
            HEIGHT / 2 - 75,
            play_button,
            play_button_pressed,
            start_game,
        )
        create_button(
            WIDTH / 2 - 150, HEIGHT / 2 + 75, quit_button, quit_button_pressed, quit
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
