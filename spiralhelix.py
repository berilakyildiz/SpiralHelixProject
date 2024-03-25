import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_instance = turtle.Turtle()
turtle.speed(10)
turtle_colors = ['red', 'green', 'blue', 'pink', 'orange', 'yellow']

for i in range(15):
    turtle_instance.color(turtle_colors[i %6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.done()
