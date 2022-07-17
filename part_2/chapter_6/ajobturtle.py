import turtle

class Ajobturtle(turtle.Turtle) :
    def forward(self,pixel) :
        super().backward(pixel);

    def backward(self,pixel) :
        super().forward(pixel);

    def left(self,angle) :
        super().right(angle);

    def right(self,angle) :
        super().left(angle);


if __name__ == "__main__" :
    montu = Ajobturtle();
    jhontu = turtle.Turtle();

    montu.color('blue');
    jhontu.color('red');

    montu.shape("turtle");
    jhontu.shape("classic");

    montu.left(30);
    jhontu.left(30);

    montu.forward(200);
    jhontu.forward(200);
    
    montu.left(45);
    jhontu.left(45);

    montu.backward(100);
    jhontu.backward(100);

    montu.right(90);
    jhontu.right(90);

    montu.forward(10);
    jhontu.forward(10);

    
    turtle.done();