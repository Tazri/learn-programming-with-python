import turtle

def draw_square(side_length) : 
    for i in range(4) : 
        turtle.forward(100);
        turtle.left(90);

counter = 0;

turtle.color("red");
while counter < 90 : 
    draw_square(100);
    turtle.right(4);
    counter += 1;

turtle.exitonclick();