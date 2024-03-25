
import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")

def shirinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5


shirinkingSquare(150)
shirinkingSquare(130)
shirinkingSquare(110)
shirinkingSquare(90)
shirinkingSquare(70)
shirinkingSquare(50)
shirinkingSquare(30)
shirinkingSquare(10)

turtle.done()