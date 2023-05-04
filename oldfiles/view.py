import pygame
from player import Players
#from ball import Ball
from ball1 import Ball
#from ball1 import drawMoveBall
#from ball import updateBall
import random

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300
screenColor = (132, 192, 17)
lineColor = (255, 255, 255)
ballColor = (145, 224, 255)
leftColor = (255, 255, 255)
rightColor = (0, 0, 0)
fieldCenter = FIELD_WIDTH, FIELD_LENGTH = 300, 150
midlineBegin = wid1, len1 = 300, 0
midlineEnd = wid2, len2 = 300, 600
surface = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Foosball")
image_surface = pygame.image.load("soccer-ball-realistic-png.png")
arg_img = pygame.image.load("argentinaflag.png")
image_surface = pygame.transform.scale(image_surface, (15,15))
ball_speed = x_speed, y_speed = 1, 1
players2 = [Players("goalie2"), Players("def3"), Players("def4")]
players3 = [Players("mid3"), Players("mid4"), Players("att2")]
players = [Players("goalie1"), Players("def1"), Players("def2")]
players1 = [Players("mid1"), Players("mid2"), Players("att1")]
ball = Ball()
x_speed = random.randint(2,4)
y_speed = random.randint(-4,4)
#ball.drawBall(surface)
# ball = Ball(ballColor, 20, 20)
# ball.rect.x = 295
# ball.rect.y = 145
# all_sprites_list = pygame.sprite.Group()
# all_sprites_list.add(ball)
# all_sprites_list.add(players)
# all_sprites_list.add(players1)
# all_sprites_list.add(players2)
# all_sprites_list.add(players3)
#ball = Ball()
#ball.drawBall(surface)

# ballColor = (145, 224, 255)
# ballSize = ballWidth, ballHeight = 10,10
# ballPos = ballX, ballY = 295, 145
# ballSpeed = .5
# SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300
# ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
# x_speed = random.randint(2,4)
# y_speed = random.randint(-4,4)

#ball = Ball(surface, "soccer-ball-realistic-png.png")
#ball_group = pygame.sprite.Group()
#ball_group.add(ball)




#gL = goalieL()
def drawBALLS():
    ball.drawBall(surface)

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

def up():
    global y_speed
    global x_speed
    surface.fill(screenColor)
    pygame.draw.circle(surface, lineColor, fieldCenter, 15, 1)
    pygame.draw.line(surface, lineColor, midlineBegin, midlineEnd)
    leftGoalBox()
    rightGoalBox()
    leftTeam()
    rightTeam()
    drawBALLS()
    ball.moveBall(surface)
    #ball.rect.clamp_ip(surface.get_rect())
    #ball.rect.move_ip(x_speed, y_speed)
    #ball.moveBall(surface)
    #all_sprites_list.update(surface)
    # if ball.rect.x>=600:
    #     ball.velocity[0] = -ball.velocity[0]
    # if ball.rect.x<=0:
    #     ball.velocity[0] = -ball.velocity[0]
    # if ball.rect.y>300:
    #     ball.velocity[1] = -ball.velocity[1]
    # if ball.rect.y<0:
    #     ball.velocity[1] = -ball.velocity[1]

    #if pygame.sprite.collide_mask(ball, players) or pygame.sprite.collide_mask(ball, players1) or pygame.sprite.collide_mask(ball, players2) or pygame.sprite.collide_mask(ball, players3):
     # ball.bounce()


    #all_sprites_list.draw(surface)
    #pygame.draw.rect(surface, ballColor, ball)
    #ball.clamp_ip(surface.get_rect())
    #ball.move_ip(x_speed, y_speed)
    #ball.moveBall(surface)
    # if ball.right >= SCREEN_WIDTH or ball.left <= 0:
    #     x_speed *= -1
    # if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0:
    #     y_speed *= -1
    #if players2.rect.colliderect(ball):
        #print("hit")
    #ball.moveBall(surface)
    #pygame.draw.circle(surface, ballColor, fieldCenter, 8)
    #ball_group.draw(surface)
    #ball_group.update(surface)
    #surface.blit(image_surface, [293,143])
    # ball = Ball(leftColor,10,10)
    # ball.rect.x = 150
    # ball.rect.y = 150
    #
    # all_sprites_list = pygame.sprite.Group()
    # all_sprites_list.add(ball)
    # if ball.rect.x>=690:
    #     ball.velocity[0] = -ball.velocity[0]
    # if ball.rect.x<=0:
    #     ball.velocity[0] = -ball.velocity[0]
    # if ball.rect.y>490:
    #     ball.velocity[1] = -ball.velocity[1]
    # if ball.rect.y<0:
    #     ball.velocity[1] = -ball.velocity[1]
    #updateBall(ball, surface)
    #ball.move_ip(x_speed, y_speed)
    #surface.blit(image_surface, fieldCenter)
    #MOUSE_POS = pygame.mouse.get_pos()
    #surface.blit(image_surface, MOUSE_POS)
    pygame.display.update()

def leftTeam():
    # [goalPos, def1Pos, def2Pos, mid1Pos, mid2Pos, attPos]
    # goalPos = goalX, goalY = 15, 150
    # leftGoalie = pygame.draw.circle(surface, leftColor, goalPos, 15)
    # def1Pos = def1X, def1Y = 100, 75
    # def2Pos = def2X, def2Y = 100, 225
    # LeftDef1 = pygame.draw.circle(surface, leftColor, def1Pos, 15)
    # LeftDef2 = pygame.draw.circle(surface, leftColor, def2Pos, 15)
    # mid1Pos = mid1X, mid1Y = 275, 75
    # mid2Pos = mid2X, mid2Y = 275, 225
    # LeftMid1 = pygame.draw.circle(surface, leftColor, mid1Pos, 15)
    # LeftMid2 = pygame.draw.circle(surface, leftColor, mid2Pos, 15)
    # attPos = attX, attY = 450, 150
    # LeftAtt = pygame.draw.circle(surface, leftColor, attPos, 15)

    #print("GOIN THRU THE LLEFT TEAM")
    for x in players1:
        #print(x.type)

        x.handle_L1keys(surface, leftColor)
        x.drawIt(surface, leftColor)

    for x in players:

        x.handle_L2keys(surface, leftColor)
        x.drawIt(surface, leftColor)


    #
    # for player in players:
    #     player.draw(surface)
        # draw playere


    #pygame.display.update()

def rightTeam():
    #print("GOIN THRU THE LLEFT TEAM")
    for x in players2:
        #print(x.type)
        x.handle_Rkeys(surface, rightColor)
        x.drawIt(surface, rightColor)

    for x in players3:

        x.handle_R2keys(surface, rightColor)
        x.drawIt(surface, rightColor)

    # defPos = defX, defY = 585, 150
    # pygame.draw.circle(surface, rightColor, defPos, 15)
    # def1Pos = def1X, def1Y = 500, 75
    # def2Pos = def2X, def2Y = 500, 225
    # pygame.draw.circle(surface, rightColor, def1Pos, 15)
    # pygame.draw.circle(surface, rightColor, def2Pos, 15)
    # mid1Pos = mid1X, mid1Y = 325, 75
    # mid2Pos = mid2X, mid2Y = 325, 225
    # pygame.draw.circle(surface, rightColor, mid1Pos, 15)
    # pygame.draw.circle(surface, rightColor, mid2Pos, 15)
    # attPos = attX, attY = 150, 150
    # pygame.draw.circle(surface, rightColor, attPos, 15)

#def upball(position):
     #surface.blit(image_surface, position)
     #pygame.display.update()
