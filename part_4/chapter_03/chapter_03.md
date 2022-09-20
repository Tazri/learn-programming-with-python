Chapter 03 : Decorator
======================

Table of Content : 
- [Chapter 03 : Decorator](#chapter-03--decorator)
  - [Decorator](#decorator)
  - [Decorator with Perameter](#decorator-with-perameter)
  - [Decorator Keyword](#decorator-keyword)
  - [Create Timeit Decorator](#create-timeit-decorator)
  - [\_\_call\_\_](#__call__)
  - [Class Decorator](#class-decorator)
  - [< Go Back](#-go-back)

## Decorator
Decorator is one kind of function which can take a function and add some functionality and return it. Here simple example of decorator : 

**Python : decorator_function.py**
```python
def decorator(func):
    def wrapper():
        print("Here work some functionality before call function.");
        
        print("function calling.");
        func();
        
        print("\nafter the function here work some functionality after call function.");
    
    return wrapper
def hello():
    print("\n>>> Hello, I am Hello function.");
    
fnc = decorator(hello);

print("fnc : ",fnc,"\n");
fnc();
```
output : 
```
fnc :  <function decorator.<locals>.wrapper at 0x7f0ab98f7e50> 

Here work some functionality before call function.
function calling.

> Hello, I am Hello function.

after the function here work some functionality after call function.
```

<hr />
<br />

## Decorator with Perameter
Here example of creating decorator function with perameter. 

**Python : decorator_function_with_perameter.py**
```python
def deco(func):
    def wrapper(*args,**kwargs):
        print(">>> call with args",args,"<<<")
        func(*args)
        print(">>> function call is finish <<<\n")
        
    return wrapper

def greeting(greet,name):
    print(greet+",",name);
    
    
fnc = deco(greeting);

fnc('hello','anonymo')
```

output : 
```bash
> call with args ('hello', 'anonymo') <<<
hello, anonymo
> function call is finish <<<

> 
```

<hr />
<br />

## Decorator Keyword
We use **@** token for create decorator function like that : 

**Python : decorator_keyword.py**
```python
def deco(func):
    def wrapper(*args,**kewargs):
        print("start calling function with :",args,"and",kewargs);
        func(*args,**kewargs);
        print(">>> Function Finish <<<\n\n");
        
    return wrapper;
    

@deco
def greeting(g,name):
    print(g+",",name+"!");
    
greeting("Hi","Anonymo");
```

output : 
```
start calling function with : ('Hi', 'Anonymo') and {}
Hi, Anonymo!
> Function Finish <<<
```

Here :
```python
@deco
def greeting(g,name):
    print(g+",",name+"!");
```
Equivalent to : 
```python
def greeting(g,name):
    print(g+",",name+"!");

greeting = deco(greeting);
```

## Create Timeit Decorator
Here create a decorator for check how many time a function took.

```python
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time();
        print(func.__name__);
        func(*args,**kwargs);
        end = time.time();
        
        details = ">>> Function took {:.2f} seconds <<<".format(end-start);
        print(details,"\n");
        
    return wrapper
    
@timer 
def sleep_func(s):
    time.sleep(s);
    
@timer
def serial_sum(n):
    s = 0;
    for i in range(1,n+1):
        s += i;

    print(str(n)+"nth","Sum is : ",s);

@timer
def serial_sum_two(n):
    s = ((n+1)*n)//2;
    print(str(n)+"nth","Sum is : ",s);

n = 10000000;   
sleep_func(1.5);
serial_sum(n);
serial_sum_two(n);
```

output : 
```bash
sleep_func
>>> Function took 1.50 seconds <<< 

serial_sum
10000000nth Sum is :  50000005000000
>>> Function took 1.45 seconds <<< 

serial_sum_two
10000000nth Sum is :  50000005000000
>>> Function took 0.00 seconds <<< 
```

<hr />
<br />

## \_\_call\_\_
**\_\_call\_\_** is class magic method to make class object callable. Here example : 

***Python : call_method.py***
```python
class Person:
    # constructor
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
    
    # meke the object callable
    def __call__(self):
        print("name :",self.name);
        print("age :",self.age);
        
me = Person("Anonymo","99");

# call the object
me();
```

output : 
```bash
name : Anonymo
age : 99
```

## Class Decorator
We can create class decorator using **\_\_call\_\_** magic method. Here example : 

**Program : 
```python
class deco:
    def __init__(self,func):
        self.func = func;
        
    def __call__(self,*args,**kwargs):
        print(self.func.__name__);
        self.func(*args,**kwargs);
        print(">>> program finish <<<");
    
@deco
def greeting(g,n):
    print(g+",",n+"!");
    
greeting('Hello',"Anonymo");
```

output : 
```bash
greeting
Hello, Anonymo!
>>> program finish <<<
```

<hr />
<br />

[< Go Back](./../part_4.md)
---------------------------