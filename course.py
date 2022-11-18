import pygame
import sys
import numpy as np
from scipy.special import lambertw


def drawFor():
    global center
    for i in range(40, 1280 , 20):
        pygame.draw.line(screen, (170,170,170),(i, 0), (i,500))
    for i in range(0, 500,20):
        pygame.draw.line(screen,(170,170,170),(0,i), (1280,i))
    pygame.draw.line(screen,BLACK,(0,center[1]), (1280,center[1]))
    pygame.draw.line(screen,BLACK,(center[0], 0), (center[0], 720))
    pygame.draw.circle(screen,BLACK,center,2)
    pygame.draw.line(screen, BLACK, (440,500),(440,570))
    pygame.draw.line(screen, BLACK,(20,570),(860,570))
    pygame.draw.rect(screen, BLACK, (20, 500, 841, 120), width=1)


def drawSlider():
    global x,y,ys
    pygame.draw.rect(screen, BLACK, Slider_t, width = 1)
    pygame.draw.rect(screen, BLACK, (t_pos_x, t_pos_y, 4, 7))
    pygame.draw.line(screen,BLUE,(x,y),(x,center[1]))
    pygame.draw.circle(screen, RED, (x,y), 5)
    pygame .draw.circle(screen,BLUE,(x,ys),3)

def drawParabola():
    global x,y,center,ys, dt, t_pos_x, k
    g = 9.81
    pxx = center[0]
    pyy = center[1]
    # print (dt)
    if k == 0:
        dv = dt *(-g)
        dy = (-g)*dt*dt/2
        t0 = (dv + np.sqrt(dv*dv - 2*g*(-ys - dy +y)))/g
        # center[1] - y  x - center[0]
        if x == center[0]:
            a = np.pi/2
        else:
            a = np.arctan((dv*t0 + dy + center[1] - y)/(x - center[0]))
        v0 = (x - center[0])/ (np.cos(a)*t0)
        for px in range(center[0],int(x)+1):
            t = ((px - center[0])/(v0*np.cos(a)))
            py = (4.905*(t**2) - v0*np.sin(a)*t)+center[1]
            # pygame.draw.rect(screen,RED,(px,py,1,1))
            pygame.draw.line(screen,RED,(px,py),(pxx,pyy))
            pxx, pyy = px, py
        pygame.draw.arc(screen, BLACK, (0,480, 40, 40), 0, a)
        t_sl = t0*(t_pos_x-100)/900
        xt = v0*np.cos(a)*t_sl+center[0]
        yt = (4.905*(t_sl**2) - v0*np.sin(a)*t_sl)+center[1]
        pygame.draw.circle(screen,BLACK,(xt,yt),4,width = 1)
    else:
        print (dt)
        t0 = float( -dt + (lambertw(-np.exp(((k*k)*(- ys + y)/g)-1))/k) + (k*(ys - y)/g)+1/k)
        a = np.arctan( ( (g/(k*k))*(np.exp(-k*t0)-np.exp(-(k*t0) - (k*dt)) ) -((g/k)*dt) +(500-y) )/(x - 20) )
        v0 = (k*(x-20))/((1-np.exp(-k*t0))*np.cos(a))
        for px in range(center[0],int(x)+1):
            t = - (np.log((1-((px-center[0])*k)/(v0*np.cos(a))))/k)
            py = (1/k)*(-1+np.exp(-k*t))*((g/k)+v0*np.sin(a))+g*t/k +center[1]
            pygame.draw.line(screen,RED,(px,py),(pxx,pyy))
            pxx, pyy = px, py
        pygame.draw.arc(screen, BLACK, (0,480, 40, 40), 0, a)
        t_sl = t0*(t_pos_x-100)/900
        xt = -(v0*np.cos(a))/(k)*(np.exp(-k*t_sl)-1) + center[0]
        yt = (1/k)*(-1+np.exp(-k*t_sl))*((9.81/k)+v0*np.sin(a))+9.81*t_sl/k +center[1]
        pygame.draw.circle(screen,BLACK,(xt,yt),4,width = 1)
    f1 = pygame.font.SysFont("Times", 17)
    f2 = pygame.font.SysFont("Times",40)
    text1 = f1.render(f"""({(x-20)},{(500-y)})""",True,BLACK)
    screen.blit(text1,(x+10,y-8))
    text1 = f1.render(f"""({(x-20)},{(500-ys)})""",True,BLACK)
    screen.blit(text1,(x+10,ys-5))
    text1 = f1.render("Начальные координаты мишени:", True, BLACK)
    screen.blit(text1,(100,505))
    text1 = f1.render("Точка столкновения:",True,BLACK)
    screen.blit(text1,(580,505))
    text1 = f2.render(f"""V₀ = {round(v0,3)} m/s""",True,BLACK)
    screen.blit(text1,(980,505))
    text1 = f2.render(f"""φ = {round(a,3)} rad""",True,BLACK)
    screen.blit(text1,(1050,550))

    # Rect_x = pygame.Rect(1115,510,160,30)
    # Rect_y = pygame.Rect(1115,545,160,30)
    # Rect_t = pygame.Rect(1115,580,160,30)
    # Slider_t = pygame.Rect(100, 700, 800, 3)


def drawKnopki():
    global user_x,user_y,user_t,Rect_x,Rect_y,screen,center, writing_x, writing_y, writing_tm, writing_k, writing_xs, writing_ys
    pygame.draw.rect(screen,BLACK,Rect_x)
    if writing_x:
        pygame.draw.rect(screen,WHITE,(62,537,156,26),width = 1)
    pygame.draw.rect(screen,BLACK,Rect_y)
    if writing_y:
        pygame.draw.rect(screen,WHITE,(267,537,156,26),width = 1)
    pygame.draw.rect(screen, BLACK,Rect_t)
    if writing_t:
        pygame.draw.rect(screen,WHITE,(267,582,156,26),width = 1)
    pygame.draw.rect(screen,GREY, Rect_xs)
    pygame.draw.rect(screen,BLACK,Rect_ys)
    if writing_ys:
        pygame.draw.rect(screen, WHITE,(687, 537, 154,26),width = 1)
    pygame.draw.rect(screen, BLACK, Rect_k)
    if writing_k:
        pygame.draw.rect(screen, WHITE,(687, 582, 154, 26),width = 1)
    font = pygame.font.SysFont("Times", 25)
    text = font.render("Задержка времени Δt:",True, BLACK)
    screen.blit(text, (30,582))
    text = font.render("x:",True, BLACK)
    screen.blit(text, (35,537))
    text = font.render("y:",True, BLACK)
    screen.blit(text, (240,537))
    text = font.render("x:",True, BLACK)
    screen.blit(text,(455,537))
    text = font.render("y:",True,BLACK)
    screen.blit(text, (660,537))
    text = font.render("Коэф. сопротивления:",True,BLACK)
    screen.blit(text,(450,582))
    text = font.render(user_x,True,WHITE)
    screen.blit(text,(63,537))
    text = font.render(user_y,True,WHITE)
    screen.blit(text,(268,537))
    text = font.render(user_t,True,WHITE)
    screen.blit(text,(268,582))
    text = font.render(user_x , True,WHITE)
    screen.blit(text,(483,537))
    text = font.render(user_ys,True,WHITE)
    screen.blit(text,(688,537))
    text = font.render(user_k, True, WHITE)
    screen.blit(text,(688,582))


def changeCoord(user_x,user_y, user_t,user_ys, user_k):
    global x, y, xs,ys, dt, k
    dot = False
    x, y, dt, ys, k = 0, 0, 0, 0, 0
    p = 1
    for i in user_x:
        if i == '.':
            dot = True
        else:
            if not dot:
                x = x*10 + int(i)
            else:
                x += int(i)/(10*p)
                p+=1
    dot = False
    p = 1
    for i in user_y:
        if i == '.':
            dot = True
        else:
            if not dot:
                y = y*10 + int(i)
            else:
                y += int(i)/(10*p)
                p+=1
    dot = False
    p = 1
    for i in user_ys:
        if i == '.':
            dot = True
        else:
            if not dot:
                ys = ys*10 + int(i)
            else:
                ys += int(i)/(10*p)
                p+=1
    dot = False
    p = 1
    for i in user_k:
        if i == '.':
            dot = True
        else:
            if not dot:
                k = k*10 + int(i)
            else:
                k += int(i)/(10*p)
                p+=1
    minus = False
    dot = False
    p = 1
    for i in user_t:
        if i == '.':
            dot = True
        elif i == '-':
            minus = True
        if not i == '-' and not i == '.':
            if minus:
                if not dot:
                    dt = dt*10 - int(i)
                else:
                    dt -= int(i)/(10*p)
                    p+=1
            else:
                if not dot:
                    dt = dt*10 + int(i)
                else:
                    dt += int(i)/(10*p)
                    p+=1

    x = x+20
    y = 500-y
    ys = 500-ys
    xs = x
    if y >ys:
        ys = y+8
        user_ys = str(500-ys)



pygame.init()
screen = pygame.display.set_mode((1280, 720))
x = 100
y = 100
ys = 120
dt = 0
k = 0
center = (20,500)
clock = pygame.time.Clock()

RED = (255,0,0)
BLUE = (90,90,90)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (100,100,100)

moving1 = False
moving2 = False
moving_t = False
Resistance = True

writing_x = False
writing_y = False
writing_ys = False
writing_xs = False
writing_t = False
writing_k = False

change = False

user_x = str(-center[0]+x)
user_y = str(center[1]-y)
user_ys = str(center[1]-y-20)
user_xs = user_x
user_t = '0'
user_k = '0'

# Rect_x = pygame.Rect(60,510,160,30)
# Rect_y = pygame.Rect(60,545,160,30)
# Rect_t = pygame.Rect(60,580,160,30)
# Rect_xs = pygame.Rect(225, 510, 160, 30)
# Rect_ys = pygame.Rect(225, 545, 160, 30)
# Rect_k = pygame.Rect(225, 580, 160, 30)
Rect_x = pygame.Rect(60,535,160,30)
Rect_y = pygame.Rect(265, 535, 160, 30)
Rect_xs = pygame.Rect(480, 535, 160, 30)
Rect_ys = pygame.Rect(685, 535, 160, 30)
Rect_t = pygame.Rect(265,580,160,30)
Rect_k = pygame.Rect(685, 580, 160, 30)
t_pos_y = 697
t_pos_x = 100
Slider_t = pygame.Rect(100, 700, 900, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            r = pygame.Rect(t_pos_x, t_pos_y, 4, 7)
            if ((event.pos[0] - x)**2 + (event.pos[1] - y)**2)**(1/2) < 5:
                moving1 = True
            if ((event.pos[0] - x)**2 + (event.pos[1] - ys)**2)**(1/2) < 3:
                moving2 = True
            if Rect_x.collidepoint(event.pos):
                writing_x = True
            if Rect_y.collidepoint(event.pos):
                writing_y = True
            if Rect_t.collidepoint(event.pos):
                writing_t = True
            if Rect_ys.collidepoint(event.pos):
                writing_ys = True
            if Rect_k.collidepoint(event.pos):
                writing_k = True
            if r.collidepoint(event.pos):
                moving_t = True
            if not Rect_y.collidepoint(event.pos):
                writing_y = False
            if not Rect_x.collidepoint(event.pos):
                writing_x = False
            if not Rect_t.collidepoint(event.pos):
                writing_t = False
            if not Rect_ys.collidepoint(event.pos):
                writing_ys = False
            if not Rect_k.collidepoint(event.pos):
                writing_k = False

        if event.type == pygame.MOUSEMOTION and moving1:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if pygame.mouse.get_pos()[1] > 492:
                y = 492
                ys = 500
            elif pygame.mouse.get_pos()[1] > ys-8:
                y = pygame.mouse.get_pos()[1]
                ys = y+8
            user_x =str(x-center[0])
            user_y = str(center[1] - y)
            user_ys = str(center[1]-ys)
            user_xs = user_x

        if event.type == pygame.MOUSEMOTION and moving2:
            ys = pygame.mouse.get_pos()[1]
            if pygame.mouse.get_pos()[1] < y+8:
                ys = y+8
            if pygame.mouse.get_pos()[1] > 500:
                ys = 500
            user_ys = str(500-ys)

        if event.type == pygame.MOUSEMOTION and moving_t:
            t_pos_x = pygame.mouse.get_pos()[0]
            if t_pos_x > 1000:
                t_pos_x = 997
            if t_pos_x < 100:
                t_pos_x = 100

        if event.type == pygame.MOUSEBUTTONUP:
            moving1 = False
            moving2 = False
            moving_t = False

        if event.type == pygame.KEYDOWN:
            if writing_x:
                user_x += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    user_x = user_x[:-2]
                if event.key == pygame.K_ESCAPE:
                    user_x = user_x[:-1]
                if event.key == pygame.K_RETURN:
                    writing_x = False
                    user_x = user_x[:-1]
                    change = True
            if writing_y:
                user_y += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    user_y = user_y[:-2]
                if event.key == pygame.K_ESCAPE:
                    user_y = user_y[:-1]
                if event.key == pygame.K_RETURN:
                    writing_y = False
                    user_y = user_y[:-1]
                    change = True
            if writing_ys:
                user_ys += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    user_ys = user_ys[:-2]
                if event.key == pygame.K_ESCAPE:
                    user_ys = user_ys[:-1]
                if event.key == pygame.K_RETURN:
                    writing_ys = False
                    user_ys = user_ys[:-1]
                    change = True
            if writing_k:
                user_k += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    user_k = user_k[:-2]
                if event.key == pygame.K_ESCAPE:
                    user_k = user_k[:-1]
                if event.key == pygame.K_RETURN:
                    writing_k = False
                    user_k = user_k[:-1]
                    change = True
            if writing_t:
                user_t += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    user_t = user_t[:-2]
                if event.key == pygame.K_ESCAPE:
                    user_t = user_t[:-1]
                if event.key == pygame.K_RETURN:
                    writing_t = False
                    user_t = user_t[:-1]
                    change = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                removing = False

    screen.fill(WHITE)
    if change:
        changeCoord(user_x,user_y, user_t,user_ys, user_k)
        change = False
    drawFor()
    drawSlider()
    drawParabola()
    drawKnopki()
    pygame.display.flip()
    clock.tick(60)
