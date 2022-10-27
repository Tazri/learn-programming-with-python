class Car : 
    def __init__(self,name:str,manufacturer:str,year:int,price:float=None) -> None:
        self.name = name;
        self.manufacturer = manufacturer;
        self.year = year;
        self._price = price

    # getter
    @property
    def price(self):
        return self._price

    # setter
    @price.setter
    def price(self,new_price):
        if not isinstance(new_price,(float)):
            print(">>> Invalid data for price.");
        elif new_price < 0 : 
            print("Price can't be negative");
        else : 
            self._price = new_price;
    
    # deleter for delete price
    @price.deleter
    def price(self):
        self._price = None;

if __name__ == "__main__":
    car = Car("Camry","Toyota",2022,35000.0);
    print(car.price);
    car.price = 38454.33;
    print(car.price);
    car.price = '100';
    print(car.price);