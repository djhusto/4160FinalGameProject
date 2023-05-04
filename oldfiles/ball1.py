import pygame
import random
ballColor = (145, 224, 255)
ballSize = ballWidth, ballHeight = 10,10
ballPos = ballX, ballY = 295, 145
ballSpeed = .5
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300

x_speed = random.randint(2,4)
y_speed = random.randint(-4,4)
class Ball(object):
    def __init__(self):
        self.x = 295
        self.y = 145
        self.rect = pygame.Rect(self.x, self.y, ballWidth, ballHeight)
        self.velocity = [random.randint(0,1),random.randint(-1,1)]

    def drawBall(self, surface):
        ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
        pygame.draw.rect(surface, ballColor, ball)

    def moveBall(self,surface):
        #global x_speed
        #global y_speed
        x_speed = random.randint(2,4)
        y_speed = random.randint(-4,4)
        self.rect = pygame.Rect(self.x, self.y, ballWidth, ballHeight)
        self.rect.clamp_ip(surface.get_rect())
        self.rect.move_ip(x_speed, y_speed)
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            x_speed *= -1
        if self.rect.bottom >= SCREEN_HEIGHT or self.rect.top <= 0:
            y_speed *= -1
        self.drawBall(surface)
