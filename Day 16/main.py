from msilib.schema import tables
import turtle
import prettytable


tuktuk = turtle.Turtle()
print(tuktuk)
tuktuk.shape("turtle")
tuktuk.clone()
tuktuk.forward(100.0)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = prettytable.PrettyTable()
table.add_column("Pokemon",["Pickachu","Squirtel","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="r"
print(table.align)
print(table)