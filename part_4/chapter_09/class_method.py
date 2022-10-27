class Car():
    count = 0;
    
    def __init__(self,name,company,color,price):
        print("Creating Car");
        self.name = name;
        self.company = company;
        self.color = color;
        self._price = price;
        
        # increase static property
        Car.count += 1;
    
    # class method
    @classmethod
    def display_count(cls):
        print("Car Count : ",cls.count);
    
    # class method
    @classmethod
    def reset_count(cls):
        cls.count = 0;
    
    # class method
    @classmethod
    def reset_display_count(cls):
        cls.reset_count();
        cls.display_count();
        
if __name__ == '__main__':
    mycar_one = Car('camry','Toyota','black',23564.54);
    mycar_four = Car('camry','Toyota','black',23564.54);
    mycar_three = Car('camry','Toyota','black',23564.54);
    mycar_five = Car('camry','Toyota','black',23564.54);
    
    Car.display_count();
    Car.reset_count();
    Car.display_count();
    
    # create car again
    car_one = Car("Tesla","Tesla","Whie",35000.43);
    car_two = Car("Tesla","Tesla","Whie",35000.43);
    car_three = Car("Tesla","Tesla","Whie",35000.43);
    car_five = Car("Tesla","Tesla","Whie",35000.43);
    car_six = Car("Tesla","Tesla","Whie",35000.43);
    
    Car.display_count();
    Car.reset_display_count();