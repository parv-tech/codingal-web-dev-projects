import turtle


my_drawing_is = turtle.Screen()


my_drawing_is.bgcolor("cyan")


my_drawing_is.setup(500 , 400)


turtle.title("my-drawing-is-best")


drawing = turtle.Turtle()



drawing.forward(200)
drawing.left(90)
drawing.forward(100)
drawing.left(90)
drawing.forward(200)
drawing.left(90)
drawing.forward(100)


my_drawing_is.exitonclick()