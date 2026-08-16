from turtle import*
from colorsys import*
bgcolor("black")
tracer(10)
h=0.7
goto(130,250)
for i in range(900):
     c=hsv_to_rgb(h,1,1)
     color(c)
     begin_fill()
     circle(-40,60)
     forward(10-i*0.1)
     left(50)
     end_fill()
     h+=1/37
done()
