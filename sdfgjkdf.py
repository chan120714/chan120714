from turtle import*
from math import*
from random import*
penup()
r=[]
def radius(n,m):#n=꼭짓점의 갯수,m=한변의 길이
    return (m/2)*(1/(sin(pi/n)))

def is_pile_up(x1,y1,r1,x2,y2,r2):
    if x1==x2 and y1==y2:#x좌표와 y좌표가 같은경우
        return False
    n=sqrt((x2-x1)**2+(y2-y1)**2)
    if n>abs(r1-r2) and n<abs(r1+r2):#두점이 접하는 경우
        return False
    elif n==abs(r1+r2) or n==abs(r1-r2):#접하는 경우
        return False
    elif n>abs(r1+r2) or n<abs(r1-r2):#접하지 않는 경우
        return True
    return False#그외
def inside(x1,y1,r1,x2,y2):
    if (x1-x2)**2+(y1-y2)**2<=r1**2:
        return False
    return True
def draw():
    n=randint(3,20)
    m=randint(3,20)
    x,y=randint(-500,500),randint(-300,300)
    r1=ceil(radius(n,m))
    for i in r:
        if not is_pile_up(x,y,r1,*i) or not inside(x,y,r1,i[0],i[1]) or not inside(*i,x,y):
            return draw()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(n):
        forward(m)
        right(360/n)
    r.append([x,y,ceil(r1*1.4)])
    end_fill()
    penup()
n=int(input())
speed(0)
for i in range(n):
    draw()
