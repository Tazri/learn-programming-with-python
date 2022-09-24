Chapter 04 : Sorting
=================

Here we learn about sorting function which can use for sorting list, tuple. Here table of content : 

- [Chapter 04 : Sorting](#chapter-04--sorting)
  - [sort](#sort)
  - [sorted](#sorted)
  - [< Go Back](#-go-back)

## sort
sort use for sort the list. sort is a list method. Here want to sort list reverse then pass the perameter **reverse=True** for sort the list reverse.

```bash
>>> li = [3,4,5,6,29,2]
>>> li.sort()
>>> li
[2, 3, 4, 5, 6, 29]
>>> li.sort(reverse=True)
>>> li
[29, 6, 5, 4, 3, 2]
>>> 
```
<hr />
<br />

## sorted
**sorted()** is function for use sort list, tuple and dictionary and return new list or tuple. Also here work **reverse=True** perameter in secound placed. Here example : 

```bash
>>> # list
>>> li = [4,5,6,7]
>>> sorted(li)
[4, 5, 6, 7]
>>> sorted(li,reverse=True)
[7, 6, 5, 4]
>>> 
>>> # tuple
>>> tu = (4,3,5,6)
>>> sorted(tu)
[3, 4, 5, 6]
>>>
>>> # dictionary
>>> di = { 'c' : 3, 'd' : 1, 'l' : 49, 'a' : 4}
>>> sorted(di)
['a', 'c', 'd', 'l']
>>> 
```

Sorted  tuple of list :

***Program : list_of_tupe.py*** 
```python
fruits = [
    ('benana',4),
    ('apple',10),
    ('mango',21),
    ('guava',2),
]

print("> fruits :");
print(sorted(fruits))

print("> sorted(fruits) : ");
print(sorted(fruits));
```

output : 
```bash
> fruits :
[('apple', 10), ('benana', 4), ('guava', 2), ('mango', 21)]
> sorted(fruits) : 
[('apple', 10), ('benana', 4), ('guava', 2), ('mango', 21)]
```

If we want to spacify the item for sorted by which item then use **key** perameter which take a function and sorted will sorted by what function return. Here example : 

***Program : key_sorted.py***
```python
fruits = [
    ('benana',4),
    ('apple',10),
    ('mango',21),
    ('guava',2),
]

def compare_key(item):
    return item[1];

print("> fruits ");
print(sorted(fruits))

print("> sorted(fruits,key=compare_key) : ");
print(sorted(fruits,key=compare_key));
```

output : 
```bash
> fruits 
[('apple', 10), ('benana', 4), ('guava', 2), ('mango', 21)]
> sorted(fruits,key=compare_key) : 
[('guava', 2), ('benana', 4), ('apple', 10), ('mango', 21)]
```

We do this thing by using **itemgetter()** function from **operator**. Here it take item which use for sorted by the whole list. **itemgetter()** take \*args for priority of item for sort the list and return the list. Here example : 

***Program : item_getter.py***
```python
from operator import itemgetter

fruits = [
    ('benana',2),
    ('apple',2),
    ('mango',21),
    ('guava',24),
]

print("> fruits ");
print(fruits)

print("> sorted(fruits,key=compare_key) : ");
print(sorted(fruits,key=itemgetter(1,0)));
```

output : 
```bash
> fruits 
[('benana', 2), ('apple', 2), ('mango', 21), ('guava', 24)]
> sorted(fruits,key=compare_key) : 
[('apple', 2), ('benana', 2), ('mango', 21), ('guava', 24)]
```

<hr />
<br />

[< Go Back](./../part_4.md)
-------------