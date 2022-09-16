Chapter 01 : Iterator and Generator
===================================

Here We discuss about : 
- [Chapter 01 : Iterator and Generator](#chapter-01--iterator-and-generator)
  - [Container](#container)
  - [Iterator](#iterator)
  - [Create Iterator](#create-iterator)
  - [Generator](#generator)
  - [< Go Back](#-go-back)

<hr />
<br />

## Container
In python container is one kind of data type which contain many data type and has a feature like check a spacify data exist or not. Example is : Tuple, List,Set and Dictunary.

Here the example : 

```bash
>>> alist = [3,2,6]
>>> atuple = (3,4,6)
>>> aset = {4,3,6,2}
>>> adictionary = {'a' : 3,'b': 4}
>>> 
>>> 
>>> 2 in alist
True
>>> 10 in atuple
False
>>> 3 in aset
True
>>> 'a' in adictionary
True
>>> 
```
<hr />
<br />

## Iterator
Iterator is one kind of object which can remember current state and also find next state by calling it with **next()** function. In python create iterator whith **iter()** function. here example : 

```bash
>>> city = "Cumilla"
>>> city_itr = iter(city)
>>> city_itr
<str_iterator object at 0x7f4e50908c40>
>>> type(city_itr)
<class 'str_iterator'>
>>> 
```

Here example of calling iteration object by **next()** function : 

```bash
>>> next(city_itr)
'C'
>>> next(city_itr)
'u'
>>> next(city_itr)
'm'
>>> next(city_itr)
'i'
>>> next(city_itr)
'l'
>>> next(city_itr)
'l'
>>> next(city_itr)
'a'
```
<hr />
<br />

<a id="create"></a>
## Create Iterator

We can create iterator by create class. The requirment for this class : 

- must has **\_\_iter__()** method. which return self.
- must has **\_\_next__()** method. This method return element if call it with **next()** function. If iteration complete then it raise **StopIteration** error. 

Here create my_range class by using iterator.
***Program : my_range.py***
```python
# create a simple iteration object
class my_range:
    def __init__(self,start:int,end:int=None,step:int=1):
        self.step = step;
        if end == None : 
            self.start = 0;
            self.end = start;
        else : 
            self.start = start;
            self.end = end;



    # __iter__ method must return self
    def __iter__(self):return self;

    # __next__ method return the next iteration data
    def __next__(self):
        if self.start < self.end :
            temp = self.start;
            self.start += self.step; 
            return temp;
        else :
            # if iteration complete then raise StopIteration error 
            raise StopIteration;
        

# say hello from 0 to 4
print(">>> say hello from 0 to 4 <<<");
for i in my_range(5):
    print("Hello, Mr.",i);

print("\n>>> say ok for every even number between 10 and 20 <<<");
for i in my_range(10,20,2):
    print("Everythink ok : ",i);

```

***Output : my_range.py***
```bash
>>> say hello from 0 to 4 <<<
Hello, Mr. 0
Hello, Mr. 1
Hello, Mr. 2
Hello, Mr. 3
Hello, Mr. 4

>>> say ok for every even number between 10 and 20 <<<
Everythink ok :  10
Everythink ok :  12
Everythink ok :  14
Everythink ok :  16
Everythink ok :  18
```

<hr />
<br />

## Generator
Generator is a one kind of function which return a iterator. In other what, a function where use **yield** keyword called generator. **yield** use for return some data from function and stop executing. If called again it return another yield data if yeild is use again in function otherwise return. Here example : 

```bash
>>> def foo():
...     yield 5;
...     yield 10;
...     yield 12;
...     yield 100;
... 
>>> foo_itr = foo()
>>> foo_itr
<generator object foo at 0x7f575d2c10b0>
>>> type(foo_itr)
<class 'generator'>
>>> next(foo_itr)
5
>>> next(foo_itr)
10
>>> next(foo_itr)
12
>>> next(foo_itr)
100
>>> next(foo_itr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Here create my_range function by generator : 

***Program : yield.py***
```python
def my_range(start:int,end:int=None,step:int=1):
    if end == None : 
        end = start;
        start = 0;

    while start < end :
        yield start;
        start += step;

if __name__ == "__main__":
    # say hello from 0 to 4
    print(">>> say hello from 0 to 4 <<<");
    for i in my_range(5):
        print("Hello, Mr.",i);

    print("\n>>> say ok for every even number between 10 and 20 <<<");
    for i in my_range(10,20,2):
        print("Everythink ok : ",i);
```

***Output : yield.py***
```bash
>>> say hello from 0 to 4 <<<
Hello, Mr. 0
Hello, Mr. 1
Hello, Mr. 2
Hello, Mr. 3
Hello, Mr. 4

>>> say ok for every even number between 10 and 20 <<<
Everythink ok :  10
Everythink ok :  12
Everythink ok :  14
Everythink ok :  16
Everythink ok :  18
````

<br />
<hr />

[< Go Back](./../part_4.md)
---------------------------