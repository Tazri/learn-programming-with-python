class Car :
    def __init__(self,n,c) :
        self.name = n;
        self.color = c;

    def start(self) :
        print("> name : ",self.name);
        print("> color : ",self.color);
        print("> Car is Starting <");

my_car = Car("Corolla","white");
my_car.start();
Car.start(my_car);

my_car.year = 2017;
print("my_car.year : ",my_car.year);