import turtle

turtle.color("black");
turtle.shape("turtle");
turtle.speed(4);

counter = 0;
while counter < 36 : 
    for i in range(4) : 
        turtle.forward(100);
        turtle.right(90);
    turtle.right(10);
    counter += 1;

turtle.exitonclick();