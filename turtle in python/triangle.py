import turtle


my_drawing_is = turtle.Screen()


my_drawing_is.bgcolor("cyan")


my_drawing_is.setup(500 , 400)


turtle.title("my-drawing-is-best")


drawing = turtle.Turtle()



drawing.forward(200)
drawing.left(135)
drawing.forward(150)
drawing.left(92)
drawing.forward(150)


my_drawing_is.exitonclick()