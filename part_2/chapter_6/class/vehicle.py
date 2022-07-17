class Vehicle :
    def __init__(self,name,manufacturer,color) : 
        print("Creating a vehicle");
        self.name = name;
        self.manufacturer = manufacturer;
        self.color = color;

    def drive(self) :
        print("Driving",self.manufacturer,self.name);
    
    def turn(self,direction) :
        print("Turning",self.name,"to",direction);

    def brake(self) :
        print(self.name,"is stopping!");


if __name__ == "__main__":
    v1 = Vehicle('tesla_1','tesla','red');

    v1.drive();
    v1.turn('left');
    v1.brake();