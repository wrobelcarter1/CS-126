import turtle
# sets up the intial window
turtle.setup(500,500)
# move turtle forward - draws a black line by default
turtle.fd(100)
# turn right
turtle.rt(90)
# move foward again...
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)
turtle.rt(90)
turtle.fd(100)
# remember you can make a function called draw_square
def draw_square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
# tell turtle to get ready to fill shape
turtle.begin_fill()
# set color to fill with
turtle.fillcolor('yellow') 
# draw the square
draw_square(100)
# done filling color
turtle.end_fill()
# set background color
turtle.bgcolor('navy')
# move turtle to a new position
turtle.pu()       # pick up the pen (to move without drawing)
turtle.goto(200, -200)    # move to new location
turtle.pd()       # put the pen back down (to draw again)
turtle.begin_fill()
turtle.fillcolor('white')
draw_square(25)   # draw a smaller square
turtle.end_fill()
# finsihed drawing so the turtle is done
turtle.done()
