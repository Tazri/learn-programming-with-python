import turtle,random

color_list = [
    "red",
    "yellow",
    "black",
    "crimson",
    "blue",
    "cyan",
    "pink",
    "orange",
    "tan"   
]

turtle.penup()

for i in range(50) : 
    turtle.color(color_list[random.randint(0,len(color_list) - 1)]);
    x,y = random.randint(-150,150),random.randint(-150,150);
    turtle.setposition(x,y);
    turtle.dot();

turtle.exitonclick();