import pygame

moveDist = .5
rectSize = rectWidth, rectHeight = 20, 20
BLACK = (0,0,0)

class Players(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()
        self.type = type
        self.x = 0
        self.y = 0

        self.image = pygame.Surface([rectWidth, rectHeight])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        if type == "goalie1":
            self.x = 15
            self.y = 150
        if type == "goalie2":
            self.x = 585
            self.y = 150
        if type == "def1":
            self.x = 100
            self.y = 75
        if type == "def2":
            self.x = 100
            self.y = 225
        if type == "def3":
            self.x = 500
            self.y = 75
        if type == "def4":
            self.x = 500
            self.y = 225
        if type == "mid1":
            self.x = 275
            self.y = 75
        if type == "mid2":
            self.x = 275
            self.y = 225
        if type == "att1":
            self.x = 450
            self.y = 150
        if type == "mid3":
            self.x = 325
            self.y = 75
        if type == "mid4":
            self.x = 325
            self.y = 225
        if type == "att2":
            self.x = 150
            self.y = 150

        self.rect = self.image.get_rect()
        
    def drawIt(self, surface, color):
        self.pos = self.x, self.y
        #pygame.draw.circle(surface, color, self.pos, 15)
        pygame.draw.rect(surface, color, (self.x,self.y,rectWidth,rectHeight))

        #i = 2
        #pygame.draw.circle(surface, leftColor, goalPos, 15)

    #def goalieL(self):
    #    self.x = 30
    #    self.y = 100

    # def update(self):
    #     if upkeypressed:
    #         x = x + speed
    def handle_Rkeys(self, surface, color):
        key = pygame.key.get_pressed()
        dist = moveDist
        #if self.y < 0:
            #self.y = 0
        if key[pygame.K_DOWN]:
            #$if self.y == 0:
            #print("pressing key down")
            self.y += dist
        elif key[pygame.K_UP]:
            #print("pressing key up")
            self.y -= dist
        self.pos = self.x, self.y
        #pygame.draw.circle(surface, color, self.pos, 15)
        pygame.draw.rect(surface, color, (self.x,self.y,rectWidth,rectHeight))

    def handle_R2keys(self, surface, color):
        key = pygame.key.get_pressed()
        dist = moveDist
        if key[pygame.K_PERIOD]:
            #print("pressing key down")
            self.y += dist
        elif key[pygame.K_SEMICOLON]:
            #print("pressing key up")
            self.y -= dist
        self.pos = self.x, self.y
        #pygame.draw.circle(surface, color, self.pos, 15)
        pygame.draw.rect(surface, color, (self.x,self.y,rectWidth,rectHeight))

    def handle_L1keys(self, surface, color):
        key = pygame.key.get_pressed()
        dist = moveDist
        if key[pygame.K_s]:
            #print("pressing key down")
            self.y += dist
        elif key[pygame.K_w]:
            #print("pressing key up")
            self.y -= dist
        self.pos = self.x, self.y
        #pygame.draw.circle(surface, color, self.pos, 15)
        pygame.draw.rect(surface, color, (self.x,self.y,rectWidth,rectHeight))

    def handle_L2keys(self, surface, color):
        key = pygame.key.get_pressed()
        dist = moveDist
        if key[pygame.K_a]:
            #print("pressing key down")
            self.y += dist
        elif key[pygame.K_q]:
            #print("pressing key up")
            self.y -= dist
        self.pos = self.x, self.y
        #pygame.draw.circle(surface, color, self.pos, 15)
        pygame.draw.rect(surface, color, (self.x,self.y,rectWidth,rectHeight))
