import pygame
import random

config = {
    "head_size": 10,
    "head_color": (255, 0, 0),
    "body_space": 20,
    "body_size": 8,
    "body_color": (255, 255, 255),
    "body_start_length": 2,
    "case_size": 10,
    "case_color": (0, 255, 0),
    "case_max": 2
}

def motion(screen):
    global snake_add
    if snake_add:
        snake_add -= 1
    else:
        snake_body.pop(0)
    x, y = snake_body[-1]
    x += movement[0] * config["body_space"]
    y += movement[1] * config["body_space"]
    snake_body.append((x, y))
    for xy in snake_body[:-1]:
        pygame.draw.circle(screen, config["body_color"], xy, config["body_size"])
    pygame.draw.circle(screen, config["head_color"], snake_body[-1], config["head_size"])
    food()
    eating()

def self_intersect():
    xh, yh = snake_body[-1]
    for x, y in snake_body[:-1]:
        if x == xh and y == yh:
            return True
    return False

def food():
    if not case or len(case) < config["case_max"]:
        if random.random() < 0.1:
            x = random.randrange(20, 480, config["body_space"])
            y = random.randrange(20, 480, config["body_space"])
            case.append((x, y))

def eating():
    global snake_add
    xh, yh = snake_body[-1]
    for i, (x, y) in enumerate(case):
        if xh - config["head_size"] <= x <= xh + config["head_size"] and \
           yh - config["head_size"] <= y <= yh + config["head_size"]:
            snake_add += 1
            case.pop(i)

def lose(screen):
    global case
    case = []
    font = pygame.font.Font(None, 50)
    textwon1 = font.render('YOU LOSE!', True, (110, 255, 100))
    screen.blit(textwon1, (168, 220))
    textnewgame1 = font.render('NEW GAME', True, (100, 255, 100))
    screen.blit(textnewgame1, (165, 270))
    pygame.draw.rect(screen, (0, 0, 0), (155, 260, 215, 50))
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos[0], event.pos[1])
        if 380 > event.pos[0] > 155 and 290 > event.pos[1] > 260:
            new_game()

def new_game():
    global snake_body, case, movement, snake_add
    snake_body = [(250 - i, 250) for i in range(config["body_start_length"])][::-1]
    movement = (1, 0)
    case = []
    snake_add = 0

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    new_game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not movement[1]:
                    movement = (0, -1)
                elif event.key == pygame.K_DOWN and not movement[1]:
                    movement = (0, 1)
                elif event.key == pygame.K_RIGHT and not movement[0]:
                    movement = (1, 0)
                elif event.key == pygame.K_LEFT and not movement[0]:
                    movement = (-1, 0)

        screen.fill((0, 0, 0))

        for xy in case:
            pygame.draw.circle(screen, config["case_color"], xy, config["case_size"])

        x, y = snake_body[-1]
        if 20 <= x <= 480 and 20 <= y <= 480 and not self_intersect():
            motion(screen)
        else:
            lose(screen)

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()
