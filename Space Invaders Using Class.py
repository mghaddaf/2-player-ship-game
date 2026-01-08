import pygame
pygame.init()
WIDTH = 900
LENGTH = 600
TITLE = "2-player rocket game"
run = True
rpoints = 5
ypoints = 5
w = 1000
h = 300
ybull = []
rbull = []
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

def all_bull():
    global run
    global ypoints, rpoints
    for y_rect in ybull:
        pygame.draw.rect(screen, "yellow", y_rect)
        y_rect.x = y_rect.x + 10
        if y_rect.colliderect(r_rocket.rect):
            rpoints = rpoints - 1
            ybull.remove(y_rect)
    for r_rect in rbull:
        pygame.draw.rect(screen, "red", r_rect)
        r_rect.x = r_rect.x - 10
        if r_rect.colliderect(y_rocket.rect):
            ypoints = ypoints - 1
            rbull.remove(r_rect)
    if ypoints <= 0:
        font3 = pygame.font.SysFont("Comic Sans MC", 100)
        message3 = font3.render(("Red Wins!"), True, "white")
        screen.blit(message3, (310, 150))
        pygame.display.update()
        pygame.time.delay(2000)
        run = False
    if rpoints <= 0:
        font4 = pygame.font.SysFont("Comic Sans MC", 100)
        message4 = font4.render(("Yellow Wins!"), True, "white")
        screen.blit(message4, (250, 150))
        pygame.display.update()
        pygame.time.delay(2000)
        run = False

        

while run:
    screen.blit(space, (0, 0))
    pygame.draw.line(screen, "black", (450, 0), (450, 600), 5)
    rocket_group.draw(screen)
    all_bull()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                y_rect = pygame.Rect((y_rocket.rect.x, y_rocket.rect.y), (20, 5))
                y_rect.center = y_rocket.rect.center
                ybull.append(y_rect)
            if event.key == pygame.K_RSHIFT:
                r_rect = pygame.Rect((r_rocket.rect.x, r_rocket.rect.y), (20, 5))
                r_rect.center = r_rocket.rect.center
                rbull.append(r_rect)
        if event.type == pygame.QUIT:
            run = False
    Kb = pygame.key.get_pressed()
    if Kb[pygame.K_DOWN]:
        r_rocket.rect.y = r_rocket.rect.y + 5
    if Kb[pygame.K_UP]:
        r_rocket.rect.y = r_rocket.rect.y - 5
    if Kb[pygame.K_LEFT]:
        r_rocket.rect.x = r_rocket.rect.x - 5
    if Kb[pygame.K_RIGHT]:
        r_rocket.rect.x = r_rocket.rect.x + 5

    if Kb[pygame.K_s]:
        y_rocket.rect.y = y_rocket.rect.y + 5
    if Kb[pygame.K_w]:
        y_rocket.rect.y = y_rocket.rect.y - 5
    if Kb[pygame.K_a]:
        y_rocket.rect.x = y_rocket.rect.x - 5
    if Kb[pygame.K_d]:
        y_rocket.rect.x = y_rocket.rect.x + 5
    
    if y_rocket.rect.right > 450:
        y_rocket.rect.right = 450
    if y_rocket.rect.left < 0:
        y_rocket.rect.left = 0
    if y_rocket.rect.top <= 0:
        y_rocket.rect.top = 0
    if y_rocket.rect.bottom > 600:
        y_rocket.rect.bottom = 600
        
    if r_rocket.rect.right > 900:
        r_rocket.rect.right = 900
    if r_rocket.rect.left < 450:
        r_rocket.rect.left = 450
    if r_rocket.rect.top <= 0:
        r_rocket.rect.top = 0
    if r_rocket.rect.bottom > 600:
        r_rocket.rect.bottom = 600
    
    font1 = pygame.font.SysFont("Comic Sans MC", 45)
    message1 = font1.render(("Yellow lives = " + str(ypoints)), True, "white")
    screen.blit(message1, (10, 25))
    font2 = pygame.font.SysFont("Comic Sans MC", 45)
    message2 = font2.render(("Red lives = " + str(rpoints)), True, "white") 
    screen.blit(message2, (650, 25))



    pygame.display.update()