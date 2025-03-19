import pygame

import random
import loops 
import config
import display
import sql

                    
        
 
def gameLoop():
    dis.fill(white)
    if Length_of_snake>10:
        message("You win "+user_name+" your score "+str(Length_of_snake-1), green)
    else:
        message("You lose "+user_name+" your score "+str(Length_of_snake-1), red)
    pygame.display.update()
    need_exit=False
    while not need_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                need_exit = True
            if event.type == pygame.KEYDOWN:
                need_exit = True



def fullLoop():
    sql.creatorTableSql()
    while 1:
        for event in config.pygame.event.get():
            if event.type == config.pygame.QUIT:
                config.pygame.quit()
            if config.state=="enteredName":
                config.user_name,config.state=loops.enterName(event,config.user_name,config.state)
            if  config.state == "startgame":
                loops.snakeSelectDirectionMove(event, config.snake_block)
            if config.state == "gameover":
                config.state=loops.needRestart(event,config.state)
            if config.state == "restartgame":
                loops.  reInit()
                config.state = "startgame"
                
                
                
        if config.state=="enteredName":
            display.displayName(config.user_name)
        if  config.state == "startgame":
            if(config.eatFood()):
                loops.newFood()
                loops.increaseLenght()
            display.displayGame()
            loops.snakeMove()
            config.state=loops.deadSnake(config.state)
            display.displayGame()
            print(config.state)
        if config.state == "sqlInsert":
            if config.Length_of_snake>10:
                sql.insert(config.user_name, config.Length_of_snake-1)
            config.state = "gameover"
        if config.state == "gameover":
            display.gameOver()
            
        
fullLoop()       
    