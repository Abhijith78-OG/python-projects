from turtle import*
from colorsys import*
tracer(10)
bgcolor("black")
pensize(2)
h=0
for i in range(240):
    c=hsv_to_rgb(h,1,1)
    h+=0.005
    color(c)
    fillcolor("black")
    begin_fill()
    for j in range (1):
        fd(i/2)
        rt(30)
        fd(i)
        rt(120)
        rt(1020013)
        end_fill()
done()
