import pygame
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)





class addAPicture(pygame.sprite.Sprite):

    def __init__(self, filename):

        super().__init__()


        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()


pygame.init()

screen_width = 1000
screen_height = 560
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Coin Collector")


coin_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

back_img = pygame.image.load("wallpaper.jpg").convert()
back_img_pos = [0,0]

music = pygame.mixer.music.load("bgmusic.ogg")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)


for i in range(500):
    
    coin = addAPicture("ring.png")

    coin.rect.x = random.randrange(screen_width)
    coin.rect.y = random.randrange(screen_height)

    coin_list.add(coin)
    all_sprite_list.add(coin)

player = addAPicture("sonic.jpg")
all_sprite_list.add(player)


running = True
clock = pygame.time.Clock()
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(back_img, back_img_pos)

    pos = pygame.mouse.get_pos()


    player.rect.x = pos[0]
    player.rect.y = pos[1]


    coin_collected_list = pygame.sprite.spritecollide(player, coin_list, True)

    for coin in coin_collected_list:
        score += 1

        print("You have collected " + str(score) + " ring(s) so far!")

    all_sprite_list.draw(screen)


    clock.tick(60)

    pygame.display.flip()

pygame.quit()
