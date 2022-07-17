class Car :
    def __init__(self,n,c) :
        self.name = n;
        self.color = c;
    

    def start(self) :
        print(">>> Car is Starting <<<");


my_car = Car("Corolla","White");
print(my_car.name);
print(my_car.color);
my_car.start();