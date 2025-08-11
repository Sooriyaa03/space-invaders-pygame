import turtle
import os
import math
import random
import winsound
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Invaders")
wn.bgpic("bgspace.gif")
wn.screensize()
wn.setup(width = 1.0, height = 1.0)
    
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
turtle.register_shape("knife.gif")
turtle.register_shape("boss.gif")
turtle.register_shape("bag.gif")
turtle.register_shape("green.gif")
turtle.register_shape("yellow.gif")
turtle.register_shape("red.gif")
turtle.register_shape("white.gif")
turtle.register_shape("comet.gif")
turtle.register_shape("cometside.gif")
turtle.register_shape("blast.gif")

bag = turtle.Turtle()
bag.penup()
bag.speed(0)
bag.shape("bag.gif")
bag.setposition(-800 , 0)

bag2 = turtle.Turtle()
bag2.penup()
bag2.speed(0)
bag2.shape("bag.gif")
bag2.setposition(800 , 0)

title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.color("white")
title_pen.penup()
title_pen.setposition(-270, 310)
titlestring = "SPACE INVADERS"
title_pen.write(titlestring, False, align="left", font=("Fixedsys", 70, "italic", "underline"))
title_pen.hideturtle()

energy = turtle.Turtle()
energy.speed(0)
energy.color("white")
energy.penup()
energy.setposition(373, 220)
energystring = "ENERGY"
energy.write(energystring, False, align="left", font=("Fixedsys", 20, "bold", "underline",))
energy.hideturtle()

prize_level= turtle.Turtle()
prize_level.speed(0)
prize_level.color("white")
prize_level.penup()
prize_level.setposition(-530, 0)
prizelevelstring = "LEVEL 1"
prize_level.write(prizelevelstring, False, align="left", font=("Fixedsys", 20, "bold"))
prize_level.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-295, 275)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15
number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("knife.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
bulletstate = "ready"

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("knife.wav",winsound.SND_ASYNC)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

count = 0
command = True
command2 = True

level = turtle.Turtle()
level.speed(0)
level.color("white", "black")
level.pensize(5)
level.penup()
level.setposition(350, 0)
level.pendown()
level.begin_fill()
level.left(90)
level.backward(250)
level.forward(450)
level.right(90)
level.forward(150)
level.right(90)
level.forward(450)
level.right(90)
level.forward(150)
level.end_fill()
level.hideturtle()

green = turtle.Turtle()
green.penup()
green.speed(0)
green.shape("green.gif")
green.setposition(425 , -50)
green.hideturtle()

yellow = turtle.Turtle()
yellow.penup()
yellow.speed(0)
yellow.shape("yellow.gif")
yellow.setposition(425 , -137)
yellow.hideturtle()

red = turtle.Turtle()
red.penup()
red.speed(0)
red.shape("red.gif")
red.setposition(425 , -240)
red.hideturtle()

white = turtle.Turtle()
white.penup()
white.speed(0)
white.shape("white.gif")
white.setposition(425 , -25)
white.hideturtle()

shelf = turtle.Turtle()
shelf.speed(0)
shelf.color("white")
shelf.pensize(15)
shelf.penup()
shelf.setposition(-900, -270)
shelf.pendown()
shelf.forward(500)

shelf2 = turtle.Turtle()
shelf2.speed(0)
shelf2.color("white")
shelf2.pensize(15)
shelf2.penup()
shelf2.setposition(-900, -250)
shelf2.pendown()
shelf2.forward(500)


while command:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            count = count + 1
            if count == 10:
                command = False
            
    for enemy in enemies:
        if enemy.ycor() < -275:
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()
            winsound.PlaySound("lose.wav",winsound.SND_ASYNC)
            boundary2_pen = turtle.Turtle()
            boundary2_pen.speed(0)
            boundary2_pen.color("white")
            boundary2_pen.penup()
            boundary2_pen.setposition(-170, 0)
            boundary2string = "GAME OVER"
            boundary2_pen.write(boundary2string, False, align="left", font=("Fixedsys", 50, "normal"))
            boundary2_pen.hideturtle()
                   
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

#----------------------------------------------

for enemy in enemies:
    enemy.hideturtle()

winsound.PlaySound("boss1.wav",winsound.SND_ASYNC)

if command2:
    boss_pen = turtle.Turtle()
    boss_pen.speed(0)
    boss_pen.color("white")
    boss_pen.penup()
    boss_pen.setposition(-245, 0)
    bossstring = "BOSS: OCTOWITCH"
    boss_pen.write(bossstring, False, align="left", font=("Fixedsys", 41, "normal"))
    boss_pen.hideturtle()
    time.sleep(2)
    boss_pen.clear()
    bulletspeed = 50 

boss2_bullet = turtle.Turtle()
boss2_bullet.color("white")
boss2_bullet.shape("cometside.gif")
boss2_bullet.penup()
boss2_bullet.speed(0)
boss2_bullet.setheading(90)
boss2_bullet.hideturtle()

boss2_bulletspeed = 20
boss2_bulletstate = "ready"

boss3_bullet = turtle.Turtle()
boss3_bullet.color("white")
boss3_bullet.shape("cometside.gif")
boss3_bullet.penup()
boss3_bullet.speed(0)
boss3_bullet.setheading(90)
boss3_bullet.hideturtle()

boss3_bulletspeed = 20
boss3_bulletstate = "ready"

boss_bullet = turtle.Turtle()
boss_bullet.color("white")
boss_bullet.shape("comet.gif")
boss_bullet.penup()
boss_bullet.speed(0)
boss_bullet.setheading(90)
boss_bullet.hideturtle()

boss_bulletspeed = 20
boss_bulletstate = "ready"

def boss_bullets():
    global boss_bulletstate
    if boss_bulletstate == "ready":
        boss_bulletstate == "fire"
        x = player.xcor()
        y = player.ycor() + 23
        boss_bullet.setposition(x , y*-1)
        boss_bullet.showturtle()

def boss_bullets2():
    global boss2_bulletstate
    if boss2_bulletstate == "ready":
        boss2_bulletstate == "fire"
        x = player.xcor()-15
        y = player.ycor() + 23
        boss2_bullet.setposition(x , y*-1)
        boss2_bullet.showturtle()

def boss_bullets3():
    global boss3_bulletstate
    if boss3_bulletstate == "ready":
        boss3_bulletstate == "fire"
        x = player.xcor()+15
        y = player.ycor() + 23
        boss3_bullet.setposition(x , y*-1)
        boss3_bullet.showturtle()
    
if command2:
    boss = turtle.Turtle()
    boss.color("red")
    boss.shape("boss.gif")
    boss.shapesize(2.5, 2.5)
    boss.penup()
    boss.speed(0)
    boss.setposition(-200, 255)
    bossspeed = 15

else:
    player.hideturtle()
    boundary_pen = turtle.Turtle()
    boundary_pen.speed(0)
    boundary_pen.color("white")
    boundary_pen.penup()
    boundary_pen.setposition(-170, 0)
    winsound.PlaySound("lose.wav",winsound.SND_ASYNC)
    boundarystring = "GAME OVER"
    boundary_pen.write(boundarystring, False, align="left", font=("Fixedsys", 50, "normal"))
    boundary_pen.hideturtle()

damage = 0
g_turn = 0
y_turn = 0
r_turn = 0

def blast_boss():
    blast = turtle.Turtle()
    blast.penup()
    blast.color("white")
    blast.speed(0)
    blast.shape("blast.gif")
    x = boss.xcor()
    y = boss.ycor()
    blast.setposition(x , y+20)

def gameover():
    boss.hideturtle()
    player.hideturtle()
    bullet.hideturtle()
    winsound.PlaySound("lose.wav",winsound.SND_ASYNC)
    boundary2_pen = turtle.Turtle()
    boundary2_pen.speed(0)
    boundary2_pen.color("white")
    boundary2_pen.penup()
    boundary2_pen.setposition(-170, 0)
    boundary2string = "GAME OVER"
    boundary2_pen.write(boundary2string, False, align="left", font=("Fixedsys", 50, "normal"))
    boundary2_pen.hideturtle()

octo_pen = turtle.Turtle()
octo_pen.speed(0)
octo_pen.color("white")
octo_pen.penup()
octo_pen.setposition(-210, -380)
octostring = "(!) Hit the Centre to Damage (!)" 
octo_pen.write(octostring, False, align="left", font=("Arial", 20 , "normal"))
octo2string = "# bullet speed increased\n# can adjust bullet while in fire"
octo_pen.setposition(-190, -430)
octo_pen.write(octo2string, False, align="left", font=("Arial", 15 , "normal"))



octo_pen.hideturtle()


while command2:
    y = boss_bullet.ycor()
    y -= boss_bulletspeed
    boss_bullet.sety(y)

    y = boss2_bullet.ycor()
    y -= boss2_bulletspeed
    boss2_bullet.sety(y)

    y = boss3_bullet.ycor()
    y -= boss3_bulletspeed
    boss3_bullet.sety(y)

    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 300 :
        bullet.hideturtle()
        bulletstate = "ready"

    if boss_bullet.ycor() < -275:
        boss_bullet.hideturtle()
        bulletstate = "ready"

    if boss2_bullet.ycor() < -275:
        boss2_bullet.hideturtle()
        boss2_bulletstate = "ready"

    if boss3_bullet.ycor() < -275:
        boss3_bullet.hideturtle()
        boss3_bulletstate = "ready"

    x = boss.xcor()
    x += bossspeed
    boss.setx(x)

    if boss.xcor() > 280:
        bossspeed *= -1
        boss_bullets()
        boss_bullets2()
        boss_bullets3()

    if boss.xcor() < -280:
        bossspeed *= -1
        boss_bullets()
        boss_bullets2()
        boss_bullets3()

    if isCollision(boss_bullet, player):
        gameover()
            
    if isCollision(boss2_bullet, player):
        gameover()
    if isCollision(boss3_bullet, player):
        gameover()

    if isCollision(bullet, boss):
        winsound.PlaySound("damage.wav",winsound.SND_ASYNC)
        damage += 1
        g_turn += 1
        y_turn += 1
        r_turn += 1

    if damage == 0:
        white.showturtle()
        
    if damage == 1 and g_turn == 1:
        white.hideturtle()
        green.showturtle()
        g_turn = g_turn + 1

    if damage == 2:
        green.hideturtle()
        yellow.showturtle()

    if damage == 3:
        yellow.hideturtle()
        red.showturtle()

    if damage == 4:
        red.hideturtle()
        boss.hideturtle()
        blast_boss()
        winsound.PlaySound("defeat.wav",winsound.SND_ASYNC)
        boss_bullet.hideturtle()
        boss2_bullet.hideturtle()
        boss3_bullet.hideturtle()
        time.sleep(2)
        command2 = False

turtle.clearscreen()

#-----------------------------------------------------------------------------------------

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Invaders")
wn.bgpic("cloud.gif")

winsound.PlaySound("bossent.wav",winsound.SND_ASYNC)

turtle.register_shape("burger.gif")
turtle.register_shape("player2.gif")
turtle.register_shape("ice.gif")
turtle.register_shape("boss.gif")
turtle.register_shape("side.gif")
turtle.register_shape("green.gif")
turtle.register_shape("yellow.gif")
turtle.register_shape("red.gif")
turtle.register_shape("white.gif")
turtle.register_shape("comet.gif")
turtle.register_shape("cometside.gif")
turtle.register_shape("blast.gif")
turtle.register_shape("level1.gif")

bag = turtle.Turtle()
bag.penup()
bag.speed(0)
bag.shape("side.gif")
bag.setposition(-800 , 0)

bag2 = turtle.Turtle()
bag2.penup()
bag2.speed(0)
bag2.shape("side.gif")
bag2.setposition(800 , 0)

prize = turtle.Turtle()
prize.penup()
prize.speed(10)
prize.shape("level1.gif")
prize.setposition(-470 , -110)

title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.color("white")
title_pen.penup()
title_pen.setposition(-270, 310)
titlestring = "FOOD INVADERS"
title_pen.write(titlestring, False, align="left", font=("Fixedsys", 70, "italic", "underline"))
title_pen.hideturtle()

energy = turtle.Turtle()
energy.speed(0)
energy.color("white")
energy.penup()
energy.setposition(373, 220)
energystring = "ENERGY"
energy.write(energystring, False, align="left", font=("Fixedsys", 20, "bold", "underline",))
energy.hideturtle()

energy2 = turtle.Turtle()
energy2.speed(0)
energy2.color("white")
energy2.penup()
energy2.setposition(540, 220)
energy2string = "ENERGY"
energy2.write(energystring, False, align="left", font=("Fixedsys", 20, "bold", "underline",))
energy2.hideturtle()

prize_level= turtle.Turtle()
prize_level.speed(0)
prize_level.color("white")
prize_level.penup()
prize_level.setposition(-530, 0)
prizelevelstring = "LEVEL 1"
prize_level.write(prizelevelstring, False, align="left", font=("Fixedsys", 20, "bold"))
prize_level.hideturtle()

prize_level= turtle.Turtle()
prize_level.speed(0)
prize_level.color("white")
prize_level.penup()
prize_level.setposition(-720, 0)
prizelevelstring = "LEVEL 2"
prize_level.write(prizelevelstring, False, align="left", font=("Fixedsys", 20, "bold"))
prize_level.hideturtle()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 100
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-295, 275)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("player2.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15
number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("burger.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 5

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("ice.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30
bulletstate = "ready"

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("knife.wav",winsound.SND_ASYNC)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

count = 0
command = True
command2 = True

level = turtle.Turtle()
level.speed(0)
level.color("white", "black")
level.pensize(5)
level.penup()
level.setposition(350, 0)
level.pendown()
level.begin_fill()
level.left(90)
level.backward(250)
level.forward(450)
level.right(90)
level.forward(150)
level.right(90)
level.forward(450)
level.right(90)
level.forward(150)
level.end_fill()
level.hideturtle()

level2 = turtle.Turtle()
level2.speed(0)
level2.color("white", "black")
level2.pensize(5)
level2.penup()
level2.setposition(530, 0)
level2.pendown()
level2.begin_fill()
level2.left(90)
level2.backward(250)
level2.forward(450)
level2.right(90)
level2.forward(150)
level2.right(90)
level2.forward(450)
level2.right(90)
level2.forward(150)
level2.end_fill()
level2.hideturtle()

green = turtle.Turtle()
green.penup()
green.speed(0)
green.shape("green.gif")
green.setposition(425 , -50)
green.hideturtle()

yellow = turtle.Turtle()
yellow.penup()
yellow.speed(0)
yellow.shape("yellow.gif")
yellow.setposition(425 , -137)
yellow.hideturtle()

red = turtle.Turtle()
red.penup()
red.speed(0)
red.shape("red.gif")
red.setposition(425 , -240)
red.hideturtle()

white = turtle.Turtle()
white.penup()
white.speed(0)
white.shape("white.gif")
white.setposition(425 , -25)
white.hideturtle()

shelf = turtle.Turtle()
shelf.speed(0)
shelf.color("white")
shelf.pensize(15)
shelf.penup()
shelf.setposition(-900, -270)
shelf.pendown()
shelf.forward(500)

shelf2 = turtle.Turtle()
shelf2.speed(0)
shelf2.color("white")
shelf2.pensize(15)
shelf2.penup()
shelf2.setposition(-900, -250)
shelf2.pendown()
shelf2.forward(500)

while command:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            count = count + 1
            if count == 10:
                command = False
            
    for enemy in enemies:
        if enemy.ycor() < -275:
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()
            winsound.PlaySound("lose.wav",winsound.SND_ASYNC)
            boundary2_pen = turtle.Turtle()
            boundary2_pen.speed(0)
            boundary2_pen.color("white")
            boundary2_pen.penup()
            boundary2_pen.setposition(-170, 0)
            boundary2string = "GAME OVER"
            boundary2_pen.write(boundary2string, False, align="left", font=("Fixedsys", 50, "normal"))
            boundary2_pen.hideturtle()
                   
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

for enemy in enemies:
    enemy.hideturtle()

boss2_pen = turtle.Turtle()
boss2_pen.speed(0)
boss2_pen.color("black")
boss2_pen.penup()
boss2_pen.setposition(-230, 0)
boss2string = "BOSS: MEATBALLS"
boss2_pen.write(boss2string, False, align="left", font=("Fixedsys", 35, "normal"))
boss2_pen.hideturtle()
winsound.PlaySound("haha.wav",winsound.SND_ASYNC)
time.sleep(2)

turtle.clearscreen()

wn.mainloop()