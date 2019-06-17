from turtle import *

Ryan = Turtle()

Ryan.color("yellow")
Ryan.pensize(12)
Ryan.speed(10)
Ryan.shape("turtle")
 
screen = Screen()
screen.bgcolor("red")

Ryan.forward(80)
Ryan.right(50)
Ryan.forward(200)
Ryan.left(150)
Ryan.forward(50)
Ryan.circle(25)
Ryan.backwards(300)

mainloop()