from dataclasses import dataclass

@dataclass
class Car:
    name:str;
    manufacturer:str;
    year:int;
    price:int;
    
if __name__ == "__main__":
    car_one = Car("Camry","Toyota",2020,35000);
    car_two = Car("Camry","Toyota",2020,35000);
    car_three = Car("Tesla","Tesla",2022,34000);
    print(car_one);
    
    print("car_one == car_two : ",car_one == car_two);
    print("car_one == car_three : ",car_one == car_three);