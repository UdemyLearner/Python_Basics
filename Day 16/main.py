import turtle

tuktuk = turtle.Turtle()
print(tuktuk)
tuktuk.shape("turtle")
tuktuk.clone()
tuktuk.forward(100.0)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
