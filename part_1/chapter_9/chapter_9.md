Chapter 9 : Various Type of Data Structure
==========================================

## **List**
Here simple list declare syntax : 
```python
list = [1,2,3,4,5,6,7];
```

### **List Method**
List method modify the list. Can not return anything. Here some list method : 

| Method        | Explain                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------- |
| .sort()       | sort the list. **reverse** is vlue pair parameter which default value is False.             |
| .remove(v)    | remove the v in the list.                                                                   | 
| .reverse()    | reverse the list.                                                                           |
| .insert(p,v)  | insert the value v at position in list p.                                                   |
| .pop(p)       | remove element at position p. p default value is -1.                                        |
| .extend(i)    | extend the list with any iterable object items.                                             |
| .count(e)     | return total number of element e in list.                                                   |
| .join(li)     | join is string method. join the whole list item which is contain string.                    |


### **List Comprehensions**
Here syntax of list comprehensions : 
```python
li = [element for element in iterable_object];
li = [element for element in iterable if condition]
li = [element_with_expresion for element in iterable_object if condition];
```

### **del**
**del** is function which use to delete list element or list. **del** also delete anything.

### **List Concatination and Repetition**
Here simple sytax of list concatination and repetition.
```python
# concatination
new_list = list1 + list2;

# repetition
new_list = list1 * int_number;
```

<hr/>

## **Tuple**
Tuple look like list but when declare it use first bracket () or nothing instead of secound bracket []. Here simple tuple : 

```python
# tuple
new_tuple = (2,3,5,6);

# tuple without using bracket
new_tuple = 2,4,5,6;
```

**Tuple is unmutable that's mean it is unchangable.**

### **Unpacking Tuple**
Tuple unpacking syntax here :
```python
value1, value2 = tuple; # tuple = (v1,v2); value1 = v1, value2 = v2 
```

<hr />

## **Set**
**Set** create with {} if element exist otherwise create empty set with **set()** function. Here example : 
```python
empty_set = set();
new_set = {value,value,value};
```

### **Set Operation**
We can use **union, intersection, symmetric and minus** in set. In that case use **bitwise and minus** operator.

| Operator | Use For     | Example                                                                             |
| -------- | ----------- | ----------------------------------------------------------------------------------- |
| &        | intersection| set_A & se_B # return intersection of set_A and set_B                               |
| \|       | uinion      | A \| B # return union of A and B                                                    |
| ^        | symmetric   | A ^ B # return symmetric of A and B                                                 |
| -        | difference  | A - B # return A diffreence B                                                       |


<hr />

## **Dictionary**
**Dictionary** create with {} if dictionary empty otherwise create dictionary **key, value** pair with curly bracket {}. Here **key** is can be any hashablue value like string, tuple and number. Here simple syntax : 

```python
b = {key : value, key : value, key : value}
```

### **Accesing Dictionary**
Two way to access dictionary key's value : 

```python
# list syntax
dictionary[key];

# use get method
dictionary.get(key);
```

### **Dictionary Method**

Here some dictionary method : 

| Method     | Explain                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------- |
| .keys()    | return all keys in list                                                                         |
| .values()  | return all values in list                                                                       |
| .items()   | return key value pair tuple in list                                                             |
| .clear()   | clear the dictionary                                                                            |
| .update(d) | update the dictionary with parameter dictionary d                                               |
| .pop(key)  | remove dictionary item by key                                                                   |
| .copy()    | return the copy of dictionary                                                                   |


<hr />
<br />
<br />

Let's do some program with dictionary, set, tuple and list : 
------------------------------------------------------------

**Use append method on list.**
```bash
>>> saarc = ["Bangladesh","India","Sri Lanka","Pakistan","Nepal","Bhutan"]
>>> saarc
['Bangladesh', 'India', 'Sri Lanka', 'Pakistan', 'Nepal', 'Bhutan']
>>> saarc.append("Afganistan")
>>> saarc
['Bangladesh', 'India', 'Sri Lanka', 'Pakistan', 'Nepal', 'Bhutan', 'Afganistan']
>>> 
```

**Use sort method on list.**
```bash
>>> saarc = ["Bangladesh","India","Sri Lanka","Pakistan","Nepal","Bhutan"]
>>> saarc.sort()
>>> saarc
['Bangladesh', 'Bhutan', 'India', 'Nepal', 'Pakistan', 'Sri Lanka']
>>> li = [1,3,7,2,4,6,1]
>>> li.sort()
>>> li
[1, 1, 2, 3, 4, 6, 7]
>>> 
```

**Use reverse method on list.**
```bash
>>> li = [1,2,3,4]
>>> li.reverse()
>>> li
[4, 3, 2, 1]
>>> li = ["mango", "banana", "orange"]
>>> li.reverse()
>>> li
['orange', 'banana', 'mango']
>>> 
```

**Use insert method on list.**
```bash
>>> fruits = ["mango", "banana", "orange"]
>>> fruits
['mango', 'banana', 'orange']
>>> fruits.insert(2,"cocunut")
>>> fruits
['mango', 'banana', 'cocunut', 'orange']
>>> 
```

**Use remove method.**
```bash
>>> fruits = ["apple","mango", "cocunut", "banana", "orange"]
>>> fruits.remove("cocunut")
>>> fruits
['apple', 'mango', 'banana', 'orange']
>>> fruits.remove("pineapple")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
```
**Use pop method on list.**
```bash
>>> fruits = ["apple","mango", "cocunut", "banana", "orange"]
>>> item = fruits.pop()
>>> item
'orange'
>>> fruits
['apple', 'mango', 'cocunut', 'banana']
>>> 
```

**Use pop method with index on list.**
```bash
>>> fruits = ["apple","mango", "cocunut", "banana", "orange"]
>>> item = fruits.pop(1)
>>> item
'mango'
>>> fruits
['apple', 'cocunut', 'banana', 'orange']
>>> 
```

**Use extend method on list.**
```bash
>>> li = [1, 2, 3]
>>> li2 = [3, 4, 5, 6]
>>> li.extend(li2)
>>> li
[1, 2, 3, 3, 4, 5, 6]
>>> 
```

**Use count method on list.**
```bash
>>> li = [1, 2, 3, 3, 4, 5, 6]
>>> li.count(3)
2
>>> li.count(5)
1
>>> li.count(10)
0
>>> 
```

**Use del function on list.**
```bash
>>> li
[1, 2, 3, 3, 4, 5, 6]
>>> del(li[1])
>>> li
[1, 3, 3, 4, 5, 6]
>>> del(li[0])
>>> li
[3, 3, 4, 5, 6]
>>> del(li)
>>> li
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'li' is not defined
>>> 
```

**Add two string and multiply string with a number.**
```bash
>>> li1 = [1, 2, 3]
>>> li2 = [4, 5, 6]
>>> li = li1 + li2
>>> print(li)
[1, 2, 3, 4, 5, 6]
>>> li1 = [1,2,3]
>>> li2 = li1 * 3
>>> li2
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 
```

**Use join string method on list.**
```bash
>>> li = ['a','b','c']
>>> li
['a', 'b', 'c']
>>> ''.join(li)
'abc'
>>> ','.join(li)
'a,b,c'
>>> ' - '.join(li)
'a - b - c'
>>> 
```

**List comprehensions.**
```bash
>>> li = [1,2,3,4]
>>> new_li = [2*x for x in li]
>>> new_li
[2, 4, 6, 8]
>>> 
```
**Even number list by list comprehensions.**
```bash
>>> even_numbers = [x for x in range(1,11) if not x & 1]
>>> even_numbers
[2, 4, 6, 8, 10]
>>> 
```

**Another example of list comprehensions.**
```bash
>>> li = [1,2,3,4]
>>> [x*x for x in li]
[1, 4, 9, 16]
>>> 
```

**Tuple type.**
```bash
>>> x = (1, 2, 3)
>>> type(x)
<class 'tuple'>
>>> x = 1, 2, 3
>>> type(x)
<class 'tuple'>
>>> 
```

**Tuple indexing.**
```bash
>>> tp1 = 1,2,3
>>> tp1[0]
1
>>> tp1[1]
2
>>> tp1[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> 
```

**Unpacking tuple.**
```bash
>>> numbers = 10,20,30,40
>>> n1,n2,n3,n4 = numbers
>>> n1
10
>>> n2
20
>>> n3
30
>>> n4
40
>>> t = n3,n4
>>> t
(30, 40)
>>> type(t)
<class 'tuple'>
>>> 
```

**Tuple convert to list.**
```bash
>>> tp1 = (1,2,3)
>>> li = list(tp1)
>>> li
[1, 2, 3]
>>> 
```

**Empty set.**
```bash
>>> A = set()
>>> A
set()
>>> type(A)
<class 'set'>
>>> 
```

**Unempty set.**
```bash
>>> items = {'pen', 'laptop','cellphone'}
>>> items
{'pen', 'cellphone', 'laptop'}
>>> type(items)
<class 'set'>
>>> 
```

**Convert tuple and list to set.**
```bash
>>> li = [1, 2, 3, 4]
>>> tp1 = (1, 2, 3)
>>> A = set(li)
>>> A
{1, 2, 3, 4}
>>> B = set(tp1)
>>> B
{1, 2, 3}
>>> type(A)
<class 'set'>
>>> type(B)
<class 'set'>
>>> 
```

**String to convert set.**
```bash
>>> A = set("Bangadesh")
>>> A
{'n', 'e', 'g', 'B', 'd', 'h', 's', 'a'}
>>> type(A)
<class 'set'>
>>> B = set("Sri Lanka")
>>> B
{' ', 'n', 'i', 'k', 'L', 'r', 'S', 'a'}
>>> type(B)
<class 'set'>
>>> 
```

**Membership operator on set.**
```bash
>>> A = {1, 2, 3}
>>> 1 in A
True
>>> 2 in A
True
>>> 5 in A
False
>>> 
```

**Set uinion, intersection, minus and symmetric.**
```bash
>>> A = {1, 2, 3, 4, 5}
>>> B = {2, 4, 6, 8}
>>> C = A & B
>>> C
{2, 4}
>>> C = A | B
>>> C
{1, 2, 3, 4, 5, 6, 8}
>>> 
>>> C = A^B
>>> C
{1, 3, 5, 6, 8}
>>> C = A - B
>>> C
{1, 3, 5}
>>> C = B - A
>>> C
{8, 6}
>>> 
```

**Simple dictionary.**
```bash
>>> marks = {1:77, 2:76, 5:62, 4:78, 3:65}
>>> type(marks)
<class 'dict'>
>>> marks[3]
65
>>> marks.get(3)
65
>>> 
```

**Add dictionary key.**
```bash
>>> dt = {}
>>> dt
{}
>>> type(dt)
<class 'dict'>
>>> dt[1] = "one"
>>> dt
{1: 'one'}
>>> dt[2] = "two"
>>> dt
{1: 'one', 2: 'two'}
>>> 
```

**Accessing not exist key in dictionary.**
```bash
>>> dt = {"a" : "A", "b" : "B", "c" : "C"}
>>> dt["a"]
'A'
>>> dt["b"]
'B'
>>> dt["c"]
'C'
>>> dt["d"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'd'
>>> 
```

**Try to use tuple, list and set as a dictionary keys.**
```bash
>>> dt = {"a" : "A", "b" : "B", "c" : "C"}
>>> dt[(1,2,3)] = "tuple"
>>> dt
{'a': 'A', 'b': 'B', 'c': 'C', (1, 2, 3): 'tuple'}
>>> li = [1,2,3]
>>> dt[li] = "list"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> s = {1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> type(s)
<class 'set'>
>>> dt[s] = "set"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> 
```

**Use keys method on dictionary.**
```bash
>>> dt = {"a" : "A", "b" : "B", "c" : "C"}
>>> dt.keys()
dict_keys(['a', 'b', 'c'])
>>> 
```

**For in loop on dictionary.**
```bash
>>> dt
{'a': 'A', 'b': 'B', 'c': 'C'}
>>> for i in dt : 
...     print(i)
... 
a
b
c
>>> 
```

**Use items method on dictionary.**
```bash
>>> for key,value in dt.items() :
...     print("k",key);
...     print("v",value);
... 
k a
v A
k b
v B
k c
v C
>>> 
```


[< Go Back](./../part_1.md)
---------------------------