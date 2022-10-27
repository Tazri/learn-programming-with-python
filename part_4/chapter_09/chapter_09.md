Chapter 09: Some More OOP
=========================
Table of content : 
- [Chapter 09: Some More OOP](#chapter-09-some-more-oop)
  - [Magic Method](#magic-method)
  - [Plus Operator Overloading](#plus-operator-overloading)
  - [x.\_\_repr\_\_()](#x__repr__)
  - [Priority Decoretor](#priority-decoretor)
  - [Abstract Base Class](#abstract-base-class)
  - [Static Method](#static-method)
  - [Class Method](#class-method)
  - [Data class](#data-class)
  - [Multiple Inheritance](#multiple-inheritance)
  - [Mixin](#mixin)

## Magic Method
In python which method name start with **\_\_** and end with **\_\_** called magic method. Here some magic method use case : 

***Program : \_\_len\_\_()***

```bash
>>> x = 'Bangladesh'
>>> # len is magic method which return length of string or list or tuple or dict
>>> x.__len__()
10
>>> x = [1,2,3]
>>> x.__len__()
3
>>> x = { 'a' : 'A', 'b' : 'B'}
>>> x.__len__()
2
>>> 
```

***Program : \_\_str\_\_()***
```bash
>>> x = 100
>>> str(x)
'100'
>>> # __str__() magic method convert something to string
>>> x.__str__()
'100'
>>> 
```

***Program : \_\_add\_\_()***
```bash
>>> x = 100
>>> y = 10
>>> # a.__add__(b) magic method overloaded the + operator. 
>>> x.__add__(y)
110
>>> a = 'bangladesh'
>>> a = 'Bangla'
>>> b = 'desh'
>>> a.__add__(b)
'Bangladesh'
>>> 
```
<hr />
<br />


## Plus Operator Overloading

We can overload **+** operator with **\_\_add\_\_(x)** magic method. Here example : 

***Program : plus_overload.py***
```python
class Point : 
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y) + ')'

    def __add__(self,point):
        self.x += point.x;
        self.y += point.y;
        return self;

if __name__ == "__main__":
    point_one = Point(2,4);
    print('point_one :',point_one);
    point_two = Point(1,1);
    print("point_two : ",point_two);

    print("after point_one + point_two : point_one");
    added_point = point_one + point_two;
    print(added_point);
```

***Output : plus_overload.py***
```bash
point_one : Point(2,4)
point_two :  Point(1,1)
after point_one + point_two : point_one
Point(3,5)
```

<hr />
<br />

## x.\_\_repr\_\_()
__repr__() magic method return a string always which is consider a output of object when it printed. Here example : 

***Program : repr.py***
```python
class Greeting :
    def __init__(self,name:str):
        self.name = name;

    # __repr__ return the output
    def __repr__(self)->str:
        return "Hello, " + self.name + "!";

if __name__ == "__main__" :
    me = Greeting("Anonymous");
    print(me);
```

***Output : repr.py***
```bash
Hello, Anonymous!
```

<hr />
<br />

## Priority Decoretor 
Must of the programming language has 3 type of class instance variable. Here : 

1. Public
2. Private
3. Protected

But in python there is no **private** or **protected** instance variable. Here everything is public. We can use single underscore starting of the variable name for mean that this is private variable and suggest that don't change it. Must of the programming language has two method for reading and changing private variable. **getter** for reading and **setter** for changing.  But python has **@property** decorator for this. here example : 

***Program : property_decorator.py***
```python
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
```

***Output : property_decorator.py***
```bash
35000.0
38454.33
>>> Invalid data for price.
38454.33
```

<hr />
<br />

## Abstract Base Class
In python create abstract class by using **abc** module. Here example : 


***Program : abstract_method.py***
```python
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
```

***Output : abstract_method.py***
```bash
Creating a car
Camry
Turning :  Camry to left
Changing gear to D
```

<hr />
<br />

## Static Method
Some time we need to create a method which dose not work with object of class. This type of method called **static method**. We can create this by **@staticmethod** decorator. Here example : 

***Program : static_method.py***
```python
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
```

output : 

```bash 
Car.kph_to_mph(293 :  293000
```

<hr />
<br />

## Class Method
Must of the time we need to create a method which has not releated with speacify object but it use one or more property or method of class. This type of method called **classmethod**. We do it in python by using **@classmethod** decorator. Example : 

***Program : class_method.py***
```python
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
```

output : class_method.py
```bash
Creating Car
Creating Car
Creating Car
Creating Car
Car Count :  4
Car Count :  0
Creating Car
Creating Car
Creating Car
Creating Car
Creating Car
Car Count :  5
Car Count :  0
```

<hr />
<br />

## Data class
**Data class** is one type of class where only store attribute nothing else. We can do this in python by using **@dataclass** decorator easily. This property from **dataclasses** module. In this way we don't need to create **\_\_init\_\_()** method or **\_\_repr\_\_()** method. Here example : 


***Program : data_class.py***
```python
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
```

output : data_class.py
```bash
Car(name='Camry', manufacturer='Toyota', year=2020, price=35000)
car_one == car_two :  True
car_one == car_three :  False
```

We can sort them using their price. In that case pass **order=True** in **@dataclass** decorator and create **sort_index** property and set value **field(init=False,repr=False)**. This **field()** funciton is found in **dataclass** module. Create **\_\_post_init\_\_(self)** method. Where set the **self.sort_index** to attribute which attribute use for sorting. That it. Here example :

***Program : sorted_data_class.py***
```python
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
```

output : sorted_data_class.py
```bash
Car(name='Camry', manufacturer='Toyota', year=2020, price=38000)
Car(name='Prado', manufacturer='Toyota', year=2021, price=70000)
Car(name='Corolla', manufacturer='Toyota', year=2021, price=32000)
car_one > car_two :  False
car_two > car_three :  True
```

<hr />
<br />

## Multiple Inheritance
In python support multiple inheritance. Here example : 

```bash

>>> class A : 
...     def fnc(self):
...             print("Hello from A")
... 
>>> class B :
...     def fnc(self):
...             print("Hello from B")
... 
>>> 
>>> # c inherit from A and B
>>> class C(A,B):
...     pass
... 
>>> obj = C()
>>> obj.fnc()
Hello from A
>>> 
>>> # D inherit from B and A
>>> class D(B,A):
...     pass;
... 
>>> obj = D();
>>> obj.fnc()
Hello from B
>>> 
```

If Inheritor classes has implemant same method and which method work in decide called **method resolution order**. If we want to see this then called **mro()** method. Here example : 

```bash
>>> D.mro()
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
>>> 
```
If **B** and **C** inherit **A** and **D** inherit **B** and **C** together. It called Diamond problem Here what happend in that case if a method has in **A** but not in **D** but called it from **D**. Here example : 

```bash
class A:
    def __init__(self):
        self.name = "A";
        
    def hello(self):
        print("Hello from",self.name);
        
class B(A):
    def __init__(self):
        self.name = 'B';

class C(A):
    def __init__(self):
        self.name = "C";

class D(B,C):
    pass
        
obj = D();
obj.hello()
print("D.mro():");
print(D.mro());
```

<hr />
<br />

## Mixin
