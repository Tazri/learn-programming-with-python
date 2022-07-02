Chapter 4 : Conditional Logic
=============================

## **Comparision Operator**
**Comparision Operator** use for compare between two value. It always return **boolean type** data. Boolean data is **True** and **False**.

<br>

## **Logical Operator**
**Logical Operator** compare between two boolean type value and return boolean type data except **not** operator. **not** is **binary** operator. It use on only one operand. Here all Logical operator in python with truth table :

| A   | B   | A and B | A or B | not A |
|-----|-----|---------|--------|-------|
|False|False|  False  | False  |  True |
|False|True |  False  | True   |  True |
|True |False|  False  | True   |  False|
|True |True |  True   | True   |  False|

<br>

## **List**
**List** is one kind of datatype in python. List can store multiple value in single variable name. We modify list. List index number start with **0** and negative index start with **-1**. **negative** index start with last element in list and **positive** index start with first element in list. we can access list element like : 

```python
list[index_number]
```

<br><br>

## **if**
**if** is a keyword in python which is use for check condition to run a spacify statment. Here simple **if** format : 
```python
if condition :
    statement here
```

<br>

## **else**
If **if** condition is return **False** and **else** block exist with **if** block then program run **else** block instead of **if** block.Simple format : 
```python
if condition : 
    # if block statement
else : 
    # else block statement
```

## **elif**
**elif** keyword use for add multiple conditional block statement between if and else. Here example : 
```python
if condition : 
    # if block statement;
elif condition :
    # elif block statement;
elif condition :
    # elif block statement;
..................
..................
else : 
    # else block statement;
```

<br><br>

**Open the Teminal and run the python3 interpreter and let start to coding :**

**Compare two number by comparision operator.**
```bash
>>> 2 == 3
False
>>> 3 == 3
True
>>> 2 > 3
False
>>> 2 < 3
True
>>> 2 != 3
True
>>> 3 != 3
False
>>> 2 >= 3
False
>>> 2 <= 3
True
>>> 
```

**Compare two string by comparision operator.**
```bash
>>> "Bangladesh" == "Bangladesh"
True
>>> "Bangladesh" == "bangladesh"
False
>>> 
```

**Compare two int type variable by comparision operator.**
```bash
>>> my_money = 30
>>> rickshaw_fare = 40
>>> my_money >= rickshaw_fare
False
>>> 
>>> my_money = 30
>>> rickshaw_fare = 30
>>> my_money >= rickshaw_fare
True
>>> 
>>> my_money = 50
>>> rickshaw_fare = 40
>>> my_money >= rickshaw_fare
True
```

**Use not logical operator.**
```bash
>>> today = "Tuesday"
>>> today == "Tuesday"
True
>>> today = "Wednesday"
>>> today == "Tuesday"
False
>>> not (today == "Tuesday")
True
>>> 
>>> not True
False
>>> not False
True
>>> 
```

**Use logical operator and and or.**
```bash
>>> number = 20
>>> number > 10
True
>>> number < 100
True
>>> number > 10 and number < 100
True
>>> number = 200
>>> number > 10
True
>>> number < 100
False
>>> number > 10 and number < 100
False
>>> number > 10 or number < 100
True
>>> not (number < 100)
True
>>> 
```

**Create list and access list element by index.**
```bash
>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> print(numbers[0])
1
>>> print(numbers[1])
2
>>> print(numbers[9])
10
>>> print(numbers[10])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> 
```

**Create list and access with index.**
```bash
>>> saarc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
>>> print(saarc)
['Bangladesh', 'Afganistan', 'Bhutan', 'Nepal', 'India', 'Pakistan', 'Sri Lanka']
>>> print(saarc[0])
Bangladesh
>>> print("Number of countries in SAARC:",len(saarc))
Number of countries in SAARC: 7
>>> 
```

**Use membership operator on list element.**
```bash
>>> "Bangladesh" in saarc
True
>>> "China" in saarc
False
>>> "China" not in saarc
True
>>> "India" not in saarc
False
>>> 
```
<br><br>

**Use if condition.**

***Program : saarc.py***
```python
saarc = [
    "Bangladesh",
    "Afghanistan",
    "Bhutan",
    "Nepal",
    "India",
    "Pakistan",
    "Sri Lanka"
]

country = input("Enter the name of the country : ");

if country in saarc :
    print(country,"is a member of SAARC.");

print("Program terminated");
```

***Output : saarc.py***
```bash
Enter the name of the country : Bangladesh
Bangladesh is a member of SAARC.
Program terminated
```
```bash
Enter the name of the country : Japan
Program terminated
```

***Program : check_saarc.py***
```python
saarc = [
    "Bangladesh",
    "Afghanistan",
    "Bhutan",
    "Nepal",
    "India",
    "Pakistan",
    "Sri Lanka"
]

country = input("Enter the name of the country : ");

if country in saarc :
    print(country,"is a member of SAARC.");
else : 
    print(country,"is not a member of SAARC.");

print("Program terminated");
```

***Output : check_saarc.py***
```bash
Enter the name of the country : Bangladesh
Bangladesh is a member of SAARC.
Program terminated
```

***Output : check_saarc.py***
```bash
Enter the name of the country : Japan
Japan is not a member of SAARC.
Program terminated
```

***Program : marks.py***
```python
marks = input("Please enter your marks : ");
marks = int(marks);

if marks >= 80 :
    grade = "A+";
elif marks >= 70 :
    grade = "A";
elif marks >= 60 :
    grade = "A-";
elif marks >= 50 : 
    grade = "B";
else : 
    grade = "F";

print("Your grade is",grade);
```

***Output : marks.py***
```bash
Please enter your marks : 80
Your grade is A+
```

```bash
>>> n1 = 20
>>> n2 = 30
>>> n3 = 25
>>> 
>>> if n1 > n2 :
...     max_n = n1;
... else : 
...     max_n = n2;
... 
>>> max_n
30
>>> if n3 > max_n :
...     max_n = n3;
... 
>>> max_n
30
```

***Program : leap_year.py***
```python
year = input("Enter the year : ");
year = int(year);

if year % 100 and not year % 4 :
    print("Yes");
elif not year % 100 and not year % 400 :
    print("Yes");
else : 
    print("No");
```

***Output : leap_year.py***
```bash
Enter the year : 2014
No
```

[< Go Back](./../part_1.md)
---------------------------