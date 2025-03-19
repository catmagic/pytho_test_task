import config
import time

def enterName(event,user_name,state):
    if event.type == config.pygame.KEYDOWN:
        if event.key in range(97,123):
            user_name+=chr(event.key)
        if event.key == config.pygame.K_BACKSPACE:
            user_name=user_name[:-1]
        if event.key == config.pygame.K_RETURN:
            state = "startgame"
    return user_name,state

def snakeSelectDirectionMove(event,snake_block):
    if event.type == config.pygame.KEYDOWN:
        if event.key == config.pygame.K_LEFT:
            config.x1_change = -snake_block
            config.y1_change = 0
        elif event.key == config.pygame.K_RIGHT:
            config.x1_change = snake_block
            config.y1_change = 0
        elif event.key == config.pygame.K_UP:
            config.y1_change = -snake_block
            config.x1_change = 0
        elif event.key == config.pygame.K_DOWN:
            config.y1_change = snake_block
            config.x1_change = 0
def snakeMove():
    config.x1 += config.x1_change
    config.y1 += config.y1_change
    snake_Head = []
    snake_Head.append(config.x1)
    snake_Head.append(config.y1)
    config.snake_List.append(snake_Head)
    if len(config.snake_List) > config.Length_of_snake:
        del config.snake_List[0]
    config.clock.tick(config.snake_speed)
    
def increaseLenght():
    config.Length_of_snake += 1
def newFood():
    config.foodx = round(config.random.randrange(0, config.dis_width - config.snake_block) / 10.0) * 10.0
    config.foody = round(config.random.randrange(0, config.dis_height - config.snake_block) / 10.0) * 10.0
    
def deadSnake(state ):
    if config.x1 >= config.dis_width or config.x1 < 0 or config.y1 >= config.dis_height or config.y1 < 0:
       state =  "sqlInsert"
    for x in config.snake_List[:-1]:
        if x == [config.x1,config.y1]:
            state = "sqlInsert"
    return state

def needRestart(event,state):
    if event.type == config.pygame.KEYDOWN:
        if event.key == config.pygame.K_q:
            config.pygame.quit()
        if event.key == config.pygame.K_r:
            state = "restartgame"
    return state
def reInit():
    config.x1 = config.dis_width / 2
    config.y1 = config.dis_height / 2
    config.x1_change = 0
    config.y1_change = 0
    config.snake_List = []
    config.Length_of_snake = 1
    newFood()