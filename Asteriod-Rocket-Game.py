#from _typeshed import Self
import time
import pygame
import random
from pygame.constants import RLEACCEL


# define and import the controlls
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)

#constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# initialize the player class by extending the pygame.sprite.Sprite
# The surface drawn on the screen (box) is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # make the player the rocket png
        self.surf = pygame.image.load("rocket.png").convert()
        # rotate and scale the image
        self.surf = pygame.transform.rotate(self.surf,270)
        self.surf = pygame.transform.scale(self.surf,(75,50))

        self.surf.set_colorkey((0,0,0),RLEACCEL)
        # create the player surface length and width of 75 by 25
        #self.surf = pygame.Surface((75,25))

        # fill the screen black RGB
        #self.surf.fill((255,255,255))
        # get the coordinates set to .rect
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        # define the movement based on the keys pressed using pressed_keys
        # use move ip to move the player based on its' current pos
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
            
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # need to make sure the player does not extend past the window
        # using the coordinates properties
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
#end  Player


# define a class for the enemy using the pygame Sprite feature
class Enemy(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Enemy, self).__init__()
        # load the image
        self.surf = pygame.image.load("missel.png").convert()
        # roate and scale the missle image
        self.surf = pygame.transform.rotate(self.surf, 90)
        self.surf = pygame.transform.scale(self.surf,((60,30)))

        self.surf.set_colorkey((0,0,0),RLEACCEL)
        # make the enemy 20 by 10 length and width
        #self.surf = pygame.Surface((20,10))
        # make the color RGB
        #self.surf.fill((239,20,2))

        # set the starting position
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH +100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        # set the speed
        self.speed = random.randint(5,20)

    def update(self):
        # move the enemy right to left 
        self.rect.move_ip(-self.speed,0)
        # if the position is less than 0 kill the enemy obj
        if self.rect.right < 0:
            self.kill()

#end Enemy


# background image class
class Background(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Background,self).__init__() 
        backgroundImageList = ["asteroid.png","comet.png","rock.png","asteroid.png","asteroid.png","asteroid.png"]
        backgroundImage = backgroundImageList[random.randint(0,len(backgroundImageList)-1)]

        self.surf = pygame.image.load(backgroundImage).convert()

        size = [random.randint(50,200),random.randint(50,200)]
        rotation = random.randint(0,360)

        self.surf = pygame.transform.scale(self.surf,((size[0],size[1])))

        if backgroundImage == 'asteroid.png':
            self.surf = pygame.transform.rotate(self.surf, rotation)
        else:
            self.surf = pygame.transform.rotate(self.surf, 320)

        self.surf.set_colorkey((0,0,0),RLEACCEL)

        #starting pos
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
                random.randint(0,SCREEN_HEIGHT)
            )
        )
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right < 0:
            self.kill()
#end Background

def StartScreen():
    #pygame.init()
    #clock = pygame.time.Clock()
    #create the screen obj
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ADDASTEROID = pygame.USEREVENT+2
    pygame.time.set_timer(ADDASTEROID,1000)
    asteriods = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()

    # define the RGB value for white,
    #  green, blue colour .
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    
    
    # set the pygame window name
    pygame.display.set_caption('Asteriod Belt Adventure')
    
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font1 = pygame.font.SysFont('sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 32)
    font2 = pygame.font.Font('pixelFont.ttf', 24)
    
    # create a text surface object,
    # on which text is drawn on it.
    title = font1.render('Asteriod Belt Adventure', True, white, blue)
    subtitle = font2.render("Press Space to Start", True, green)
    
    # create a rectangular object for the
    # text surface object
    textRect = title.get_rect()
    subRect = subtitle.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (SCREEN_WIDTH/ 2, SCREEN_HEIGHT/ 2)
    subRect.center = ((SCREEN_WIDTH)/ 2, (SCREEN_HEIGHT+(SCREEN_HEIGHT/2))/ 2)

    #set up main loop
    runflag = True

    while runflag:
        for event in pygame.event.get():
            # did a user hit a key
            if event.type ==KEYDOWN:
                # is it the esc key
                if event.key == K_ESCAPE:
                    runflag = False
                elif event.key == K_SPACE:
                    runflag = False
            # clicking the window close button listener
            elif event.type == QUIT:
                runflag = pygame.quit()
            

            elif event.type == ADDASTEROID:
                new_asteriod = Background()
                asteriods.add(new_asteriod)
                all_sprites.add(new_asteriod)

        
            pressed_keys = pygame.key.get_pressed()
            

            #enemies.update()
        asteriods.update()

                
        screen.fill((255,255,255)) # fill the screen white

                #create a surface and send the length and width
                #surf = pygame.Surface((50,50))

                #Give the surface a color to seperate it from the background
        screen.fill((0,0,0)) #black surface

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

    
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        screen.blit(title, textRect)
        screen.blit(subtitle, subRect)
    
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
    
        # Draws the surface object to the screen.
        pygame.display.update()
        
        pygame.display.flip()

        


        clock.tick(30)
    return

# Main Driver
# Initialize pygame
pygame.init()

clock = pygame.time.Clock()
#create the screen obj

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
StartScreen()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,250)

ADDASTEROID = pygame.USEREVENT+2
pygame.time.set_timer(ADDASTEROID,1000)

#call an instance of the player class
player = Player()

enemies = pygame.sprite.Group()

asteriods = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

test = True     

#set up main loop
runflag = True

while runflag:
    for event in pygame.event.get():
        # did a user hit a key
        if event.type == KEYDOWN:
            # is it the esc key
            if event.key == K_ESCAPE:
                runflag = False
        # clicking the window close button listener
        elif event.type == QUIT:
            runflag = False
        
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDASTEROID:
            new_asteriod = Background()
            asteriods.add(new_asteriod)
            all_sprites.add(new_asteriod)

    
    pressed_keys = pygame.key.get_pressed()
    
    player.update(pressed_keys)

    enemies.update()
    asteriods.update()

    #create a surface and send the length and width
    surf = pygame.Surface((50,50))

    #Give the surface a color to seperate it from the background
    screen.fill((0,0,0)) #black surface

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player,enemies):

        player.kill()
        runflag = False

    rect = surf.get_rect()

    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT-surf.get_height())/2
    )


    #draw the surface at the center of the screen
    screen.blit(player.surf, player.rect)



    pygame.display.flip()

    clock.tick(30)

#while end


