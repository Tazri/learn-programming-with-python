from abc import ABC, abstractmethod

# vehicle inherit ABC
class Vehicle(ABC):
    def __init__(self,name,manufacturer,color):
        self.name = name;
        self.manufacturer = manufacturer;
        self.color = color;

    def turn(self,direction):
        print("Turning : ",self.name,"to",direction);
    
    # Abstract method
    @abstractmethod
    def change_gear(self,gear):
        pass;

class Car(Vehicle) :
    def __init__(self,name,manufacturer,color,year):
        print("Creating a car");
        super().__init__(name,manufacturer,color);
        self.year = year;

    # implemant abstract class
    def change_gear(self, gear):
        print("Changing gear to",gear);


if __name__ == "__main__":
    # below line must be throw error because Vehicle is a abstract class
    # mycar = Vehicle("Camry","Toyota","white")

    mycar = Car('Camry','Toyota','White',2020);
    print(mycar.name);
    mycar.turn('left');
    mycar.change_gear('D');

    