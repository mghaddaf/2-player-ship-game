import pygame
WIDTH = 900
LENGTH = 600
TITLE = "2-player rocket game"
run = True
yellow_rocket = pygame.image.load(r"Pygame Developer\Images\yellow rocket.png")
red_rocket = pygame.image.load(r"Pygame Developer\Images\red rocket.png")
space = pygame.image.load(r"Pygame Developer\Images\space2.png")
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("2-player rocket game!")
class Rocket(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        super().__init__()
        self.image = pygame.transform.scale(image, (50, 50))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
y_rocket = Rocket(yellow_rocket, 225, 300, 90)
r_rocket = Rocket(red_rocket, 675, 300, 270)
rocket_group = pygame.sprite.Group()
rocket_group.add(r_rocket)
rocket_group.add(y_rocket)

while run:
    screen.blit(space, (0, 0))
    pygame.draw.line(screen, "black", (450, 0), (450, 600), 5)
    rocket_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Kb = pygame.key.get_pressed()
    if Kb[pygame.K_DOWN]:
        r_rocket.rect.y = r_rocket.rect.y + 1
    if Kb[pygame.K_UP]:
        r_rocket.rect.y = r_rocket.rect.y - 1
    if Kb[pygame.K_LEFT]:
        r_rocket.rect.x = r_rocket.rect.x - 1
    if Kb[pygame.K_RIGHT]:
        r_rocket.rect.x = r_rocket.rect.x + 1

    if Kb[pygame.K_s]:
        y_rocket.rect.y = y_rocket.rect.y + 1
    if Kb[pygame.K_w]:
        y_rocket.rect.y = y_rocket.rect.y - 1
    if Kb[pygame.K_a]:
        y_rocket.rect.x = y_rocket.rect.x - 1
    if Kb[pygame.K_d]:
        y_rocket.rect.x = y_rocket.rect.x + 1
    pygame.display.update()