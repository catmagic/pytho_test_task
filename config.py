import pygame
import time
import random


 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
snake_block = 10
snake_speed = 15

user_name  = ""
state="enteredName"
need_quit = False 


x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

snake_Head=[]
    
def eatFood():
    print("~nya~")
    return x1 == foodx and y1 == foody
    
