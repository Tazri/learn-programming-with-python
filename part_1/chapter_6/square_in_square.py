import turtle

turtle.shape("turtle");
turtle.color("red");
turtle.speed(1);

for side_length in range(60,140,10) : 
    for i in range(4) : 
        turtle.forward(side_length);
        turtle.left(90);

turtle.exitonclick();