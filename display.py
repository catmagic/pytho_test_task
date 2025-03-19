import pygame
import config
import sql

 
 
def Your_score(score):
    value = config.score_font.render("Your Score: " + str(score), True, config.yellow)
    config.dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        config.pygame.draw.rect(config.dis, config.black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = config.font_style.render(msg, True, color)
    config.dis.blit(mesg, [config.dis_width / 6, config.dis_height / 7])
    
def displayName(user_name):
    config.dis.fill(config.blue)
    message("your name:"+user_name+"?", config.red)
    config.pygame.display.update()    
def displayGame():
    config.dis.fill(config.blue)
    config.pygame.draw.rect( config.dis,  config.green, [ config.foodx,  config.foody,  config.snake_block,  config.snake_block])
    our_snake(config.snake_block, config.snake_List)
    Your_score(config.Length_of_snake - 1)
    config.pygame.display.update()   
def gameOver():
    config.dis.fill(config.white)
    if config.Length_of_snake>10:
        message("You win "+config.user_name+" your score "+str(config.Length_of_snake-1), config.green)
    else:
        message("You lose "+config.user_name+" your score "+str(config.Length_of_snake-1), config.red)
    top5=sql.top5()
    for i in range(len(top5)):  
        text=str(i+1)+" "+top5[i][0]+" score: "+str(top5[i][1])
        mesg = config.font_style.render(text, True, config.black)
        config.dis.blit(mesg, [config.dis_width / 6, config.dis_height *(2+i)/7 ])
    config.pygame.display.update()