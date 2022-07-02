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

for i in range(30) :
    color = color_list[random.randint(0,len(color_list) - 1)]; 
    x,y = random.randint(-200,200),random.randint(-200,200);

    turtle.color(color);
    turtle.setposition(x,y);
    turtle.dot();

turtle.done();