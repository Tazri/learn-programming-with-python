import turtle

shapes = [
    'arrow',
    'turtle',
    'circle',
    'square',
    'triangle',
    'classic'
]

color = [
    'red',
    'blue',
    'green',
    'crimson',
    'purple',
    'black'
]


move = 100;
angle = 180 - 120;

turtle.speed(1);
for i in range(len(shapes)) : 
    turtle.shape(shapes[i]);
    turtle.color(color[i]);
    turtle.forward(move);
    turtle.right(angle);

turtle.exitonclick();