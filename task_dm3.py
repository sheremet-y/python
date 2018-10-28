from drawman import *

def f(x):
    return x*x*x

drawman_scale(50, 8)
x = -3.0
grid(1.0, 3, 10.0, f(3))
to_point(x, f(x))

pen_down()
while x < 3:
    to_point(x, f(x))
    x += 0.1
pen_up()

