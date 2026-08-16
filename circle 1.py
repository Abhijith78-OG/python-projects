from turtle import*
import colorsys as cs
bgcolor("black")
tracer(30)
pensize(2)
h=0
for i in range(200):
    c=cs.hsv_to_rgb(h,1,1)
    h+=0.011
    pencolor(c)
    circle(i,100)
    rt(50)
    begin_fill()
    circle(i,90)
    end_fill()
    rt(25)
    circle(10,70)
done()
    
