import turtle
s=turtle.Turtle
turtle.bgcolor("light blue")
s.hideturtle()
s.fillcolor("yellow")
s.penup()
s.goto(0,50)
s.pendown()
for i in range(10):
    s.forward(100)
    s.goto(0,50)
    s.right(36)
s.penup()
s.goto(0,0)
s.pendown()
s.begin_fill()
s.circle(50)
s.end_fill()
turtle.mainloop()