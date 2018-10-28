from turtle import Turtle

def init_drawman():
    global t, x_current, y_current, _drawman_scale_x, _drawman_scale_y
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(10, 10)

def drawman_scale(scale_x, scale_y):
    global _drawman_scale_x, _drawman_scale_y
    _drawman_scale_x = scale_x
    _drawman_scale_y = scale_y

def test_drawman():
    """чертежник"""
    pen_down()
    for i in range(5):
        on_vector(10, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current, _drawman_scale_x, _drawman_scale_y
    x_current = x
    y_current = y
    t.goto(_drawman_scale_x * x_current,_drawman_scale_y * y_current)

def axes_y(x, y):
    pen_up()
    to_point(x, -y)
    pen_down()
    to_point(x, y)
    pen_up()
    to_point(x, 0)    

def axes_x(x, y):
    pen_up()
    to_point(-x, y)
    pen_down()
    to_point(x, y)
    pen_up()
    to_point(0, y)
    
def grid(x_step, x_max, y_step, y_max):
    global t, _drawman_scale_x, _drawman_scale_y
    color_mem = t.color()
    print(str(color_mem), type(color_mem))
    t.color('black')
    axes_y(0, y_max)
    axes_x(x_max, 0)

    t.color('grey')
    i = x_step 
    while i <= x_max:
        axes_y(i, y_max)
        i += x_step 
    i = -x_step 
    while i >= -x_max:
        axes_y(i, y_max)
        i -= x_step

    i = y_step 
    while i <= y_max:
        axes_x(x_max, i)
        i += y_step 
    i = -y_step 
    while i >= -y_max:
        axes_x(x_max, i)
        i -= y_step
    t.color(color_mem[0])

init_drawman()
if __name__ == '__main__':
    import time
    test_drawman()
    #time.sleep(0.5)
