from turtle import*
from colorsys import*
bgcolor("black")
tracer(10)
pensize(2)
h=0
for i in range(120):
    c=hsv_to_rgb(h,1,1)
    h+=0.009
    color(c)
    up()
    goto(-8,0)
    down()
    fd(i)
    rt(89)
    fillcolor(c)
    begin_fill()
    circle(90,100)
    end_fill()
    lt(179)
    bk(i/2)
    lt(6)
done()
