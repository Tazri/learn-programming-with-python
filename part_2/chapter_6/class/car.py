from vehicle import Vehicle

class Car(Vehicle):
    # Car class
    def __init__(self,name,manufacturer,color,year) :
        super().__init__(name,manufacturer,color);
        self.year = 2017;
        self.wheels = 4;
        print("A new has been created. Name : ",self.name);
        print("It has",self.wheels,"wheels");

    def change_gear(self,gear_name) :
        print(self.name,"is changing gear to",gear_name);

    def turn(self,direction) :
        print(self.name,"car is turning",direction)

if __name__ == "__main__" :
    c = Car("Mustang 5.0 GT Coupe","Ford","Red",2017);
    v = Vehicle("Softail Delux","Harley-Davidson","Blue");

    c.turn('right');
    v.turn('right');