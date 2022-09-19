Chapter 02 : About Function in Python
=====================================

Here we learn about 
- [Chapter 02 : About Function in Python](#chapter-02--about-function-in-python)
  - [Function is Object](#function-is-object)
  - [Function inside the Function](#function-inside-the-function)
  - [Nonlocal](#nonlocal)
  - [Return Function](#return-function)
  - [Closure](#closure)
  - [lambda](#lambda)
  - [Function Arguments](#function-arguments)
  - [*args](#args)
  - [**kwargs](#kwargs)
  - [< Go Back](#-go-back)

<hr />
<br />

## Function is Object
In python function is a one kind of object. We store the function in a variable and use it like a funciton. Here exmple : 

```bash
>>> def add(a,b):
...     return a + b;
... 
>>> fn = add
>>> 
>>> add
<function add at 0x7ff20311e5e0>
>>> fn
<function add at 0x7ff20311e5e0>
>>> add(2,3)
5
>>> fn(2,3)
5
>>> type(add)
<class 'function'>
>>> type(fn)
<class 'function'>
>>> add.__name__
'add'
>>> fn.__name__
'add'
>>> 
```
<hr />
<br />

## Function inside the Function
We can create a function inside the another function. Here example :

```bash
>>> def hello():
...     print("Hello, i am hello")
...     
...     def hi():
...             print("hello, i am hi")
...     hi()
... 
>>> 
>>> hello()
Hello, i am hello
hello, i am hi
>>> 
```

<hr />
<br />

## Nonlocal
If create a function inside the another function then inner function can access the outer function and global vriables. But we can not change the outer function and global variable from inner fucntion. Here exmaple : 

**Program : inner_and_outer_function.py**
```python
name = "anonymo";

print(">>> name is : ",name)
def outer_add(a,b):
    result = 0;
    
    def inner_add(a,b):
        result = a + b;
        print("> inner_add result : ",result);
    
    inner_add(a,b)
    
    print("> outer_add result : ",result);
    # change global name varibale
    name = "sirius";
    print("name in function : ",name)
    
outer_add(3,4);
print(">>> after calling outer_add name :",name)
```
output :
```bash
> name is :  anonymo
> inner_add result :  7
> outer_add result :  0
name in function :  sirius
> after calling outer_add name : anonymo
> 
```

If it neccessary to change outer function variable from inner function variable then use **nonlocal** keyword. Use **global** keyword to change global variable from function. Here example :

***Program : nonlocal_global.py**
```python
name = "anonymo";

print(">>> name is : ",name)
def outer_add(a,b):
    result = 0;
    
    def inner_add(a,b):
        nonlocal result; 
        result = a + b;
        print("> inner_add result : ",result);
    
    inner_add(a,b)
    
    print("> outer_add result : ",result);
    # change global name varibale
    global name; 
    name = "sirius";
    print("name in function : ",name)
    
outer_add(3,4);
print(">>> after calling outer_add name :",name)
```
ouput : 
```bash
> name is :  anonymo
> inner_add result :  7
> outer_add result :  7
name in function :  sirius
> after calling outer_add name : sirius
> 
```

<hr />
<br />

## Return Function
It can possible to return a function from another function. Here exmaple : 

***Program : return function***
```python
def return_add(n_one,n_two):
    def add():
        return n_one + n_two;
    
    return add;
    
fn = return_add(4,10);
print(return_add)
print(fn);
print(fn());
``` 

output : 
```bash
<function return_add at 0x7f1e436f9d30>
<function return_add.<locals>.add at 0x7f1e436f9dc0>
14
```
<hr />
<br />

## Closure
Clusure in python is a one kind of function which has access his upper function variable. Closure function object **\_\_closure\_\_** is not **None**. Here example : 

***python : closure example :***
```python
def addition(n_one):
    def add(n_two):
        return n_one + n_two;

    return add;
    
ten_plus = addition(10); # here ten_plus is closure

print("ten_plus(3) : ",ten_plus(3));
print("addition.__closure__ : ",addition.__closure__)
print("ten_plus.__closure__ : ",ten_plus.__closure__);
```

output :
```bash
ten_plus(3) :  13
addition.__closure__ :  None
ten_plus.__closure__ :  (<cell at 0x7f6d2c02b4c0: int object at 0x955f60>,)
```
<hr />
<br />

## lambda
Lembda is one kind of anonymous function in python which define with **lambda** keyword and only one expression. Here structure : 

```python
a = lembda p : p*2;

# here is parameter of lembda and it return p*2
```

Here example :
***Python : lambda***
```
add = lambda a,b : a+b;

print("add : ",add);
print("add(3,3) : ",add(3,3));
print("add(5,3) : ",add(5,3));
```

output : 
```bash
add :  <function <lambda> at 0x7f02ddbfedc0>
add(3,3) :  6
add(5,3) :  8
```


<hr />
<br />

## Function Arguments
We can pass the function arguments in python two way. Here : 

1. Positiontial Argument or non-keyword argument.
2. Non-positional Argument or named argument or keyword argument.

Here example of positional and non positional argument in one program : 

***Python : positional argument and non keyword argument.***
```python
def greeting(g,n):
    print(g+",",n,"!");
    
# positional argument or non-keyword argument.
greeting("Hello","Anonymous");

# non-positional argument or keyword argument.
greeting(n="Sirius",g="Sirius");
```

output : 
```bash
Hello, Anonymous !
Sirius, Sirius !
```

<hr />
<br />

## *args
If can take argument as much as we want from function by ***\*args***. We take the argument from user as tuple. Here example : 

```python
def give_me_tuple(*args):
    print(type(args));
    print(args);

give_me_tuple(2,4,65,7,3);


def hello_every_one(g,*names):
    print("\n");
    for name in names:
        print(g+",",name);
        
hello_every_one("Hi","Anonymous","Sirius","Alpha");

# don't do below code. it dose not work
# hello_every_one(names=("Trition","lion","throw"),g="hello")
# hello_every_one(names="Trition","lion","throw",g="hello")
```

output : 
```bash
<class 'tuple'>
(2, 4, 65, 7, 3)


Hi, Anonymous
Hi, Sirius
Hi, Alpha
```

<hr />
<br />

## **kwargs
we can take argument as dictionary from function by ***\*\*kwargs***. Here example : 

***Program : \*\*kwargs***
```python
def take_dict(**kwargs):
    print(kwargs);
    
take_dict(a=3,b=6,c=4);

def show_marks(n,**marks):
    print("\nExam Name is : ",n);
    for name in marks : 
        print(name,":",marks[name]);
    
show_marks("ssc",anonymous=99,sirius=0,kripton=33)

# below code work finly
show_marks(n="hsc",anonymous=9,sirius=1,kripton=33)

# below code work fine as well
show_marks(anonymous=99,sirius=0,kripton=33,n="PSC")
```

output : 
```bash
{'a': 3, 'b': 6, 'c': 4}

Exam Name is :  ssc
anonymous : 99
sirius : 0
kripton : 33

Exam Name is :  hsc
anonymous : 9
sirius : 1
kripton : 33

Exam Name is :  PSC
anonymous : 99
sirius : 0
kripton : 33
```

<hr />
<br />

[< Go Back](./../part_4.md)
-----------------------------