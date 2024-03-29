Chapter 11 : Some More Data Structure
=====================================

Table of content of this chapter : 

- **[Array](#array)**
- **[Default Dict](#default-dict)**
- **[Counter](#counter)**
- **[Angram Problem](#anagram-problem)**
- **[Deque](#deque)**
- **[heapq](#heapq)**


<hr />

## Array
Python dose not has array but use **array** package for it. Here simple syntax : 

```py
from array import array;

n = array(data_type,list_of_data);
```

Here all datatype for array : 

| Type Code | C Type            | Python Type  | Space (bytes) |
|-----------|-------------------|--------------|---------------|
| b         | signed char       | int          | 1             |
| B         | unsigned char     | int          | 1             |
| h         | signed short      | int          | 2             | 
| H         | unsigned short    | int          | 2             | 
| i         | signed int        | int          | 2             |
| I         | unsigned int      | int          | 2             |
| l         | signed long       | int          | 4             |
| L         | unsigned long     | int          | 4             |
| q         | signed long long  | int          | 8             |
| Q         | unsigned long long| int          | 8             |
| f         | float             | float        | 4             |
| d         | double            | float        | 8             |


Here example of create array in python : 
```py
>>> from array import array
>>> 
>>> nums = array('i',[2,3,5]);
>>> nums
array('i', [2, 3, 5])
>>> nums[0]
2
>>> nums[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: array index out of range
>>>
>>>
>>> n = array('i',[3.4,3,2]);
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: integer argument expected, got float
>>> 
```

<hr />


## Default Dict
Python has defulat dict which use like a normal dictionary but difference is that, if try to access don't exist key from dictionary then it did not throw keyerror. It create a default value for it. Here syntax : 

```py
from collections import defaultdict

l = defalutdict(type);
```

> 🟢 Type is a function which return the default value, int() return the 0

if **type** is **int** then value of every none exist key which try to access is 0 by default. Here type just take a function which return the default value. 

Example here : 
```py
>>> from collections import defaultdict
>>> 
>>> l = defaultdict(int);
>>> 
>>> l
defaultdict(<class 'int'>, {})
>>> l['a'];
0
>>> l
defaultdict(<class 'int'>, {'a': 0})
>>> l['d']
0
>>> l['b'] += 32;
>>> l
defaultdict(<class 'int'>, {'a': 0, 'd': 0, 'b': 32})
>>> 
```

<hr />

## Counter
**Counter** is another function from **collections** package. It take a object and create a dictionary, and make every object as a key with intager value. Here example for **Counter**.

```py
>>> from collections import Counter;
>>> 
>>> c = Counter()
>>> c
Counter()
>>> c['a'] = 3;
>>> c['b'] = 5;
>>> c['d'] = 4;
>>> c
Counter({'b': 5, 'd': 4, 'a': 3})
>>> c['a']
3
>>> c['b']
5
>>> c['c']
0
>>> c['d']
4
>>> 
```

Try to pass various type of argument in Counter function : 
```py
>>> c = Counter(['a','b','d','a','a','a','d']);
>>> c
Counter({'a': 4, 'd': 2, 'b': 1})
>>> c = Counter({'a':4,'b':1,'d':2});
>>> c
Counter({'a': 4, 'd': 2, 'b': 1})
>>> c = Counter(a=4,b=1,d=2);
>>> c
Counter({'a': 4, 'd': 2, 'b': 1})
>>> c = Counter('hello')
>>> c
Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
>>> 
```

Some Counter built-in method : 
```py
>>> c = Counter({'a' : 4, 'd' : 2, 'b' : 1});
>>> 
>>> c.elements()
<itertools.chain object at 0x7f9d7c88ca00>
>>> [x for x in c.elements()]
['a', 'a', 'a', 'a', 'd', 'd', 'b']
>>> 
>>> c.most_common();
[('a', 4), ('d', 2), ('b', 1)]
>>> c.most_common(1);
[('a', 4)]
>>> c.most_common(2);
[('a', 4), ('d', 2)]
>>> d = Counter(a=1, c=3, d=4);
>>> c.subtract(d);
>>> 
>>> c
Counter({'a': 3, 'b': 1, 'd': -2, 'c': -3})
>>> 
>>> c.clear()
>>> c
Counter()
>>> 
```

## Anagram Problem
Here solve the anagram problem on my way. Checking two word is anagram or not : 
```py
from collections import defaultdict
from collections import Counter;


def is_anagram_one(word,target_word): # this is my solution
    # if length is not equal
    if len(word) != len(target_word) :
        return False;

    # create word dict
    word_dict = {};

    # get all character from word to word_dict
    for c in word:
        if word_dict.get(c) :
            word_dict[c] += 1;
            continue;
        
        word_dict[c] = 1;

    # removing all character from word_dict which is in target_word
    for c in target_word:
        if word_dict.get(c) == None:
            return False;
        
        if word_dict.get(c) == 0:
            return False;
        
        word_dict[c] -= 1;
    
    return True;

def is_anagram_two(word,target_word): # book solution
    w1 = "".join(sorted(word));
    w2 = "".join(sorted(target_word));

    if w1 == w2 :
        return True;
    return False;

def is_anagram_three(word,target_word): # using defaultdict
    if len(word) != len(target_word): 
        return False;

    word_dict = defaultdict(int);

    # adding character in word_dict from word
    for c in word:
        word_dict[c] += 1;

    # removing character in word_dict from target_word
    for c in target_word:
        if word_dict[c] == 0: # if word_dict[c] is zero
            return False;

        word_dict[c] -= 1;

    return True;
    
def is_anagram_four(word,target_word)->bool: # using Counter
    return Counter(word) == Counter(target_word);

```

### **[Here all program with testing anagram with output >](./02.testing_anagram.md)**

<hr />

## Deque

**Deque** is a data structure which like a circular queue. It is from **collections** package. Here Example to declare deque : 

```bash
>>> from collections import deque
>>> 
>>> d = deque()
>>> 
>>> d
deque([])
>>> d.extend([1,2,3,4,5,6,7])
>>> d.append(8)
>>> d
deque([1, 2, 3, 4, 5, 6, 7, 8])
>>> d.pop()
8
>>> d.popleft()
1
>>> d
deque([2, 3, 4, 5, 6, 7])
>>> d.appendleft(0)
>>> d
deque([0, 2, 3, 4, 5, 6, 7])
>>> 
```

Define the deque **maxlen**.

```bash
>>> d = deque(maxlen=3)
>>> d.append(1)
>>> d.append(2)
>>> d.append(3)
>>> d
deque([1, 2, 3], maxlen=3)
>>> d.appendleft(5)
>>> d
deque([5, 1, 2], maxlen=3)
>>> 
```

🔴 If try to insert the item at a full deque then it remove first one, and add at possition first then it remove last one.

Create a deque with iterable object :
```bash
deque([1, 2, 3], maxlen=5)
>>> d = deque("abcd",maxlen=5);
>>> d
deque(['a', 'b', 'c', 'd'], maxlen=5)
>>> d = deque("abcd",maxlen=3);
>>> d
deque(['b', 'c', 'd'], maxlen=3)
>>> 
```

### A simple moving average problem 
Give a temperature list and a number k. Then create average of first k number of temerature. Next create average again for n number of temerature from list, but in that case remove first one and add next temperature which is out of k. Then create a list with all average and return it.

**Solution :**
```py
from collections import deque

def get_average(temp_list:list,k:int = 100)->list:
        temp_q = deque(temp_q[:k]);

        sum_temp_q = sum(temp_q);
        average_temp = [sum_temp_q/k];

        for nt in temp_list[k:]: # nt is next temperature
            sum_temp_q = sum_temp_q + nt - sum_temp_q.popleft();
            temp_q.append(nt);
            average_temp.append(sum_temp_q/k);
        
        return average_temp;

```

<hr />

## Heapq

**heapq** is a python built-in package use for create heap. Below some heapq method : 

| method name | description                                                             |
|-------------|-------------------------------------------------------------------------|
| .heapify(li:list) | get a list and make it min heap                                   |
| .heappush(h:list,item) | get a list and number, insert the number in list follow min heap rule |
| .heappop(h:list,item) | remove root data and heapify it again                         |

**Here example of heapify :**
```bash
>>> import heapq
>>> 
>>> li = [3, 5, 2, 1, 3, 4]
>>> heapq.heapify(li)
>>> li
[1, 3, 2, 5, 3, 4]
>>> 
```
**Here example of heappush :**
```bash
>>> li = [3, 5, 2, 1, 3, 4]
>>> h = [];
>>> for item in li:
...     heapq.heappush(h,item);
... 
>>> h
[1, 2, 3, 5, 3, 4]
>>> 
```

### Problem Kth largest number
The problem is that  :
Take a array and a number which is k. Return the k'th largest number from a array. Here I solve a problem using heapq.

#### [Here solve the kth largest problem >](./markdown/kth_largest_number.md)


### Create MaxHeap class using heapq

```py
import heapq

class MaxHeap:
    def __init__(self,items=[]):
        self.h = [x*-1 for x in items];

        if items:
            heapq.heapify(self.h);
        
    def __len__(self):
        return len(self.h);

    def push(self,item):
        heapq.heappush(self.h,-item);
        return self;
    
    def pop(self):
        return -heapq.heappop(self.h);

    def look(self):
        return -self.h[0];
    

if __name__ == "__main__":
    items = [1,3,5,7,9,2,4,6,8,0];
    mx_heap = MaxHeap();
    
    for item in items:
        mx_heap.push(item);

    li = [mx_heap.pop() for _ in range(len(mx_heap))];
    print(f"items : {items}")
    print(f"li : {li}");

'''
output : 
items : [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
li : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
'''
```

### Making Priority Queue
It possible to push item in heap by **heapq.heappush()** function with priority. Here example : 

```py
import heapq as heap

h = [];

# data with priorityqueue
datas = [
    (3,"write code"),
    (2,"write tests"),
    (1,"create specification"),
    (4,"release product")
];

print("Data inserting in priority queue...............");
print("....");
for data in datas:
    # push the with priority
    heap.heappush(h,data);



print("Data Pop Out from Priority Queue : ");
while h:
    data = heap.heappop(h);
    print(f"> data : {data}");

'''
Data inserting in priority queue...............
....
Data Pop Out from Priority Queue : 
> data : (1, 'create specification')
> data : (2, 'write tests')
> data : (3, 'write code')
> data : (4, 'release product')
'''
```

Example of priority queue with **PriorityQueue** Class from **queue** package : 
```py
from queue import PriorityQueue;

pq = PriorityQueue();

# create random priority data
datas = [
    (3,"write code"),
    (2,"write tests"),
    (1,"create specification"),
    (4,"release product")
];

'''
pq.put() use for insert data.
pq.get() use for get data.
pq.qsize() use for know the queue size
'''

print("> pq.put(data).......");
print("......");
for data in datas : 
    pq.put(data);
    
print("\n> pq.get()...........");
while pq.qsize():
    print(f"> pq.get() : {pq.get()}");

'''
ity_queue_package.py 
> pq.put(data).......
......

> pq.get()...........
> pq.get() : (1, 'create specification')
> pq.get() : (2, 'write tests')
> pq.get() : (3, 'write code')
> pq.get() : (4, 'release product')
'''
```

<hr />
<br />

[< Go Back](./../part_4.md)
--------------------------