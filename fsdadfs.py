from turtle import*
from random import*
speed(1000)
up()
ht()
goto(-350,210)
for i in range(20):
    pendown(),write(i,font=('',20));fd(15)
    pu();right(90);fd(30);pd();fd(500);right(180);pu();fd(530);right(90);fd(15)
t0=Turtle()
t0.shape("turtle")
t0.color('red')
t0.up();t0.goto(-350,100);t0.down()

t1=Turtle()
t1.shape("turtle")
t1.color('blue')
t1.up();t1.goto(-350,20);t1.down()

t2=Turtle()
t2.shape("turtle")
t2.color('green')
t2.up();t2.goto(-350,-60);t2.down()

t3=Turtle()
t3.shape("turtle")
t3.color('yellow')
t3.up();t3.goto(-350,-140);t3.down()

t4=Turtle()
t4.shape("turtle")
t4.color('black')
t4.up();t4.goto(-350,-220);t4.down()

win=[0,50,100,150,200]
while 1:
    x1=randint(2,20)
    if t0.xcor()<240:
        t0.fd(x1)
        if t0.xcor()>=240:
            t0.fd(win.pop())
    x1=randint(2,20)
    if t1.xcor()<240:
        t1.fd(x1)
        if t1.xcor()>=240:
            t1.fd(win.pop())
    x1=randint(2,20)
    if t2.xcor()<240:
        t2.fd(x1)
        if t2.xcor()>=240:
            t2.fd(win.pop())
    x1=randint(2,20)
    if t3.xcor()<240:
        t3.fd(x1)
        if t3.xcor()>=240:
            t3.fd(win.pop())
    x1=randint(2,20)
    if t4.xcor()<240:
        t4.fd(x1)
        if t4.xcor()>=240:
            t4.fd(win.pop())
    if len(win)==0:
        break
