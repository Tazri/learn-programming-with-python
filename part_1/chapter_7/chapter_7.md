Chapter 7 : Function
====================

## **function**
**def** keyword use to create function. Here simple saytax of function : 
```python
def function_name(parameter=default_value) :
    # statement gose here
    return return_value;
```

<hr />

## **sum**
**sum** is default python function. It use for figure out sum of number of list. It take number list and return sum of number of list.

<hr />

**Let's some proram with function :**

**Create add function add do sum task by it.**
```bash
>>> def add(n1,n2) :
...     return n1 + n2;
... 
>>> n = 10;
>>> m = 5;
>>> result = add(n,m);
>>> print(result)
15
>>> number1 = 10
>>> number2 = 10
>>> result = add(number1,number2)
>>> print(result)
20
>>> 
>>> n1 = 20
>>> n2 = 10
>>> print(add(n1,n2)
... )
30
>>> print(add(2.5,3.5)
... )
6.0
>>> 
```

***Program : wheel_by_funtion.py***
```python
import turtle

def draw_square(side_length) : 
    for i in range(4) : 
        turtle.forward(100);
        turtle.left(90);

counter = 0;

turtle.color("red");
while counter < 90 : 
    draw_square(100);
    turtle.right(4);
    counter += 1;

turtle.exitonclick();
```

***Output : wheel_by_function***

![wheel_by_function](./../../asset/turtle/wheel_by_function.png)

**Function parameter default value.**
```bash
>>> def printy(y=10) :
...     print(y);
... 
>>> printy()
10
>>> print(20)
20
>>> 
```

**Program : add_numbers.py**
```python
def add_numbers(numbers) : 
    result = 0;
    for number in numbers : 
        result += number;
    return result;

result = add_numbers([1,2,30,4,5,9]);
print(result);
```

**Output : add_numbers.py**
```bash
51
```

**List assign is reference type.**
```bash
>>> list1 = [1,2,3,4]
>>> list2 = list1
>>> list1
[1, 2, 3, 4]
>>> list2
[1, 2, 3, 4]
>>> list2[0] = 99
>>> list1
[99, 2, 3, 4]
>>> list2
[99, 2, 3, 4]
>>> 
```

**Use sum function to figure out sum of number of list.**
```bash
>>> li = [1,2,3]
>>> sum(li)
6
>>> 
```

***Program : average_list.py***
```python
def list_average(numbers) : 
    return sum(numbers)/len(numbers);

print(list_average([4,3,5,20]));
```

***Output : average_list.py***
```bash
8.0
```


***Program : namta_function.py***
```python
def namta(n = 1) : 
    for i in range(1,11) : 
        print(n,"x",i,"=",n*i);

print("namta(9) : ");
namta(9);
print("namta() : ");
namta();
```

***Output : namta_function.py***
```bash
namta(9) : 
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
namta() : 
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
```

[< Go Back](./../part_1.md)
---------------------------