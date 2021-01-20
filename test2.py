import pygame
from random import randint
import math
from sklearn.cluster import KMeans
import sys
p1 = [12,12]
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147,153,35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)
COLER = [RED, GREEN , BLUE, YELLOW,PURPLE,SKY,ORANGE,GRAPE,GRASS]
pygame.init()
screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption('Kmeans')
clock = pygame.time.Clock()
BACKGROUND = (214,214,214)
BLACK = (0,0,0)
BACKGROUND_PANEL = (249,255,230)
WHITE = (255,255,255)
POINT = []
CLUSSTER = []
LABEL = []
def create(string):
    font = pygame.font.SysFont('sans', 40)
    return font.render(string,True,WHITE )
def create_new(string):
    font = pygame.font.SysFont('sans', 40)
    return font.render(string,True,BLACK )
def create_new_small(string):
    font = pygame.font.SysFont('sans', 20)
    return font.render(string,True,BLACK )
running = True
k = 0
error = 0
while running:
    try:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        clock.tick(60)
        screen.fill(BACKGROUND)
        # ve man hinh draw
        # hinh chu nhat rect
        pygame.draw.rect(screen,BLACK,(50,50,700,500))
        pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))

        # ve nut K++
        pygame.draw.rect(screen, BLACK, (850,50,50,50))
        screen.blit(create("+"),(865,50))
        pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
        screen.blit(create("-"), (970, 50))

        # k value
        text_k = create_new("K= "+str(k))
        screen.blit(text_k,(1050,50))

        # run button
        pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
        screen.blit(create("run"), (900,150))

        # random
        pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
        screen.blit(create("random"), (850, 250))


        # nut error _sklearn
        pygame.draw.rect(screen, BLACK, (850, 550, 150, 50))
        screen.blit(create("reset"), (850, 550))

        pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
        screen.blit(create("algthomis"), (850, 450))

        # vtao cac diem
        if 50 < mouse_x < 750 and 50 < mouse_y < 550:
            text_mouse = create_new_small("("+str(mouse_x-50)+ ',' +str(mouse_y-50)+ ')')
            screen.blit(text_mouse,(mouse_x+10,mouse_y))

        # chi dinh chuot
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # creat point panel
                if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                    LABEL = []
                    point = [mouse_x-50,mouse_y-50]
                    POINT.append(point)
                    print(POINT)
                # Change K button +
                if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                    if k < 8:
                        k+=1

                # Change K button -
                if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                    if k >0:
                        k-=1

                # run button
                if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                    LABEL =[]
                    if CLUSSTER == []:
                        continue
                    # assert points to clothes clusster
                    for p in POINT:
                        distances_to_clusster = []

                        for c in CLUSSTER:
                            dis = distance(p,c)
                            distances_to_clusster.append(dis)
                        min_distance = min(distances_to_clusster)
                        labels = distances_to_clusster.index(min_distance)
                        LABEL.append(labels)
                    # updata clusster
                    for i in range(k):
                        sum_x = 0
                        sum_y = 0
                        count = 0
                        for j in range(len(POINT)):
                            if LABEL[j]== i:
                                sum_x += POINT[j][0]
                                sum_y += POINT[j][1]
                                count += 1
                        # new clusster
                        if count!=0:
                            new_clusster_x = sum_x / count
                            new_clusster_y = sum_y / count
                            CLUSSTER[i] = [new_clusster_x,new_clusster_y]

                # random button
                if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                    CLUSSTER=[]
                    for i in range(k):
                        random_point = [randint(0,700),randint(0,500)]
                        CLUSSTER.append(random_point)

                # reset button
                if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                    POINT = []
                    CLUSSTER = []
                    LABEL = []
                    k = 0
                    error = 0
                    print('reset')

                # algothimsis button
                if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                    kmeans = KMeans(n_clusters=k).fit(POINT)
                    print(kmeans.cluster_centers_)
                    LABEL = kmeans.predict(POINT)
                    CLUSSTER = kmeans.cluster_centers_
                    print('kq')
        # draw clusster
        for i in range(len(CLUSSTER)):
            pygame.draw.circle(screen,COLER[i],(int(CLUSSTER[i][0])+50,int(CLUSSTER[i][1])+50),10)
        # ve qua cac diem
        for i in range(len(POINT)):
            pygame.draw.circle(screen,BLACK,(POINT[i][0]+50,POINT[i][1]+50),6)
            if len(LABEL) == 0:
                pygame.draw.circle(screen, WHITE, (POINT[i][0] + 50, POINT[i][1] + 50), 5)
            else:
                pygame.draw.circle(screen, COLER[LABEL[i]], (POINT[i][0] + 50, POINT[i][1] + 50), 5)
        # caculate  and daw error
        error = 0
        if len(CLUSSTER) != 0 and len(LABEL) != 0:
            for i in range(len(POINT)):
                error += distance(POINT[i],CLUSSTER[LABEL[i]])
        text_error = create_new("Error= " + str(int(error)))
        screen.blit(text_error, (850, 350))
    except error :
        sys.exit()
    pygame.display.flip()
pygame.quit()


