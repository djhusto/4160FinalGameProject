import pygame
import random

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300
screenColor = (132, 192, 17)
lineColor = (255, 255, 255)
ballColor = (145, 224, 255)
leftColor = (255, 255, 255)
rightColor = (0, 0, 0)
moveDist = .5
ballColor = (145, 224, 255)
ballSize = ballWidth, ballHeight = 10,10
ballPos = ballX, ballY = 295, 145
ballSpeed = .5
fieldCenter = FIELD_WIDTH, FIELD_LENGTH = 300, 150
midlineBegin = wid1, len1 = 300, 0
midlineEnd = wid2, len2 = 300, 600
rectSpeed = 1
surface = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("FoosPong")
playerSize = width, height = 20, 20
Lgoalie = pygame.Rect(5, 140, width, height)
LdefOne = pygame.Rect(100, 75, width, height)
LdefTwo = pygame.Rect(100, 225, width, height)
LmidOne = pygame.Rect(275, 75, width, height)
LmidTwo = pygame.Rect(275, 225, width, height)
Latt = pygame.Rect(450, 150, width, height)
Rgoalie = pygame.Rect(575, 140, width, height)
RdefOne = pygame.Rect(500, 75, width, height)
RdefTwo = pygame.Rect(500, 225, width, height)
RmidOne = pygame.Rect(325, 75, width, height)
RmidTwo = pygame.Rect(325, 225, width, height)
Ratt = pygame.Rect(150, 150, width, height)
Ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
x_speed = random.randint(2,4)
y_speed = random.randint(-4,4)
playerA_score = 0
playerB_score = 0
darkyeller = (139, 128, 0)
textScore = str(playerA_score) + " Score " + str(playerB_score)
start_time = 0



pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(textScore, True, darkyeller)
text_Rect = text.get_rect()
text_Rect.center = (600//2, 50)

def drawPlayers():
    pygame.draw.rect(surface, leftColor, Lgoalie)
    pygame.draw.rect(surface, leftColor, LdefOne)
    pygame.draw.rect(surface, leftColor, LdefTwo)
    pygame.draw.rect(surface, leftColor, LmidOne)
    pygame.draw.rect(surface, leftColor, LmidTwo)
    pygame.draw.rect(surface, leftColor, Latt)
    pygame.draw.rect(surface, rightColor, Rgoalie)
    pygame.draw.rect(surface, rightColor, RdefOne)
    pygame.draw.rect(surface, rightColor, RdefTwo)
    pygame.draw.rect(surface, rightColor, RmidOne)
    pygame.draw.rect(surface, rightColor, RmidTwo)
    pygame.draw.rect(surface, rightColor, Ratt)

def drawBall():
    pygame.draw.rect(surface, ballColor, Ball)

def moveLMLA():
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
        if LmidTwo.bottom >= 300:
            return
        LmidOne.move_ip(0, rectSpeed)
        LmidTwo.move_ip(0, rectSpeed)
        Latt.move_ip(0, rectSpeed)
    if key[pygame.K_w]:
        if LmidOne.top <= 0:
            return
        LmidOne.move_ip(0, -rectSpeed)
        LmidTwo.move_ip(0, -rectSpeed)
        Latt.move_ip(0, -rectSpeed)

def moveLGLD():
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if LdefTwo.bottom >= 300:
            return
        Lgoalie.move_ip(0, rectSpeed)
        LdefOne.move_ip(0, rectSpeed)
        LdefTwo.move_ip(0, rectSpeed)
    if key[pygame.K_q]:
        if LdefOne.top <= 0:
            return
        Lgoalie.move_ip(0, -rectSpeed)
        LdefOne.move_ip(0, -rectSpeed)
        LdefTwo.move_ip(0, -rectSpeed)

def moveRMRA():
    key = pygame.key.get_pressed()
    if key[pygame.K_PERIOD]:
        if RmidTwo.bottom >= 300:
            return
        RmidOne.move_ip(0, rectSpeed)
        RmidTwo.move_ip(0, rectSpeed)
        Ratt.move_ip(0, rectSpeed)
    if key[pygame.K_SEMICOLON]:
        if RmidOne.top <= 0:
            return
        RmidOne.move_ip(0, -rectSpeed)
        RmidTwo.move_ip(0, -rectSpeed)
        Ratt.move_ip(0, -rectSpeed)

def moveRGRD():
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if RdefTwo.bottom >= 300:
            return
        Rgoalie.move_ip(0, rectSpeed)
        RdefOne.move_ip(0, rectSpeed)
        RdefTwo.move_ip(0, rectSpeed)
    if key[pygame.K_UP]:
        if RdefOne.top <= 0:
            return
        Rgoalie.move_ip(0, -rectSpeed)
        RdefOne.move_ip(0, -rectSpeed)
        RdefTwo.move_ip(0, -rectSpeed)

def leftGoalBox():
    goal1LineB = wid3, len3 = 0, 115
    goal1LineE = wid4, len4 = 50, 115
    goal2LineB = wid5, len5 = 0, 185
    goal2LineE = wid6, len6 = 50, 185
    goal3LineB = wid5, len5 = 50, 115
    goal3LineE = wid6, len6 = 50, 185
    pygame.draw.line(surface, lineColor, goal1LineB, goal1LineE)
    pygame.draw.line(surface, lineColor, goal2LineB, goal2LineE)
    pygame.draw.line(surface, lineColor, goal3LineB, goal3LineE)
def rightGoalBox():
    goal1LineB = wid3, len3 = 600, 115
    goal1LineE = wid4, len4 = 550, 115
    goal2LineB = wid5, len5 = 600, 185
    goal2LineE = wid6, len6 = 550, 185
    goal3LineB = wid5, len5 = 550, 115
    goal3LineE = wid6, len6 = 550, 185
    pygame.draw.line(surface, lineColor, goal1LineB, goal1LineE)
    pygame.draw.line(surface, lineColor, goal2LineB, goal2LineE)
    pygame.draw.line(surface, lineColor, goal3LineB, goal3LineE)

def gameReset():
    Ball.update(ballX, ballY, ballWidth, ballHeight)
    x_speed = random.randint(2,4)
    y_speed = random.randint(-4,4)
    Ball.move_ip(x_speed, y_speed)
    Lgoalie.update(5, 140, width, height)
    LdefOne.update(100, 75, width, height)
    LdefTwo.update(100, 225, width, height)
    LmidOne.update(275, 75, width, height)
    LmidTwo.update(275, 225, width, height)
    Latt.update(450, 150, width, height)
    Rgoalie.update(575, 140, width, height)
    RdefOne.update(500, 75, width, height)
    RdefTwo.update(500, 225, width, height)
    RmidOne.update(325, 75, width, height)
    RmidTwo.update(325, 225, width, height)
    Ratt.update(150, 150, width, height)
    pygame.display.update()

def shrinkies():
    Ball.scale_by_ip(.5)

def nextGame():
    global x_speed
    global y_speed
    #BallX = 0
    #BallY = 0

    # key = pygame.key.get_pressed()
    # if key[pygame.K_SPACE]:
    #     x_speed = random.randint(2,4)
    #     y_speed = random.randint(-4,4)
    # Ball.move_ip(x_speed, y_speed)
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            x_speed = random.randint(2,4)
            y_speed = random.randint(-4,4)
            Ball.move_ip(x_speed, y_speed)
            pygame.display.update()



while True:
    for event in pygame.event.get():  #Listening for Events (key press, times, etc)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    start_time = 0
    start_time = pygame.time.get_ticks()
    surface.fill(screenColor)
    pygame.draw.circle(surface, lineColor, fieldCenter, 15, 1)
    pygame.draw.line(surface, lineColor, midlineBegin, midlineEnd)
    leftGoalBox()
    rightGoalBox()
    moveLGLD()
    moveLMLA()
    moveRGRD()
    moveRMRA()
    drawPlayers()
    drawBall()
    Ball.move_ip(x_speed, y_speed)
    if Ball.bottom >= SCREEN_HEIGHT or Ball.top <= 0:
        y_speed *= -1
    if Ball.right >= SCREEN_WIDTH or Ball.left <= 0:
        x_speed *= -1
    if Ball.colliderect(Rgoalie) or Ball.colliderect(RdefOne) or Ball.colliderect(RdefTwo) or Ball.colliderect(RmidOne) or Ball.colliderect(RmidTwo) or Ball.colliderect(Ratt):
        x_speed *= -1
    if Ball.colliderect(Lgoalie) or Ball.colliderect(LdefOne) or Ball.colliderect(LdefTwo) or Ball.colliderect(LmidOne) or Ball.colliderect(LmidTwo) or Ball.colliderect(Latt):
        x_speed *= -1
    if Ball.right >= SCREEN_WIDTH and Ball.top <= 185 and Ball.bottom >= 115:
        playerA_score += 1
        textScore = str(playerA_score) + " Score " + str(playerB_score)
        x_speed = 0
        y_speed = 0
        pygame.time.wait(2000)
        gameReset()
        nextGame()
        x_speed = random.randint(2,4)
        y_speed = random.randint(-4,4)
        Ball.move_ip(x_speed, y_speed)
    if Ball.left <= 0 and Ball.top <= 185 and Ball.bottom >= 115:
        playerB_score += 1
        textScore = str(playerA_score) + " Score " + str(playerB_score)
        x_speed = 0
        y_speed = 0
        pygame.time.wait(2000)
        gameReset()
        nextGame()
        x_speed = random.randint(2,4)
        y_speed = random.randint(-4,4)
        Ball.move_ip(x_speed, y_speed)

    # if start_time >= 30000:
    #     Ball.inflate_ip(-1,-1)
    #     start_time = 0
    # if pygame.time.wait(5000):
    #     x_speed *= 2
    #     y_speed *= 2
    surface.blit(text, text_Rect)
    text = font.render(textScore, True, darkyeller)
    pygame.display.update()
