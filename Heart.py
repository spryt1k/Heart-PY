from turtle import*
import math

def ha(x):
    return 15*math.sin(x)**3
def hb(x):
    return 12*math.cos(x)-5*\
           math.cos(2*x)-2*\
           math.cos(3*x)-\
           math.cos(4*x)
speed(3000)
bgcolor("black")
for i in range(6000):
    goto(ha(i)*20,hb(i)*20)
    for j in range(5):
        color("#FF0000")
    goto(0,0)
done()
