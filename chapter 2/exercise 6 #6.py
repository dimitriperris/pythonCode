import turtle

turtle.pensize(5)

turtle.color("black")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(30)

turtle.color('black')
turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.forward(150)

turtle.color('black')
turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.forward(-150)

turtle.color("black")
turtle.penup()
turtle.goto(0,30)
turtle.pendown()
turtle.left(90)
turtle.forward(150)

turtle.color('black')
turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.right(180)
turtle.forward(150)

turtle.penup()
turtle.hideturtle()
turtle.goto(-15, 190)
turtle.write("North", font = 16)
turtle.goto(-15, -150)
turtle.write("South", font = 16)
turtle.goto(160, 25)
turtle.write('West', font = 16)
turtle.goto(-190, 25)
turtle.write('East', font = 16)

turtle.getscreen()._root.mainloop()