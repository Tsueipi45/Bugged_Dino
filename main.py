import sys
import pygame
import random
import os

os.chdir("C:\\Workplace\\PYgame\\Dino")

#settings
FPS = 120
WIDTH = 500
HEIGHT = 300

START_X = 100
START_Y = 283

#colour(r,g,b)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

# 初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("小恐龍BUG版")

#load data
player_img =  pygame.image.load(os.path.join("Data","Player.png")).convert()
player_run_img_1 =  pygame.image.load(os.path.join("Data","Player_1.png")).convert()
player_run_img_2 =  pygame.image.load(os.path.join("Data","Player_2.png")).convert()
cactus_img_1 =  pygame.image.load(os.path.join("Data","Cactus_1.png")).convert()
cactus_img_2 =  pygame.image.load(os.path.join("Data","Cactus_2.png")).convert()
pterosaur_img_1 =  pygame.image.load(os.path.join("Data","Pterosaur_1.png")).convert()
pterosaur_img_2 =  pygame.image.load(os.path.join("Data","Pterosaur_2.png")).convert()
ground_img = pygame.image.load(os.path.join("Data","Ground.png")).convert()
cloud_img = pygame.image.load(os.path.join("Data","Cloud.png")).convert()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def draw_init():
    draw_text(screen, "Press any button to start", 32, WIDTH/2, HEIGHT/4)

    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                waiting = False
                return False

def restart():
    draw_text(screen, "You died. Press any button to restart", 32, WIDTH/2, HEIGHT/4)

    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                python = sys.executable
                os.execl(python, python, * sys.argv)

#classes
all_sprites = pygame.sprite.Group()

#ground
class Ground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.bottom = 300

ground = Ground()
all_sprites.add(ground)

#cloud
class Cloud(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cloud_img
        self.rect = self.image.get_rect()
        self.rect.left = random.randrange(WIDTH,WIDTH+500)
        self.rect.bottom = random.randrange(20,140)
    
    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.left = random.randrange(WIDTH,WIDTH+200)
            self.rect.bottom = random.randrange(20,140)


for i in range(6):
    cloud = Cloud()
    all_sprites.add(cloud)

runtime = 0

#player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = START_X
        self.rect.bottom = START_Y

    def update(self):

        global runtime
        runtime = runtime +1

        if runtime % 2 == 0:
            self.image = player_run_img_1
        else:
            self.image = player_run_img_2
        
        key_pressed = pygame.key.get_pressed()
    
        #up
        if key_pressed[pygame.K_SPACE]:
            self.image = player_img
            self.rect.y -= 13

        if key_pressed[pygame.K_UP]:
            self.image = player_img
            self.rect.y -= 13

        if key_pressed[pygame.K_SPACE] and key_pressed[pygame.K_UP]:
            self.rect.y += 13
            
        #down
        if key_pressed[pygame.K_DOWN]:
            self.image = player_img
            self.rect.y += 10

        #momvent limits
        if self.rect.top <= 150:
            self.rect.top = 150

        if self.rect.bottom >= START_Y:
            if runtime % 2 == 0:
                self.image = player_run_img_1
            else:
                self.image = player_run_img_2           
            self.rect.bottom = START_Y

        #gravity
        self.rect.y += 2

player = Player()
all_sprites.add(player)

#cactus

cactus_speed = 2
cactus_pass = 0

cactus_img_list = [cactus_img_1,cactus_img_2]

class Cactus(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(cactus_img_list)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = START_Y+5

    def update(self):
        global cactus_speed
        global cactus_pass
        
        #move
        self.rect.x -= cactus_speed
        
        #cactus check
        if self.rect.right <= 0:

            cactus_pass += 1

            self.image = random.choice(cactus_img_list)
            self.rect = self.image.get_rect()
            self.rect.left = WIDTH
            self.rect.bottom = START_Y +5
            if cactus_pass%4 == 0:
                cactus_speed = cactus_speed + 0.2
            
cactus = Cactus()
all_sprites.add(cactus)

#pterosaur

pterosaur_speed_list = [4,6,8,10]
pterosaur_speed = random.choice(pterosaur_speed_list)

pter_spawn = pygame.USEREVENT
pygame.time.set_timer(pter_spawn, random.randrange(4,8) * 1000)

class Pterosaur(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if runtime % 2 == 0:
            self.image = pterosaur_img_1
        else:
            self.image = pterosaur_img_2
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.bottom = 200

    def update(self):
        
        global pterosaur_speed
        global pter_spawn

        pter_spawn = False
        
        if runtime % 2 == 0:
            self.image = pterosaur_img_1
        else:
            self.image = pterosaur_img_2

        #move
        self.rect.x -= pterosaur_speed
        
        #pter check
        if self.rect.right <= 0:
            self.kill()

            pterosaur_speed = random.choice(pterosaur_speed_list)
            self.rect.left = WIDTH
            self.rect.bottom = 200

pter = Pterosaur()

#score
score = []

#game
#while loop

show_init = True
show_restart = False

running = True
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        draw_init()
        show_init = False
    elif show_restart:
        restart()
        show_restart = False

    clock.tick(FPS)

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pter_spawn:
            all_sprites.add(pter)
            pter_spawn = False
            pygame.time.set_timer(pter_spawn, random.randrange(4,8) * 1000)

    #update
    all_sprites.update()

    #losing detection
    hits_1 = pygame.sprite.collide_rect(player, cactus)
    hits_2 = pygame.sprite.collide_rect(player, pter)
    if hits_1 or hits_2:
        show_restart = True
        
        

    #gain poing dection
    score.append(cactus_pass)

    #display
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen,f'Score:{score[-1]}', 22, 40, 0)

    pygame.display.update()

#stop
pygame.quit()