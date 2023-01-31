import pygame
import time
import sys
import math


class Player:
    def __init__(self):
        self.life = True
        self.shop = 5
        self.X = 100
        self.Y = 100
        self.corner = 0
        self.directionX = 0
        self.directionY = 0


class Wall:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


class Vector:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        

class Mapp:
    width: int
    height: int

    def start(self):
        screen.fill((23, 242, 81))
        font = pygame.font.SysFont('couriernew', 40)
        text = font.render(str('Start'), True, (255, 192, 64))
        screen.blit(text, (200, 250))

    def end(self):
        screen.fill((78, 72, 255))
        font = pygame.font.SysFont('couriernew', 40)
        text = font.render(str('End'), True, (253, 4, 46))
        screen.blit(text, (200, 250))


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
screen_mapp = pygame.display.set_mode((500, 500))
mapp = Mapp()
mapp.start()
pygame.display.update()
time.sleep(1)
player = Player()
corner = 0
mass_vector = [Vector(player.X, player.Y)]
mass_mapp = ['.....###',
             '######.#',
             '#......#',
             '#..#...#',
             '########']
mass_wall = []
height = 0
for row in mass_mapp:
    width = 0
    for letter in row:
        if letter == '#':
            mass_wall.append(Wall(width, height))
            print(width, ' ', height)
        width += 83.33
    height += 83.33
number = 0
while number < 1050:
    mass_vector.append(Vector(player.X, player.Y))
    number += 1
pi = math.pi / 6
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                corner += -0.1
            if event.key == pygame.K_d:
                corner += 0.1
            if event.key == pygame.K_w:
                player.X = player.X + 5 * math.cos(corner)
                player.Y = player.Y + 5 * math.sin(corner)
            if event.key == pygame.K_s:
                player.X = player.X - 5 * math.cos(corner)
                player.Y = player.Y - 5 * math.sin(corner)
            if event.key == pygame.K_SPACE:
                print(player.X, ',', player.Y)
    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (0, 0, 255), (0, 0, 500, 250))
    pygame.draw.rect(screen, (6, 118, 6), (0, 255, 500, 255))
    vector_count = 0
    corner_vector = 0
    width = 0
    for vector in mass_vector:
        modul = 1
        flag = False
        while modul < 10:
            for wall in mass_wall:
                if vector.Y > wall.Y and \
                vector.Y < wall.Y + 83.333 and \
                vector.X > wall.X and \
                vector.X < wall.X + 83.333:
                    pygame.draw.rect(screen, (135, 212, 255), (width, 250*(1 - 1/modul * 3), 4.7619, 250*(1 + 1/modul * 3) - 250*(1 - 1/modul * 3)))
                    flag = True
                    break
                if flag:
                    break
            vector.X = vector.X + modul * math.cos(corner + pi - corner_vector)
            vector.Y = vector.Y + modul * math.sin(corner + pi - corner_vector)
            modul += 0.1
        vector.X = player.X
        vector.Y = player.Y
        mass_vector[vector_count] = vector
        vector_count += 1
        corner_vector += 0.001
        width += 0.476190476
    pygame.draw.line(screen, (0, 0, 0), (240, 250), (260, 250))
    pygame.draw.line(screen, (0, 0, 0), (250, 240), (250, 260))
    pygame.display.update()
    clock.tick(60)
