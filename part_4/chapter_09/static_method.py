class Car():
    def __init__(self,name,company,color,price):
        print("Creating Car");
        self.name = name;
        self.company = company;
        self.color = color;
        self._price = price;
    
    # here static method which dose not take a self. 
    @staticmethod
    def kph_to_mph(number):
        return number*1000;
        
if __name__ == '__main__':
    distance = Car.kph_to_mph(293);
    print("Car.kph_to_mph(293 : ",Car.kph_to_mph(293));