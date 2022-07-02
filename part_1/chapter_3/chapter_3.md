Chapter 3 : Variable, Datatype and Mathematical Operator
========================================================

## **Variable** 
**Variable** can store data. We can change variable value when ever we want.

<br>

## **String**
**String** is a group of character which is wraped by 2 double and single quote.

<br>

## **Data Type**
Value type called **Data Type** in python. Four simple data type : 
1. int -> (Integer number)
1. float -> (Float number which is contain fraction)
1. str -> (String)
1. bool -> (Boolean, True and False)

<br>

## **Mathematical Operator** 
**Mathematical Operator** use for execute mathematics task in python. Here all mathematical operator with their name : 

| Operator | Name                             |
|----------|----------------------------------|
| +        | Sum or Plus Operator             |
| -        | Minus or Substraction Operator   |
| *        | Multiply Operator                |
| /        | Division Operator                |
| %        | Modules or Remainder Opreator    |
| //       | Floor Division Operator          |
| **       | Power and exponent Operator      |

<br>

## **type**
**type** function use for see data type.

<br>

## **input**
**input** function use for take input from use and store variable as string.

<br>

## **int**
**int** is python built in function use to convert string and float to integer number.

<br>
<br>

Let see simple python program on variable : 
***Program : variable.py***
```python
text = "Hello, World!";
print(text);
```

***Output : variable.py***
```bash
Hello, World!
```

Then open the terminal and run the python3 interpreter. Then start to some program to see what happen.

Sum of two variable which are store number : 
```bash
>>> number1 = 10
>>> number2 = 5
>>> result = number1 + number2
>>> print(result)
15
>>>
```

Changing variable value. Changing **number1** variable multiple time. 
```bash
>>> number1 = 10
>>> print(number1)
10
>>> number1 = 15
>>> number1 = 18
>>> print(number1)
18
>>> number1 = "hello"
>>> print(number1)
hello
>>> 
```

Try to add number and string by plus and get error.
```bash
>>> number1 = "hello"
>>> number2 = 2
>>> result = number1 + number2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Try to knowing datatype of variable by **type** function :
```bash
>>> v = 10
>>> type(v)
<class 'int'>
>>> v = "10"
>>> type(v)
<class 'str'>
>>> v = 10.0
>>> type(v)
<class 'float'>
```

See example of string : 
```bash
>>> s = "100"
>>> print(s)
100
>>> s = "abscd134-09232<>??323"
>>> print(s)
abscd134-09232<>??323
>>> s = 'abc 123'
>>> print(s)
abc 123
>>> s = ''
>>> print(s)

>>> s = ""
>>> print(s)

>>> 
```

We can not plus string and number in python otherwise it throw error :
```bash
>>> a = 1
>>> b = 2.5
>>> c = a + b
>>> print(c)
3.5
>>> 
>>> a = 1
>>> b = "2"
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
```

5 divide by 2 : 
```bash
>>> 5 / 2
2.5
```

5 substracted by 2 :
```bash
>>> 5 - 2
3
```

5 multiply by 2 : 
```bash
>>> 5 * 2
10
```

5 floor divide by 2 :
```bash
>>> 5 // 2
2
```

5 modules by 2 :
```bash
>>> 5 % 2
1
```

5 to the power of 2 : 
```bash
>>> 5 ** 2
25
```

print multiple variable by one print function : 
```bash
>>> a = 1
>>> b = 1.2
>>> c = "hello"
>>> print(a, b, c)
1 1.2 hello
>>> print(a, b, c, "world")
1 1.2 hello world
>>> 
```

***Program : input.py ***
```python
name = input("What is your name ? ");
print("Welcome to Python,",name,'!')
```

***Output : input.py ***
```bash
What is your name ? Md Tazri
Welcome to Python, Md Tazri !
```

***Program : input_1.py***
```python
number1 = input("Please type an integer and press enter : ");
number2 = input("Please type another integer and press enter : ");

print("number1 + number2 ",number1+number2);
```

***Ouput : input_1.py***
```bash
Please type an integer and press enter : 3
Please type another integer and press enter : 6
number1 + number2  36
```

***Program : input_2.py***
```python
number1 = input("Please type an integer and press enter : ");
number2 = input("Please type another integer and press enter : ");
number1 = int(number1);
number2 = int(number2);

print("number1 + number2 ",number1+number2);
```

***Output : input_2.py***
```bash
Please type an integer and press enter : 3
Please type another integer and press enter : 6
number1 + number2  9
```

[< Go Back](./../part_1.md)
---------------------------