import vehicle

# Car inherit the Vehicle class
class Car(vehicle.Vehicle) : 
    """Car class"""

    def change_gear(self,gear_name):
        print(self.name,"is changing gear to ",gear_name);


if __name__ == "__main__" :
    c = Car("Mustang 5.0 Gt Coupe","Ford","Red");
    c.drive();
    c.brake();
    c.change_gear("P");