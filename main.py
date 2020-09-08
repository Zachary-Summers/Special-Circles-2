import pygame, random, time, sys, os
os.system('clear')
print("\033[\n36mSpecial Circles \033[0m")
print("\033[36mBy Zachary And Dane \n\033[0m")
print("\033[34mYou are the green ball. The red ball is trying to touch you to make you lose a life. The blue ball will give you a life. The two same colored balls are portals that you can teleport between. the grey ball will make you faster and yellow. The big pink ball will also kill you but is immobile. The pink balls at the top are your lives. If you get enough lives your level goes up. If you lose all your lives it goes to one. The white balls are your level. The arrow keys and WASD keys will move your charecter. The e key will quit, the r key will restart everything, the p key will pause, the u key will unpause, the g key will pause the red ball for playtesting, the b key will unpause the red ball, c will clear the terminal, and z will use your power if possible.\n\033[0m")
highScore = 0
pygame.init()
screen = pygame.display.set_mode([800,600])
green = (255, 0, 166) 
blue = (0, 0, 0) 
square = False  
font = pygame.font.SysFont("comicsansms", 50)
text = font.render('Special Circles', True, green, blue) 
textRect = text.get_rect()  
textRect.center = (650, 35) 
radius = 10
COLOR = (0,255,0)
BAD_COLOR = (255,0,0)
END_COLOR = (0, 13, 255)
LIFE_COLOR = (255, 120, 196)
ISLAND_COLOR = (255, 0, 255)
BAD_ISLAND_COLOR = (255, 0, 136)
SLOW_COLOR = (128, 62, 57)
clock = 3  
wNum = 10
level = 1
speed = 2
b = True
print('level:',level)
x_change = 0
y_change = 0
x = random.randint(0,800)
y = random.randint(0,600)
bx = random.randint(0,800)
by = random.randint(0,600)
fx = random.randint(0,800)
fy = random.randint(0,600)
ix = random.randint(0,800)
iy = random.randint(0,600)
bix = random.randint(0,800)
biy = random.randint(0,600)
itx = random.randint(0,800)
ity = random.randint(0,600)
sx = random.randint(0,800)
sy = random.randint(0,600)
run = True
BLACK = (0,0,0)
lives = 5
print(lives)
ex = random.randint(0,800)
ey = random.randint(0,600)
do = False
do2 = False
do3 = True
do4 = True
do5 = False
while run:
  if level % 2 == 0:
    square == True
  if level > highScore:
    highScore = level
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        x_change = -speed
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        x_change = speed
      elif event.key == pygame.K_UP or event.key == pygame.K_w:
        y_change = -speed
      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        y_change = speed
      elif event.key == pygame.K_p:
        clock = 1
      elif event.key == pygame.K_u:
        clock = 3
      elif event.key == pygame.K_e:
        pygame.quit()
        quit()
      elif event.key == pygame.K_z and level % 2 == 1 and speed == 3 and do3 == True:
        lives += 1
        do3 = False
      elif event.key == pygame.K_z and level % 2 == 0 and speed >= 2 and do4 == True:
        wNum -= 1
        do4 = False
      elif event.key == pygame.K_r:
        do3 = True
        do4 = True
        clock = 3
        wNum = 10
        level = 1
        print('level:',level)
        x_change = 0
        y_change = 0
        x = random.randint(0,800)
        y = random.randint(0,600)
        bx = random.randint(0,800)
        by = random.randint(0,600)
        ix = random.randint(0,800)
        iy = random.randint(0,600)
        bix = random.randint(0,800)
        biy = random.randint(0,600)
        ity = random.randint(0,600)
        itx = random.randint(0,800)
        run = True
        lives = 5
        print(lives)
        ex = random.randint(0,800)
        ey = random.randint(0,600)
      elif event.key == pygame.K_g:
        b = False
      elif event.key == pygame.K_b:
        b = True
      elif event.key == pygame.K_c:
        os.system('clear')
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_w:
        x_change = 0
        y_change = 0
    if event.type == pygame.MOUSEBUTTONDOWN:
      Mouse_x, Mouse_y = pygame.mouse.get_pos()
      do5 = True
      if Mouse_x > x:
        x_change = speed
      elif Mouse_x < x:
        x_change = -speed
    elif event.type == pygame.MOUSEBUTTONUP:
      x_change = 0
      y_change = 0
      do5 = False
    elif do5 == True:
      if Mouse_y > y:
        y_change = speed
      elif Mouse_y < y:
        y_change = -speed    
  if clock == 3:
    time.sleep(0.01)
    if bx < x:
      bx_change = 1
    if bx > x:
      bx_change = -1
    if by < y:
      by_change = 1
    if by > y:
      by_change = -1
    if ex < x:
      ex_change = -1
    if ex > x:
      ex_change = 1
    if ey < y:
      ey_change = -1
    if ey > y:
      ey_change = 1
    if x >= 800:
      x_change = -speed
    elif x <= 0:
      x_change = speed
    elif y >= 600:
      y_change = -speed
    elif y <= 0 :
      y_change = speed
    elif bx >= 800:
      bx_change = -1
    elif bx <= 0:
      bx_change = 1
    elif by >= 600:
      by_change = -1
    elif by <= 0:
      by_change = 1
    elif ex >= 800:
      ex_change = -1
    elif ex <= 0:
      ex_change = 1
    elif ey >= 600:
      ey_change = -1
    elif ey <= 0:
      ey_change = 1
    elif x + radius > sx - radius and y + radius >= sy - radius and x - radius <= sx + radius and sy - radius <= sy + radius and y - radius <= sy + radius:
      speed = 1
      COLOR = (255, 106, 0)
    elif x + radius >= ix - 15 and y + radius >= iy - 15 and x - radius <= ix + 15 and y - radius <= iy + 15:
      x = itx + 26
      y = ity + 26
    elif x + radius >= itx - 15 and y + radius >= ity - 15 and x - radius <= itx + 15 and y - radius <= ity + 15:
      x = ix + 26
      y = iy + 26
    elif (x + radius >= bx - radius and y + radius >= by - radius  and x - radius <= bx + radius and y - radius <= by + radius) or  (x + radius>= bix - 15 and y + radius >= biy - 15 and x - radius <= bix + 15 and y - radius <= biy + 15):
      lives-=1
      print(lives)
      x = random.randint(0,800)
      y = random.randint(0,600)
      bx = random.randint(0,800)
      by = random.randint(0,600)
      ex = random.randint(0,800)
      ey = random.randint(0,600)
      fx = random.randint(0,600)
      fy = random.randint(0,800)
      ix = random.randint(0,800)
      iy = random.randint(0,600)
      bix = random.randint(0,800)
      biy = random.randint(0,600)
      itx = random.randint(0,800)
      ity = random.randint(0,600)
      COLOR = (0, 255, 0)
      speed = 2
      do3 = True
      do4 = True
      time.sleep(0.1)
    elif x + radius > fx - radius and y + radius >= fy - radius and x - radius <= fx + radius and fy - radius <= fy + radius and y - radius <= fy + radius:
      speed = 3 
      COLOR = (255, 255, 0)
    elif x + radius >= ex - radius and y + radius >= ey - radius and x - radius <= ex + radius and y - radius <= ey + radius:
      lives+=1
      print(lives)
      x = random.randint(0,800)
      y = random.randint(0,600)
      bx = random.randint(0,800)
      by = random.randint(0,600)
      ex = random.randint(0,800)
      ey = random.randint(0,600)
      fx = random.randint(0,600)
      fy = random.randint(0,800)
      ix = random.randint(0,800)
      iy = random.randint(0,600)
      bix = random.randint(0,800)
      biy = random.randint(0,600)
      itx = random.randint(0,800)
      ity = random.randint(0,600)
      COLOR = (0, 255, 0)
      speed = 2
      do3 = True
      do4 = True
      time.sleep(0.1)
    if lives <= -1:
      print("\033[31mYOU LOSE \n\033[0m")
      level = 1
      x_change = 0
      y_change = 0
      x = random.randint(0,800)
      y = random.randint(0,600)
      bx = random.randint(0,800)
      by = random.randint(0,600)
      ix = random.randint(0,800)
      iy = random.randint(0,600)
      bix = random.randint(0,800)
      biy = random.randint(0,600)
      itx = random.randint(0,800)
      ity = random.randint(0,600)
      run = True
      BLACK = (0,0,0)
      lives = 5
      do3 = True
      do4 = True
      print('level:',level)
      print(lives)
      fx = random.randint(0,600)
      fy = random.randint(0,800)
      COLOR = (0, 255, 0)
      speed = 2
      time.sleep(0.1)
    elif lives >= wNum:
      print("\033[32mYOU WIN \n\033[0m")
      level+=1
      x_change = 0
      y_change = 0
      x = random.randint(0,800)
      y = random.randint(0,600)
      bx = random.randint(0,800)
      by = random.randint(0,600)
      ix = random.randint(0,800)
      iy = random.randint(0,600)
      bix = random.randint(0,800)
      biy = random.randint(0,600)
      run = True
      itx = random.randint(0,800)
      ity = random.randint(0,600)
      BLACK = (0,0,0)
      lives = 5
      print('level:',level)
      ex = random.randint(0,800)
      ey = random.randint(0,600)
      wNum += 1
      print(lives)
      fx = random.randint(0,600)
      fy = random.randint(0,800)
      do3 = True
      do4 = True
      COLOR = (0, 255, 0)
      speed = 2
      time.sleep(0.1)
    if b == True:
      bx = bx + bx_change
      by = by + by_change
    x += x_change
    y += y_change
    def lifeCircles(repLife):
      for i in range (repLife):
        pygame.draw.circle(screen, LIFE_COLOR,((i*20+10), 50), radius)
    def levelCircles(repLevel):
      for a in range (repLevel):
        pygame.draw.circle(screen, (255,255,255),((a*20+10), 100), radius)
    def highScoreCircles(repHighScore):
      for h in range (repHighScore):
        pygame.draw.circle(screen, (0, 255, 238), ((h*20+10), 150), radius)
    screen.fill(BLACK)
    screen.blit(text, textRect)
    lifeCircles(lives)
    levelCircles(level)
    highScoreCircles(highScore)
    pygame.draw.circle(screen,SLOW_COLOR,(sx,sy),radius)
    pygame.draw.circle(screen,ISLAND_COLOR,(itx,ity), 15)
    pygame.draw.circle(screen, COLOR,(x,y), radius)
    pygame.draw.circle(screen, END_COLOR, (ex,ey),radius)
    pygame.draw.circle(screen, BAD_COLOR,(bx,by), radius)
    pygame.draw.circle(screen, (50,50,50),(fx, fy), radius)
    pygame.draw.circle(screen, ISLAND_COLOR,(ix,iy), 15)
    pygame.draw.circle(screen, BAD_ISLAND_COLOR,(bix, biy), 15)
    if level % 2 == 0:
      rectangle = pygame.Rect((x - 10, y - 10), (20, 20))
      pygame.draw.rect(screen, COLOR, rectangle)
    pygame.display.update()


#TODO: rotate the green circle to an x and y when mouse clicked
#plan:
#mouse gets clicked:
#rotate green circle towards the mouse x and y
#green circle moves to x and y eventually
#repeat until game end or death
