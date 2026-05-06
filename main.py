from gamelib import*
from Snippets import*
game = Game(1000,700,"Purrfect Pursuit")
background = Image("./images/BlueWallpaper.webp",game)

#Furnature
painting1 = Image("./images/Painting1.png",game)
painting1.resizeBy(120)

painting2 = Image("./images/Painting2.png",game)
painting2.resizeBy(120)

drawer = Image("./images/Drawer.png",game)
drawer.resizeBy(200)


MouseOpenning = Image("./images/MouseOpenning.png",game)
MouseOpenning.resizeBy(90)
MouseOpenning2 = Image("./images/MouseOpenning2.png",game)
MouseOpenning2.resizeBy(90)

#floor
floor = Image("./images/floor.png",game)
floor2 = Image("./images/floor2.png",game)
floor3 = Image("./images/floor2.png",game)
floor4 = Image("./images/floor3.png",game)
floor5 = Image("./images/floor4.png",game)


#Things
yarn = Image("./images/Yarn.png",game)
yarn.resizeBy(-30)


CatToy = Image("./images/CatToy.png",game)
CatToy2 = Image("./images/CatToy2.png",game)
CatToy3 = Image("./images/CatToy3.png",game)

catFood = Image("images/CatFood.png", game)
catFood.resizeBy(-50)

MouseTrap = Image("images/MouseTrap.png",game)
MouseTrap2 = Image("images/MouseTrap.png",game)



#cursor
cursor = Image("./images/OrangeCursor.png",game)
cursor.resizeBy(-50)
cursorselect = Image("./images/OrangeSelect.png",game)
cursorselect.resizeBy(-50)

#fonts
f = Font(black,100,black,"Blackadder ITC")
f2 = Font(black,40,black,"Goudy Stout")
f3 = Font(black,40,white,"Goudy Stout")


#cats/dog/mouse
DogSit = Animation("./images/DogSit.png",3,game,395/3,146/1,6)
DogSit.resizeBy(50)

rat = Animation("images/RatIdle.png", 4, game, 404/4, 100, 5)
ratAttack = Animation("images/RatAttack.png", 3, game, 299/3, 88, 5)
ratRunning = Animation("images/RatRunning.png", 3, game, 274/3, 63, 5)
ratDie = Animation("images/RatDie.png", 3, game, 303/3, 51, 5)


GrayCat = Animation("./images/GrayCatRight.png",3,game,401/3,102/1,6)
GrayCatDown = Animation("./images/GrayCatDown.png",3,game,434/3,132/1,6)
GrayCatLeft = Animation("./images/GrayCatLeft.png",3,game,419/3,105/1,6)
GrayCatRight = Animation("./images/GrayCatRight.png",3,game,401/3,102/1,6)
GrayCatUp = Animation("./images/GrayCatUp.png",3,game,434/3,105/1,6)
GrayCatLeft = Animation("./images/GrayCatLeft.png",3,game,419/3,105/1,6)

OrangeCat = Animation("./images/OrangeCatRight.png",3,game,434/3,106/1,6)
OrangeCatDown = Animation("./images/OrangeCatDown.png",3,game,434/3,126/1,6)
OrangeCatLeft = Animation("./images/OrangeCatLeft.png",3,game,434/3,105/1,6)
OrangeCatRight = Animation("./images/OrangeCatRight.png",3,game,434/3,106/1,6)
OrangeCatUp = Animation("./images/OrangeCatUp.png",3,game,434/3,110/1,6)

GrayCatIcon = Animation("./images/GrayCaticon.png",2,game,207/2,87/1,25)
OrangeCatIcon = Animation("images/orangeicon.png", 2, game, 202/2, 97/1, 25)

#screens

HowtoPlay = Image("images/howtoplay.png", game)
HowtoPlay.moveTo(500,323)
HowtoPlay.visible = False

LevelUp = Image("images/levelup.png", game)
LevelUp.moveTo(500, 323)
LevelUp.visible = False

Defeat = Image("images/GameOver.png", game)
Defeat.moveTo(500, 323)
Defeat.visible = False

GameWin = Image("images/gamewin.png", game)
GameWin.moveTo(500, 323)
GameWin.visible = False

#Music
bossMusic = Sound("music/BackToMe_boss.wav", 0)
gameMusic = Sound("music/NoOneNoticed_gameplay.wav", 1)
openingMusic = Sound("music/ShowMeHow_opening.wav", 2)

#Grey cat controls
def greycatcontrol():
    GrayCat.draw()
    if keys.Pressed[K_s]:
        GrayCat.images = GrayCatDown.images
        GrayCat.y +=5
    elif keys.Pressed[K_d]:
        GrayCat.images = GrayCatRight.images
        GrayCat.x +=5
# elif keys.Pressed[K_w]:
#        GrayCat.images = GrayCatUp.images
#        GrayCat.y -=5
    elif keys.Pressed[K_a]:
        GrayCat.images = GrayCatLeft.images
        GrayCat.x -=5
    else:
        GrayCat.images = GrayCatRight.images

#Orange cat controls
def orangecatcontrols():
    OrangeCat.draw()
    if keys.Pressed[K_DOWN]:
        OrangeCat.images = OrangeCatDown.images
        OrangeCat.y +=5
    elif keys.Pressed[K_RIGHT]:
        OrangeCat.images = OrangeCatRight.images
        OrangeCat.x +=5
#    elif keys.Pressed[K_UP]:
#        OrangeCat.images = OrangeCatUp.images
#        OrangeCat.y -=5'''
    elif keys.Pressed[K_LEFT]:
        OrangeCat.images = OrangeCatLeft.images
        OrangeCat.x -=5
    else:
        OrangeCat.images = OrangeCatRight.images





#positiion objects
def positionObjects(object):
    for i in range(len(object)):
        x = randint(150,850)
        y = randint(-5000,-100)
        object[i].moveTo(x,y)
        object[i].visible = True


orangejumping = False
orangelanded = False
orangefactor = 2
grayjumping = False
graylanded = False
grayfactor = 2
def GrayCatjumping():
    global grayjumping
    global graylanded
    global grayfactor
    
    if grayjumping:
        grayjumping = True
        graylanded = False
        GrayCat.y -= 24 * grayfactor
        grayfactor *= .85
        if grayfactor < 0.05:
            grayjumping = False
            grayfactor = 2

    if keys.Pressed[K_w] and graylanded and not grayjumping:
        grayjumping = True
    #print(graylanded,grayjumping,keys.Pressed[K_w]) 
    if not graylanded and  not GrayCat.collidedWith(floor,"rectangle"):
        GrayCat.y += 8
    if GrayCat.collidedWith(floor,"rectangle") or GrayCat.collidedWith(floor2,"rectangle") or GrayCat.collidedWith(floor3,"rectangle") or GrayCat.collidedWith(floor4,"rectangle") or GrayCat.collidedWith(floor5,"rectangle"):
        graylanded = True
    else:
        graylanded = False


def OrangeCatjumping():
    global orangejumping
    global orangelanded
    global orangefactor
    
    if orangejumping:
        orangejumping = True
        orangelanded = False
        OrangeCat.y -= 24 * orangefactor
        orangefactor *= .85
        if orangefactor < 0.05:
            orangejumping = False
            orangefactor = 2

    if keys.Pressed[K_UP] and orangelanded and not orangejumping:
        orangejumping = True
    #print(orangelanded,orangejumping,keys.Pressed[K_UP]) 
    if not orangelanded and not OrangeCat.collidedWith(floor,"rectangle"):
        OrangeCat.y += 8
    print(OrangeCat.collidedWith(floor2,"rectangle"))
    if OrangeCat.collidedWith(floor,"rectangle") or OrangeCat.collidedWith(floor2,"rectangle") or OrangeCat.collidedWith(floor3,"rectangle") or OrangeCat.collidedWith(floor4,"rectangle") or OrangeCat.collidedWith(floor5,"rectangle"):
        orangelanded = True
    else:
        orangelanded = False
    
'''
#lists
food = []
for i in range(16):
'''

#thing in the way

'''
GrayCat.moveTo(200,200)
while not game.over:
    game.processInput()
    background.draw()
    greycatcontrol()
    orangecatcontrols()
    #GrayCat.draw()
    floor2.draw()
    if keys.Pressed[K_a] and GrayCat.col

    if keys.Pressed[K_LEFT] and OrangeCat.collidedWith(floor3,"rectangle") and OrangeCat.x > floor3.x and OrangeCat.left < floor3.right and OrangeCat.bottom > floor3.top and OrangeCat.top < floor3.bottom:
            OrangeCat.x += 5
    if keys.Pressed[K_RIGHT] and OrangeCat.collidedWith(floor3,"rectangle") and OrangeCat.x < floor3.x and OrangeCat.right > floor3.left and OrangeCat.bottom > floor3.top and OrangeCat.top < floor3.bottom:
            OrangeCat.x -= 5
    if keys.Pressed[K_UP] and OrangeCat.collidedWith(floor3,"rectangle") and OrangeCat.y > floor3.y and OrangeCat.top < floor3.bottom and OrangeCat.left < floor3.right and OrangeCat.right > floor3.left:
            OrangeCat.y += 5
    if keys.Pressed[K_DOWN] and OrangeCat.collidedWith(floor3,"rectangle") and OrangeCat.y < floor3.y and OrangeCat.bottom > floor3.top and OrangeCat.left < floor3.right and OrangeCat.right > floor3.left:
            OrangeCat.y -= 5

    if keys.Pressed[K_LEFT] and OrangeCat.collidedWith(floor4,"rectangle") and OrangeCat.x > floor4.x and OrangeCat.left < floor4.right and OrangeCat.bottom > floor4.top and OrangeCat.top < floor4.bottom:
            OrangeCat.x += 5
    if keys.Pressed[K_RIGHT] and OrangeCat.collidedWith(floor4,"rectangle") and OrangeCat.x < floor4.x and OrangeCat.right > floor4.left and OrangeCat.bottom > floor4.top and OrangeCat.top < floor4.bottom:
            OrangeCat.x -= 5
    if keys.Pressed[K_UP] and OrangeCat.collidedWith(floor4,"rectangle") and OrangeCat.y > floor4.y and OrangeCat.top < floor4.bottom and OrangeCat.left < floor4.right and OrangeCat.right > floor4.left:
            OrangeCat.y += 5
    if keys.Pressed[K_DOWN] and OrangeCat.collidedWith(floor4,"rectangle") and OrangeCat.y < floor4.y and OrangeCat.bottom > floor4.top and OrangeCat.left < floor4.right and OrangeCat.right > floor4.left:
            OrangeCat.y -= 5
'''







bar = Image("images/emptyWhite.png",game,use_alpha=False)
bar.resizeBy(-65)
bar.moveTo(495,380)

bar2 = Image("images/emptyWhite2.png",game,use_alpha=False)
bar2.resizeTo(500,50)
bar2.moveTo(490,460)

bar3 = Image("images/emptyWhite3.png",game,use_alpha=False)
bar3.resizeBy(-65)
bar3.moveTo(495,550)

#Cover
while not game.over:
    game.processInput()
    background.draw()
    floor.draw()
    floor.moveTo(500,675)
    painting2.draw()
    painting2.moveTo(800,550)
    painting1.draw()
    painting1.moveTo(130,200)
    game.drawText("Purrfect Pursuit",210,150,f)
    game.drawText("Start",370,350,f2)
    game.drawText("How To Play",230,430,f2)
    game.drawText("Quit",400,520,f2)
    cursor.visible = True
    bar.draw()
    bar2.draw()
    bar3.draw()
    HowtoPlay.draw()

    if cursor.collidedWith(bar,"rectangle"):
        cursor.visible = False
        cursorselect.moveTo(mouse.x,mouse.y)
        cursorselect.draw()
        #game.over = True

    if cursor.collidedWith(bar2,"rectangle"):
        cursor.visible = False
        cursorselect.moveTo(mouse.x,mouse.y)
        cursorselect.draw()

    if cursor.collidedWith(bar3,"rectangle"):
        cursor.visible = False
        cursorselect.moveTo(mouse.x,mouse.y)
        cursorselect.draw()

    if cursorselect.collidedWith(bar,"rectangle")and mouse.LeftClick:
        game.over = True

    
    if cursorselect.collidedWith(bar3,"rectangle")and mouse.LeftClick:
        game.quit()
        
    if mouse.LeftClick and cursorselect.collidedWith(bar2,"rectangle"):
        HowtoPlay.visible = True

    if keys.Pressed[K_z]:
        HowtoPlay.visible = False
        
    openingMusic.play()
    cursor.moveTo(mouse.x,mouse.y)
    cursor.draw()
    game.update(30)

cursor.visible = True
game.over = False
#game intro

while not game.over:
    game.processInput()
    background.draw()
    GrayCat.y = game.height - 50
    OrangeCat.y = game.height - 50

    MouseOpenning.draw()
    MouseOpenning.moveTo(870,600)
    floor.draw()
    floor.moveTo(500,675)
    painting1.draw()
    painting1.moveTo(200,200)
    painting2.draw()
    painting2.moveTo(500,260)
    drawer.draw()
    drawer.moveTo(510,590)
    catFood.draw()
    catFood.moveTo(yarn.x - 10,yarn.y - 40)
    yarn.draw()
    yarn.moveTo(400,660)
    CatToy2.draw()
    CatToy2.moveTo(100,600)
    CatToy3.draw()
    CatToy3.moveTo(700,550)
    DogSit.draw()
    DogSit.moveTo(300,600)
    cursor.moveTo(mouse.x,mouse.y)
    cursor.draw()
    orangecatcontrols()
    greycatcontrol()
    GrayCatjumping()
    gameMusic.play()


    if GrayCat.collidedWith(MouseOpenning):
        game.over = True
    if OrangeCat.collidedWith(MouseOpenning):
        game.over = True

    game.update(30)

game.over = False


#level 1

GrayCatHealthbar = Shape("bar", game, GrayCat.health, 10, green)
GrayCatIcon.resizeBy(-65)
OrangeCatHealthbar = Shape("bar", game, OrangeCat.health, 10, green)
OrangeCatIcon.resizeBy(-65)






yarn.resizeBy(-20)
CatToy.resizeBy(-50)
drawer.resizeBy(-50)
CatToy2.resizeBy(-15)
MouseTrap.resizeBy(-70)
MouseTrap2.resizeBy(-70)


GrayCat.y = game.height - 500
OrangeCat.y = game.height - 5
floor2.moveTo(500,550)
floor4.moveTo(50,300)
floor5.moveTo(1100,400)
floor3.moveTo(550,250)
MouseOpenning.moveTo(100,600)
GrayCat.moveTo(MouseOpenning.x,MouseOpenning.y)
OrangeCat.moveTo(MouseOpenning.x,MouseOpenning.y)

while not game.over:
    game.processInput()
    background.draw()
    MouseOpenning.draw()
    cursor.moveTo(mouse.x,mouse.y)
    floor.draw()
    floor2.draw()
    floor3.draw()
    
    floor4.draw()
    floor5.draw()
    floor4.moveTo(50,300)
    GrayCatjumping()
    OrangeCatjumping()
    #GrayCat.draw()
    orangecatcontrols()
    greycatcontrol()
    cursor.draw()
    catFood.draw()
    catFood.moveTo(250,600)


    
    yarn.draw()
    yarn.moveTo(floor2.x+50,floor2.y-50)
    
    CatToy.draw()
    CatToy.moveTo(800,350)
    
    drawer.draw()
    drawer.moveTo(floor4.x+150,floor4.y-50)
    
    CatToy2.draw()
    CatToy2.moveTo(CatToy.x+130,CatToy.y-20)
    
    MouseTrap.draw()
    MouseTrap.moveTo(floor3.x+70,floor3.y-20)
    MouseOpenning2.moveTo(floor4.x,floor4.y-78)
    
    GrayCatHealthbar.draw()
    GrayCatHealthbar.moveTo(GrayCat.x,GrayCat.y-50)

    OrangeCatHealthbar.draw()
    OrangeCatHealthbar.moveTo(OrangeCat.x,OrangeCat.y-50)
    
    GrayCatIcon.draw()
    GrayCatIcon.moveTo(GrayCatHealthbar.x,GrayCatHealthbar.y)

    
    OrangeCatHealthbar.width = OrangeCat.health
    OrangeCatIcon.moveTo(OrangeCatHealthbar.x, OrangeCatHealthbar.y)



    #if GrayCat.collidedWith(yarn) or (CatToy) or (CatToy2) and keys.Pressed[K_d]:
        #GrayCat.x -= 2

    if keys.Pressed[K_a] and GrayCat.collidedWith(floor2,"rectangle") and GrayCat.x > floor2.x and GrayCat.left < floor2.right and GrayCat.bottom > floor2.top and GrayCat.top < floor2.bottom:
            GrayCat.x -= 5
    if keys.Pressed[K_d] and GrayCat.collidedWith(floor2,"rectangle") and GrayCat.x < floor2.x and GrayCat.right > floor2.left and GrayCat.bottom > floor2.top and GrayCat.top < floor2.bottom:
            GrayCat.x += 5
#    if keys.Pressed[K_w] and GrayCat.collidedWith(floor2,"rectangle") and GrayCat.y > floor2.y and GrayCat.top < floor2.bottom and GrayCat.left < floor2.right and GrayCat.right > floor2.left:
#            GrayCat.y += 5
    if keys.Pressed[K_s] and GrayCat.collidedWith(floor2,"rectangle") and GrayCat.y < floor2.y and GrayCat.bottom > floor2.top and GrayCat.left < floor2.right and GrayCat.right > floor2.left:
            GrayCat.y -= 5

    if keys.Pressed[K_LEFT] and OrangeCat.collidedWith(floor2,"rectangle") and OrangeCat.x > floor2.x and OrangeCat.left < floor2.right and OrangeCat.bottom > floor2.top and OrangeCat.top < floor2.bottom:
            OrangeCat.x -= 5
    if keys.Pressed[K_RIGHT] and OrangeCat.collidedWith(floor2,"rectangle") and OrangeCat.x < floor2.x and OrangeCat.right > floor2.left and OrangeCat.bottom > floor2.top and OrangeCat.top < floor2.bottom:
            OrangeCat.x += 5
#    if keys.Pressed[K_w] and OrangeCat.collidedWith(floor2,"rectangle") and OrangeCat.y > floor2.y and OrangeCat.top < floor2.bottom and OrangeCat.left < floor2.right and OrangeCat.right > floor2.left:
#            OrangeCat.y += 5
    if keys.Pressed[K_DOWN] and OrangeCat.collidedWith(floor2,"rectangle") and OrangeCat.y < floor2.y and OrangeCat.bottom > floor2.top and OrangeCat.left < floor2.right and OrangeCat.right > floor2.left:
            OrangeCat.y -= 5

    if GrayCat.collidedWith(MouseOpenning2) and OrangeCat.collidedWith(MouseOpenning2):
        LevelUp.visible = True
        if keys.Pressed[K_KP_ENTER]:
            game.over = True

    GrayCatHealthbar.width = GrayCat.health
    OrangeCatHealthbar.width = OrangeCat.health


    if GrayCat.collidedWith(catFood):
        catFood.visible = False
        GrayCat.health += 30
    if OrangeCat.collidedWith(catFood):
        catFood.visible = False
        OrangeCat.health += 30


    if GrayCat.collidedWith(MouseTrap):
         MouseTrap.visible = False
         GrayCat.health -= 40
    if GrayCat.collidedWith(CatToy):
        CatToy.visible = False
        GrayCat.health -=30
    if GrayCat.collidedWith(CatToy2):
        CatToy2.visible = False
        GrayCat.health -=20
    if GrayCat.collidedWith(CatToy3):
        CatToy3.visible = False
        GrayCat.health -=30
    if GrayCat.collidedWith(yarn):
        yarn.visible = False
        GrayCat.health -=40
    if GrayCat.collidedWith(drawer):
        drawer.visible = False
        GrayCat.health -=30
        
    if OrangeCat.collidedWith(MouseTrap):
         MouseTrap.visible = False
         OrangeCat.health -= 40
    if OrangeCat.collidedWith(CatToy):
        CatToy.visible = False
        OrangeCat.health -=20
    if OrangeCat.collidedWith(CatToy2):
        CatToy2.visible = False
        OrangeCat.health -=30
    if OrangeCat.collidedWith(CatToy3):
        CatToy3.visible = False
        OrangeCat.health -=30
    if OrangeCat.collidedWith(yarn):
        yarn.visible = False
        OrangeCat.health -=40
    if OrangeCat.collidedWith(drawer):
        drawer.visible = False
        OrangeCat.health -=30

    LevelUp.draw()




    '''
    if GrayCat.collidedWith(MouseTrap) or GrayCat.collidedWith(catToy) or GrayCat.collidedWith(catToy2) or GrayCat.collidedWith(drawer) or OrangeCat.collidedWith(MouseTrap) or OrangeCat.collidedWith(catToy) or OrangeCat.collidedWith(catToy2) or OrangeCat.collidedWith(drawer):
        MouseTrap.visible = False
        GrayCat.health -= 10

    '''

   

    game.update(30)

GrayCat.moveTo(MouseOpenning.x,MouseOpenning.y)
OrangeCat.moveTo(MouseOpenning.x,MouseOpenning.y)



    

#Level 2
game.over = False

s = randint(1,10)

obstacles = []
for i in range(200):
    d = Image("./images/Drawer.png",game)
    d.setSpeed(10, 180)
    obstacles.append(d)
positionObjects(obstacles)

while not game.over:
    game.processInput()
    background.draw()
    MouseOpenning.draw()
    bossMusic.play()

    greycatcontrol()
    orangecatcontrols()
    GrayCatjumping()

    MouseOpenning2.moveTo(900,600)
    
    MouseOpenning2.draw()
    
    GrayCatHealthbar.draw()
    GrayCatHealthbar.moveTo(GrayCat.x,GrayCat.y-50)
    GrayCatIcon.moveTo(GrayCatHealthbar.x,GrayCatHealthbar.y)

    OrangeCatHealthbar.draw()
    OrangeCatHealthbar.moveTo(OrangeCat.x, OrangeCat.y-50)
    OrangeCatIcon.moveTo(OrangeCatHealthbar.x, OrangeCatHealthbar.y)

    floor.draw()
    rat.draw()
    rat.moveTo(MouseOpenning2.x, MouseOpenning.y)
    
    GrayCatHealthbar.width = GrayCat.health
    OrangeCatHealthbar.width = OrangeCat.health
    for i in range(len(obstacles)):
        obstacles[i].move()
        if GrayCat.collidedWith(obstacles[i]):
            obstacles[i].visible = False
            GrayCat.health -= 50

        if OrangeCat.collidedWith (obstacles[i]):
            obstacles[i].visible = False
            OrangeCat.health -= 40
        
        game.score += 1

        if game.score == 200 or GrayCat.health <= 0 or OrangeCat.health <= 0:
            Defeat.visible = True
            if keys.Pressed[K_LSHIFT]:
                game.over = True

        if GrayCat.collidedWith(rat) and OrangeCat.collidedWith(rat):
            GameWin.visible = True
            if keys.Pressed[K_x]:
                game.over = True 
    

    greycatcontrol()
    orangecatcontrols()
    GrayCatjumping()
    GameWin.draw()
    cursor.draw()
    cursor.moveTo(mouse.x,mouse.y)
    
    game.update(30)
game.quit()
