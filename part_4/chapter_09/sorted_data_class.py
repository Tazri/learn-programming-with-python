from dataclasses import dataclass, field

@dataclass(order=True)
class Car:
    # set the sort index to filed(init=False,repr=False);
    sort_index: int = field(init=False,repr=False);
    name:str;
    manufacturer:str;
    year:int;
    price:int;
    
    def __post_init__(self):
        self.sort_index = self.price; # here use a attribute which is using for sorting. 
    
if __name__ == "__main__":
    car_one = Car("Camry","Toyota",2020,38000);
    car_two = Car("Prado","Toyota",2021,70000);
    car_three = Car("Corolla","Toyota",2021,32000);
    print(car_one);
    print(car_two);
    print(car_three);
    print("car_one > car_two : ",car_one > car_two);
    print("car_two > car_three : ",car_two > car_three);