import pygame
import time
import random

pygame.init()

#display settings
dis_width=800
dis_height=600

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Snake')
game_over= False



clock=pygame.time.Clock()


font_style = pygame.font.SysFont(None, 50)
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/10, dis_height/5])

def our_snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(dis,(255,255,255),[i[0],i[1],10,10])





def game_loop():
    #colors
    white=(255,255,255)
    blue= (0,0,255)
    red=(255,0,0)
    black=(0,0,0)



    x=dis_width/2
    y=dis_height/2

    x_change=0
    y_change=0

    foodx = round(random.randrange(0, dis_width -30) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width -30) / 10.0) * 10.0

    snake_List = []
    Length_of_snake = 1
 

    game_over= False
    game_close=False

    while not game_over:

        while game_close == True:

            dis.fill(black)
            message("You Lost!  Press   Q-Quit o r  P-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-10
                    y_change=0
                elif event.key == pygame.K_RIGHT:
                    x_change=10
                    y_change=0 
                elif event.key == pygame.K_UP:
                    x_change=0
                    y_change=-10
                elif event.key == pygame.K_DOWN:
                    x_change=0
                    y_change=10

        if x >= dis_width or x<=0 or y>= dis_height or y <=0:
            game_close=True
        
        x+=x_change
        y+=y_change
        dis.fill(black)
        pygame.draw.rect(dis,red, [foodx, foody,10,10])
        snake_Head =[]
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len (snake_List) > Length_of_snake:
            del(snake_List[0])

        for i in snake_List[:-1]:
            if i == snake_Head:
                game_close=True

        our_snake(snake_List)

        pygame.display.update()  

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, dis_width - 30) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - 30) / 10.0) * 10.0
            Length_of_snake += 1


        clock.tick(30)   

    pygame.quit()
    quit()


game_loop()
