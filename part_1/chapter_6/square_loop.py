import turtle

move = 100;

turtle.shape("turtle");
turtle.color('red');
turtle.speed(1);

for i in range(4) : 
    turtle.forward(move);
    turtle.left(90);

turtle.exitonclick();