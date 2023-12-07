import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


choice = input('Which art do you want to generate? Enter a number between 1 to 8, '
                   'inclusive: ')

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location


def new_position():
    turtle.penup()
    turtle.forward(size*(1-reduction_ratio)/2)
    turtle.left(90)
    turtle.forward(size*(1-reduction_ratio)/2)
    turtle.right(90)
    location[0] = turtle.pos()[0]
    location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

if choice == '1':
    for i in range(30):
        draw_polygon(3,  random.randint(50, 150), random.randint(0, 90), [random.randint(-300, 300), random.randint(-200, 200)], get_new_color(), random.randint(1, 10))
        new_position()
if choice == '2':
    for i in range(30):
        draw_polygon(3, random.randint(50, 150), random.randint(0, 90),
                     [random.randint(-300, 300), random.randint(-200, 200)], get_new_color(), random.randint(1, 10))
        new_position()
if choice == '3':
    draw_polygon(5, size, orientation, location, color, border_size)


# draw the second polygon embedded inside the original
draw_polygon(num_sides, size, orientation, location, color, border_size)


# hold the window; close it by clicking the window close 'x' mark
turtle.done()

