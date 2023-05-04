import pygame
import random
BLACK = (0,0,0)
#ballColor = (255, 165, 0)

#randy = random.randint(1,2)
#ballSpeed = 1
ballPos = ballX, ballY = 300, 150
#self.velocity.x = 0
#velocity.
class Ball(pygame.sprite.Sprite):

    def __init__ (self, color, width, height):
        super().__init__()
        #self.image = pygame.Surface([width, height])
        #self.image.fill(BLACK)
        #self.rect = self.image.get_rect()
        #self.image.set_colorkey(BLACK)
        # self.image = pygame.image.load(picture_path)
        # self.image = pygame.transform.scale(self.image, (15,15))
        # self.rect = self.image.get_rect()
        # self.rect.center = ballPos
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)


        pygame.draw.rect(self.image, color, [0, 0, width, height])
        #[]
        #self.image = pygame.transform.scale(self.image, (15,15))
        #surface.blit(self.image, [self.ballX,self.ballY])
        self.velocity = [random.randint(2,4), random.randint(-4,4)]
        #self.velocity.x = 1
        #self.rect.x += self.velocity[0]
        #self.rect.y += self.velocity[1]
        #self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()

    def update(self, surface):
        #self.rect.x += self.velocity.x
        #if self.rect.x >= 0 or self.rect.x >= 600:
            #self.velocity = 0
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


        # if self.rect.x <= 0 or self.rect.x >= 600:
        #     self.rect.x *= -1
        # else:
        #     self.rect.x += self.velocity[0]
        # if self.rect.y <= 0 or self.rect.y >= 300:
        #     self.rect.y *= -1
        # else:
        #     self.rect.y += self.velocity[1]
        #self.clamp_ip(surface.get_rect())
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)


#def updateBall(self, surface):
    #self.ballX += self.velocity[0]
    #self.ballY += self.velocity[1]
    #surface.blit(self.image, [self.ballX,self.ballY])
