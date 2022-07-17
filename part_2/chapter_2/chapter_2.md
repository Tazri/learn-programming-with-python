Chapter 2 : Module and Package
------------------------------

## **import**
Here all import syntax to import module :
```python
# import the single mdoule
import module

# import multiple module
import module1, module2

# import a function from module
from module import function_name

# import a module alias other name
import module as m
```

<hr>

## **webbrowser.open**
syntax here :
```python
import webbrowser

# open the url by default browser
webbrowser.open(url)
```

<hr />

## **dir**
**dir** function use for see about the module. It take the module name and print a list which contain all method inside the module.

<hr />

## **math**
**math** is python simpe module which is use for mathmatic task. Here some necessary function of math :

| function    | work for                                                                            |
| pi          | return a pi value 3.141592653589793                                                 |
| math.pow()  | use for figure out power, math.pow(2,2) = 4.0, math(2,3) = 8.0                      |
| math.sqrt() | return the number root, math.sqrt(25) = 5.0                                         |
| math.floor()| floor the number math.floor(5.2) = 5                                                |
| math.ceil() | ceiling the number, math.ceil(5.2) = 6                                              |

<hr />

## Let's write some program by import.

**See the details of module by dir builtin function.**
```bash
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError',.......
.....................
```

**Little about math module.**
```bash
>>> import math
>>> math.pi
3.141592653589793
>>> math.pow(2,3)
8.0
>>> math.sqrt(25)
5.0
>>> math.floor(5.2)
5
>>> math.ceil(5.2)
6
>>> 
```

**Little about datetime.**
```bash
>>> import datetime
>>> today = datetime.date.today()
>>> print(today)
2022-07-03
>>> 
```

**Import spacify class in module by from and import keyword.**
```bash
>>> from datetime import datetime
>>> d = datetime.today()
>>> d
datetime.datetime(2022, 7, 3, 23, 6, 56, 266376)
>>> print(d)
2022-07-03 23:06:56.266376
>>> 
```

**Open the url by default browser with webbrowser module.**
```bash
>>> import webbrowser
>>> url = "http://subeen.com"
>>> webbrowser.open(url)
True
```

**import webbrowser as web.**
```bash
>>> import webbrowser as wb
>>> url = "http://subeen.com"
>>> wb.open(url)
True
```

***Program : fibo.py***
```python
def find_fibo(n) :
    if n <= 2 :
        return 1;
    else : 
        past = 1;
        present = 1;

        for i in range(n - 2) :
            past, present = present, past+present;

        return present;

def list_fibo(n) :
    if n <= 2 :
        if n == 2 : return [1,1];
        return [1]
    
    fibo_list = [1,1]

    i = 2;

    while i < n :
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2]);

        i+= 1;

    return fibo_list;


for x in range(1,11) :
    print(find_fibo(x));

print(list_fibo(1));
print(list_fibo(2));
print(list_fibo(10));
```

***Output : fibo.py***
```bash
1
1
2
3
5
8
13
21
34
55
[1]
[1, 1]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

***Program : program.py***
```python
import fibo

print("Hello, I am inside program.py!")

n = fibo.find_fibo(15);

print("15th fibonacci number is,",n);
```

***Output : program.py***
```bash
1
1
2
3
5
8
13
21
34
55
[1]
[1, 1]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Hello, I am inside program.py!
15th fibonacci number is, 610
```

***Program : trail.py***
```python
print("My name is",__name__);
```

***Output : trial.py***
```bash
My name is __main__
```

***Program : program2.py***
```python
import trial

print("Hello, I am inside program.py");
print(trial.__name__);
```

***Output : program2.py***
```bash
My name is trial
Hello, I am inside program.py
trial
```

***Program : program3.py***
```python
import program2

print("Here program 3.");
print(program2.__name__);
```

***Output : program3.py***
```bash
import program2

print("Here program 3.");
print(program2.__name__);
```

**See the path by sys module path function.**
```bash
>>> import sys
>>> sys.path
['', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/local/lib/python3.9/dist-packages', '/usr/lib/python3/dist-packages']
>>> 
```

[< Go Back](./../part_2.md)
---------------------------