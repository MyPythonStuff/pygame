import pygame
import os
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

xsize = 600
ysize = 500
pygame.init()
screen = pygame.display.set_mode((xsize, ysize))
done = False
is_blue = True
color = (0, 128, 255)
x = 30
y = 30
clock = pygame.time.Clock()
image = pygame.image.load('004.png')
image2 = pygame.image.load('resizecandy.jpg')


def poke(x, y):
    screen.blit(image, (x, y))


def candy():
    screen.blit(image2, (xsize*.85, ysize*.85))


def evolve():
    global image
    image = pygame.image.load('005.png')


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if is_blue:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            evolve()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    screen.fill((0, 0, 0))

    candy()
    poke(x, y)
    if x == xsize*.85 or y == ysize*.85:
        evolve()


    #pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(60)
