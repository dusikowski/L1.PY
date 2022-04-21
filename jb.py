
from typing_extensions import Self
import random
import pygame

class jablko():
    def __init__(self):
        self.kolor=(18,27,11)
        self.applePostion=(20,20)
    def setPosition(self,x,y):
        self.applePostion=(x,y)
    def getPosition(self):
        return self.applePostion
    def randomPostion(self):
        xApple=random.randint(0,9)*40+20
        yApple=random.randint(0,9)*40+20
        self.setPosition(xApple,yApple)
def drawApple(self,OknoGry):
        pygame.draw.circle(OknoGry,self.kolor,(self.applePostion[0],self.applePostion[1]),20)
