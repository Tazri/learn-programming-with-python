class Car :
    name = "";
    color = "";

    def start(self) :
        print(">>> Car Engine is Starting.. <<<");


# creating a Car object
my_car = Car();
my_car.name = "ALlion";
print(my_car.name);
my_car.start();