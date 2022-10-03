Chapter 08 : Type Hinting in Python
===================================

Python is dynamically typed language. Here we can not declear variable with data type. Python do it automatically. But we can speacify the type for variable, function parameter, function return type. It called **Type Hinting**. But it dose not effect the python program. It just help us which type of value are store in variable or nothing else. Here example : 

***Program : type_hinting.py***

```python
def is_eligible(platform:str,age:int)-> bool: # return type 
    if platform == 'facebook' and age >= 13 :
        return True;
    if platform == 'twitter' and age>= 18 : 
        return True;
    return False;

if __name__ == "__main__":
    platform:str = 'facebook';
    age:int = 15;
    print(is_eligible(platform,age));
```

***Output : type_hinting.py***
```bash
Ture
```
we can see is type hinting maintain successfully or not by using **mypy** python package. Here example : 

```bash
$ mypy type_hinting.py 
Success: no issues found in 1 source file
```

We can use **typing** module for indicate what kind of data use variable. Here example : 

```bash
>>> from typing import List, Tuple, Set, Dict
>>> 
>>> # here said list element are string
>>> fruits: List[str] = ["Mango", "Guava","Apple"]
>>> 
>>> # here said tuple elements are  float
>>> coordinate: Tuple[float, float] = (23.6432, 90.4343)
>>> 
>>> # here said set elements are string
>>> colors: Set[str] = {"green", "blue", "orange"}
>>> 
>>> # here saids dict elements are string
>>> capitals : Dict[str,str] = {"Bangladesh": "Dhaka", "England" : "London"}
```


<hr />
<br />

[< Go Back](./../part_4.md)
---------------------------