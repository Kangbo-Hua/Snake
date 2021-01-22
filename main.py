import tkinter,random,pygame,easygui
from pygame.locals import *
pygame.init()
#变量
with open("high.user","r") as file:
    high=file.read()
bodies=[(20,100),(40,100),(60,100),(80,100)]
bodies2=[(20,200),(40,200),(60,200),(80,200)]
headx=80
heady=100
headx2=80
heady2=200
foodx=200
foody=200
score=0
score2=0
way=2
way2=2
link=1
player1=True
player2=True
def init():
    global bodies,bodies2,headx,heady,headx2,heady2,foodx,foody,score,score2,way,way2,link,player1,player2
    bodies=[(20,100),(40,100),(60,100),(80,100)]
    bodies2=[(20,200),(40,200),(60,200),(80,200)]
    headx=80
    heady=100
    headx2=80
    heady2=200
    foodx=200
    foody=200
    score=0
    score2=0
    way=2
    way2=2
    link=1
    player1=True
    player2=True
    pygame.init()
    pygame.font.init()
    pygame.display.init()
def handleEvent():
    global way,way2
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP and way!=3:
                way=1
            if event.key == K_RIGHT and way!=4:
                way=2
            if event.key == K_DOWN and way!=1:
                way=3
            if event.key == K_LEFT and way!=2:
                way=4
            if event.key == K_w and way2!=3:
                way2=1
            if event.key == K_d and way2!=4:
                way2=2
            if event.key == K_s and way2!=1:
                way2=3
            if event.key == K_a and way2!=2:
                way2=4
def game():
    global headx,heady,foodx,foody,score,way,link,high
    canvas=pygame.display.set_mode((500,300))
    pygame.display.set_caption("Snake")
    canvas.fill((255,255,255))
    with open("color.user") as file:
        color=file.read()
        if color == "0":
            bg=pygame.image.load("bg1.png")
            body=pygame.image.load("body1.png")
            food=pygame.image.load("food1.png")
        else:
            bg=pygame.image.load("bg2.png")
            body=pygame.image.load("body2.png")
            food=pygame.image.load("food2.png")
    while True:
        if link == 1:
            if headx <= -20 or headx >= 500 or heady <= -20 or heady >= 300:
                link=0
            canvas.blit(bg,(0,0))
            font=pygame.font.Font("font.ttf",100)
            word=font.render(str(score),True,(200,200,200))
            canvas.blit(word,(200,100))
            for c in bodies:
                canvas.blit(body,c)
                if (headx,heady) == c and bodies.index(c) != len(bodies)-1:
                    link=0
            if way == 1:
                heady-=20
            if way == 2:
                headx+=20
            if way == 3:
                heady+=20
            if way == 4:
                headx-=20
            canvas.blit(food,(foodx,foody))
            if headx == foodx and heady == foody:
                score+=1
                new_x=random.randint(0,480)
                new_y=random.randint(0,280)
                new_x-=new_x%20
                new_y-=new_y%20
                for c in bodies:
                    if (new_x,new_y) == c and c != (headx,heady):
                        new_x=random.randint(0,480)
                        new_y=random.randint(0,280)
                        new_x-=new_x%20
                        new_y-=new_y%20
                    if c == (headx,heady):
                        new_x=bodies[0][0]
                        new_x=bodies[0][1]
                foodx=new_x
                foody=new_y
            bodies.append((headx,heady))
            if len(bodies) > score+4:
                bodies.pop(0)
        else:
            font=pygame.font.Font("font.ttf",100)
            word=font.render("GAME OVER",True,(200,200,200))
            canvas.blit(word,(50,100))
            link-=1
            if link < -10:
                with open("high.user","r") as file:
                    high=file.read()
                with open("high.user","w") as file:
                    if score > int(high):
                        file.write(str(score))
                    else:
                        file.write(high)
                break
        pygame.display.update()
        handleEvent()
        pygame.time.delay(100)
    pygame.display.quit()
    enter_root()
def game2():
    global bodies,bodies2,headx,heady,headx2,heady2,foodx,foody,score,score2,way,way2,link,player1,player2
    canvas=pygame.display.set_mode((500,300))
    pygame.display.set_caption("Snake")
    canvas.fill((255,255,255))
    with open("color.user") as file:
        color=file.read()
        if color == "0":
            bg=pygame.image.load("bg1.png")
            body=pygame.image.load("body1.png")
            body2=pygame.image.load("body3.png")
            food=pygame.image.load("food1.png")
        else:
            bg=pygame.image.load("bg2.png")
            body=pygame.image.load("body2.png")
            body2=pygame.image.load("body3.png")
            food=pygame.image.load("food2.png")
    while True:
        if link == 1:
            if headx <= -20 or headx >= 500 or heady <= -20 or heady >= 300:
                link=0
                player1=False
            if headx2 <= -20 or headx2 >= 500 or heady2 <= -20 or heady2 >= 300:
                link=0
                player2=False
            canvas.blit(bg,(0,0))
            font=pygame.font.Font("font.ttf",100)
            word=font.render(str(score),True,(200,200,200))
            canvas.blit(word,(200,100))
            font=pygame.font.Font("font.ttf",100)
            word=font.render(str(score2),True,(200,200,200))
            canvas.blit(word,(400,100))
            for c in bodies:
                canvas.blit(body,c)
                if (headx,heady) == c and bodies.index(c) != len(bodies)-1:
                    link=0
                    player1=False
            for c in bodies2:
                canvas.blit(body2,c)
                if (headx2,heady2) == c and bodies2.index(c) != len(bodies2)-1:
                    link=0
                    player2=False
            if way == 1:
                heady-=20
            if way == 2:
                headx+=20
            if way == 3:
                heady+=20
            if way == 4:
                headx-=20
            if way2 == 1:
                heady2-=20
            if way2 == 2:
                headx2+=20
            if way2 == 3:
                heady2+=20
            if way2 == 4:
                headx2-=20
            canvas.blit(food,(foodx,foody))
            if headx == foodx and heady == foody:
                score+=1
                new_x=random.randint(0,480)
                new_y=random.randint(0,280)
                new_x-=new_x%20
                new_y-=new_y%20
                for c in bodies:
                    if (new_x,new_y) == c and c != (headx,heady):
                        new_x=random.randint(0,480)
                        new_y=random.randint(0,280)
                        new_x-=new_x%20
                        new_y-=new_y%20
                    if c == (headx,heady):
                        new_x=bodies[0][0]
                        new_x=bodies[0][1]
                foodx=new_x
                foody=new_y
            if headx2 == foodx and heady2 == foody:
                score2+=1
                new_x=random.randint(0,480)
                new_y=random.randint(0,280)
                new_x-=new_x%20
                new_y-=new_y%20
                for c in bodies2:
                    if (new_x,new_y) == c and c != (headx2,heady2):
                        new_x=random.randint(0,480)
                        new_y=random.randint(0,280)
                        new_x-=new_x%20
                        new_y-=new_y%20
                    if c == (headx2,heady2):
                        new_x=bodies[0][0]
                        new_x=bodies[0][1]
                foodx=new_x
                foody=new_y
            for c in bodies:
                if (headx2,heady2) == c:
                    if bodies.index(c) == len(bodies)-1:
                        if random.randint(0,1):
                            link=0
                            player1=False
                        else:
                            link=0
                            player2=False
                    else:
                        link=0
                        player2=False
            for c in bodies2:
                if (headx,heady) == c:
                    if bodies2.index(c) == len(bodies2)-1:
                        if random.randint(0,1):
                            link=0
                            player1=False
                        else:
                            link=0
                            player2=False
                    else:
                        link=0
                        player1=False
            bodies.append((headx,heady))
            bodies2.append((headx2,heady2))
            if len(bodies) > score+4:
                bodies.pop(0)
            if len(bodies2) > score2+4:
                bodies2.pop(0)
        else:
            font=pygame.font.Font("font.ttf",80)
            if not player1:
                word=font.render("PLAYER2 WIN",True,(200,200,200))
            if not player2:
                word=font.render("PLAYER1 WIN",True,(200,200,200))
            canvas.blit(word,(50,100))
            link-=1
            if link < -10:
                break
        pygame.display.update()
        handleEvent()
        pygame.time.delay(100)
    pygame.display.quit()
    enter_root()
def enter_root():
    global highLab
    with open("high.user","r") as file:
        high=file.read()
    highLab.destroy()
    highLab=tkinter.Label(text="HIGHSCORE:"+str(high),font=("Font",20))
    highLab.pack()
    root.deiconify()
    root.update()
#命令属性
def tab(root):
    players=easygui.buttonbox("PLAYERS","CHOOSE",choices=("1PLAYER","2PLAYERS"))
    if players == None:
        return
    root.withdraw()
    init()
    if players == "1PLAYER":
        game()
    if players == "2PLAYERS":
        game2()
def color():
    chc=easygui.buttonbox("COLOR","CHOOSE",choices=("CLASSIC","GRASS"))
    if chc == "CLASSIC":
        with open("color.user","w") as file:
            file.write("0")
    if chc == "GRASS":
        with open("color.user","w") as file:
            file.write("1")
#创建一级界面
root=tkinter.Tk()
root.geometry("200x300")
root.resizable(0, 0)
root.title("Snake")
titleLab=tkinter.Label(text="Snake",font=("Font",40))
titleLab.pack()
highLab=tkinter.Label(text="HIGHSCORE:"+str(high),font=("Font",20))
highLab.pack()
startBtn=tkinter.Button(text="START",font=("FONT",30),bd=5,command=lambda:tab(root))
startBtn.place(x=35,y=125)
colorBtn=tkinter.Button(text="COLOR",font=("FONT",30),bd=5,command=color)
colorBtn.place(x=35,y=210)
root.mainloop()
