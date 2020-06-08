import turtle
import random
import time


start_time=(time.time())
end_time=start_time+5
GRAVITY=-0.015
game_over=False

wn=turtle.Screen()
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

objects=[]

#############################################################
spikes=turtle.Turtle()
spikes.penup()
spikes.goto(-100, 300)
spikes.color("red", "red")
spikes.pendown()
spikes.left(45)
spikes.begin_fill()
for i in range (19):
    spikes.right(90)
    spikes.forward(15)
    spikes.left(90)
    spikes.forward(15)
spikes.end_fill()
spikes.hideturtle()
spikes.fillcolor()
spikes.penup()
spikes.goto(-100, -300)
spikes.pendown()
spikes.begin_fill()
spikes.right(90)
for i in range (19):
    spikes.left(90)
    spikes.forward(15)
    spikes.right(90)
    spikes.forward(15)
spikes.end_fill()




pen=turtle.Turtle()
pen.penup()
pen.color("white")
pen.goto(0, 0)
pen.hideturtle()

pen_m=turtle.Turtle()
pen_m.penup()
pen_m.color("white")
pen_m.goto(-200, 100)
pen_m.hideturtle()
pen_m.write(f"coins: 0", align="center", font=("Calibri", 35))

p_pen=turtle.Turtle()
p_pen.penup()
p_pen.color("white")
p_pen.goto(100, 0)
p_pen.hideturtle()



#############################################################

boarder=turtle.Turtle()
boarder.penup()
boarder.hideturtle()
boarder.goto(-300, -300)
boarder.pendown()
for i in range (4):
    boarder.forward(600)
    boarder.left(90)
boarder.goto(-100, -300)
boarder.left(90)
boarder.forward(600)


ball=turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.goto(100, 250)
ball.shapesize(stretch_wid=1.2, stretch_len=1.2)
ball.direction="none"
ball.dy=-2
ball.speed(0)
objects.append(ball)

squeeze=1
coins=[]
class coin (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        coins.append(self)
        objects.append(self)
        
    
    def animate(self):
        global squeeze
        self.shapesize(stretch_wid=1, stretch_len=squeeze)
        squeeze-=0.1
        if squeeze<=-1:
            squeeze=1
        wn.ontimer(self.animate, 70)

coin1=coin()
coin1.animate()
coin2=coin()
coin2.animate()

        

floors=[]
class floor (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("blue")
        self.speed(0)
        self.shapesize(stretch_wid=0.7, stretch_len=5)
        floors.append(self)
        objects.append(self)
        


floor1=floor()
floor2=floor()
floor3=floor()
floor4=floor()
floor5=floor()
floor6=floor()
floor7=floor()
floor8=floor()

places=[-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2]
random.shuffle(places)


for floor in floors:
    num=places[0]
    places.pop(0)
    
    floor.goto(random.randint(-1, 5)*50, num*50)

coin1.goto(floor1.xcor(), floor1.ycor()+20)
coin2.goto((floor2.xcor(), floor2.ycor()+20))
    
        




pause=True
############
def replay():
    
    global ready
    global game_over
    global money
    global score
    global blocked
    
    if game_over==True:
        ready=True
        pen.clear()
        blocked=False
        game_over=False
        
        pen_m.clear()
        pen_m.write(f"coins: 0", align="center", font=("Calibri", 35))
        ball.dy=-2
        
        money=0
        score=0
        
        
        ball.goto(100, 250)
        
        places=[-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2]
        random.shuffle(places)


        for floor in floors:
            num=places[0]
            places.pop(0)
        
            floor.goto(random.randint(-1, 5)*50, num*50)

        coin1.goto(floor1.xcor(), floor1.ycor()+20)
        coin2.goto((floor2.xcor(), floor2.ycor()+20))
        


def right():
    ball.direction="right"

def left():
    ball.direction="left"

def stop():
    ball.direction="none"

def pause():
    global pause
    if pause==True:
        pause=False
        p_pen.clear()
    else:
        pause=True
        p_pen.write(f"paused", align="center", font=("Calibri", 20))


wn.listen()
wn.onkeypress(right, "Right")
wn.onkeyrelease(stop, "Right")
wn.onkeypress(left, "Left")
wn.onkeyrelease(stop, "Left")
wn.onkeypress(pause, "p")
wn.onkeypress(replay, "r")

blocked=False
score=0
money=0
counter=0
ready=True


while True:#main loop##########################################################################################################
    wn.update()
    if pause==True:
        pass
    elif pause==False:
        if ball.direction=="right": #moving ball right
            x=ball.xcor()
            x+=1.8
            ball.setx(x)
            if ball.xcor()>280:
                ball.setx(280)
             
        if ball.direction=="left": #moving ball left
            x=ball.xcor()
            x-=1.8
            ball.setx(x)
            if ball.xcor()<-80:
                ball.setx(-80)

        if blocked==False: #ball downwards
            ball.dy+=GRAVITY
            y=ball.ycor()
            y+=ball.dy
            ball.sety(y)
        if blocked==True:#ball moving up
            y=ball.ycor()
            y+=1.4
            ball.sety(y)

##        if ball.ycor()<-280:
##            ball.sety(-280)

        for floor in floors:
            y=floor.ycor()
            y+=1.4
            floor.sety(y)
            if floor.ycor()>300:
                floor.goto(random.randint(-1, 5)*50, -320)#putting floors back to the bottom of the screen




            if blocked==False:
                
                if floor.ycor()+20>ball.ycor() and ball.ycor()-10>=floor.ycor() and floor.xcor()-55<ball.xcor() and floor.xcor()+55>ball.xcor():#checking if ball hit floors
                    blocked=True
                    ball.dy=-2
                    

            if blocked==True:

                if (ball.ycor()>floor.ycor() and ball.ycor()<floor.ycor()+20) and (floor.xcor()+55<ball.xcor() or floor.xcor()-55>ball.xcor()):#checking if ball moved away from floor
                    blocked=False


        
                    

        for coin in coins:
            y=coin.ycor()#moving coins up
            y+=1.4
            coin.sety(y)
            
        if coin1.ycor()>320:
            coin1.goto(floor1.xcor(), floor1.ycor()+20)

        if coin2.ycor()>320:
            coin2.goto(floor2.xcor(), floor2.ycor()+20)


        if (((ball.xcor()-coin1.xcor())**2)+((ball.ycor()-coin1.ycor())**2))**0.5<20:
            coin1.goto(-1000, -1000)
            money+=1
            pen_m.goto(-200, 100)
            pen_m.clear()
            pen_m.write(f"coins: {money}", align="center", font=("Calibri", 35))
            

        if (((ball.xcor()-coin2.xcor())**2)+((ball.ycor()-coin2.ycor())**2))**0.5<20:
            coin2.goto(-1000, -1000)
            money+=1
            pen_m.goto(-200, 100)
            pen_m.clear()
            pen_m.write(f"coins: {money}", align="center", font=("Calibri", 35))


        if floor1.ycor()<-300:
            coin1.goto(floor1.xcor(), floor1.ycor()+20)

        if floor2.ycor()<-300:
            coin2.goto(floor2.xcor(), floor2.ycor()+20)

        #game_over_situations
    
        if ball.ycor()>300 or ball.ycor()<-300:
            game_over=True
            x=1000
            for obj in objects:
                obj.goto(x, 1000)
                x+=1000
            pen.goto(100, 0)
            
            
        if game_over==True and ready==True:   
            pen.write(f"GAME OVER", align="center", font=("Calibri", 50))
            pen.goto(100, -60)
            pen.write(f"press 'r' to replay", align="center", font=("Calibri", 20))
            ready=False

        
            
            
                
  


                            
        
    
