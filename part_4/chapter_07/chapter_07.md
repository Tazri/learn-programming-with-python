Chapter 07 : Use of bisect Module 
============================
table of content : 
- [Chapter 07 : Use of bisect Module](#chapter-07--use-of-bisect-module)
  - [making insort](#making-insort)
  - [making insort using binary search](#making-insort-using-binary-search)
  - [bisect](#bisect)
  - [insort function make by bisect](#insort-function-make-by-bisect)
  - [using bisect insort function](#using-bisect-insort-function)
  - [Example Compare](#example-compare)
  - [< Go Back](#-go-back)

## making insort
Here make function which append a item in list in sort.

***Program : insort.py***
```python
# find_index -> find index for x in list li
def find_index(li:list,x:int)->int:
    for i in range(len(li)):
        if li[i] > x : 
            return i;
    
    return len(li);

# insort -> insert element in list
def insort(li:list,x:int)->list : 
    index = find_index(li,x);

    li.append(x);

    for i in range(len(li)-2,index-1,-1):
        li[i+1] = li[i];

    li[index] = x;

    return li;


if __name__ == "__main__":
    li = [1,2,4,7,8];
    print("li : ",li);

    print("after insort(li,3) :");
    insort(li,3);
    print(li);

    print("after insort(li,10) :");
    insort(li,10);
    print(li);

    print("after insort(li,15) :");
    insort(li,15);
    print(li);
```

output : 
```bash
li :  [1, 2, 4, 7, 8]
after insort(li,3) :
[1, 2, 3, 4, 7, 8]
after insort(li,10) :
[1, 2, 3, 4, 7, 8, 10]
after insort(li,15) :
[1, 2, 3, 4, 7, 8, 10, 15]
```

<hr />
<br />

## making insort using binary search
Create **insort** function using binary search.


***Program : binary_insort***
```python
def binary_find_index(li:list,x:int,low:int=0,high=None)->int:
    # if item is 0
    if high == None :
        high = len(li) - 1;

    start_high = high;

    items = high - low + 1; # calculate how many item
    
    # if list was 0
    if items == 0 : return low;
    
    # list contain only one item
    if items == 1 :
        if li[low] > x : return low;
        else : return low+1;


    # otherwise
    middle = (low+high) // 2;
    mid = None;

    while low < high :
        mid = (low+high)//2;
        if li[mid] == x : 
            return mid ;
        elif li[mid] < x : 
            low = mid + 1;
        elif li[mid] > x:
            high = high - 1;


    if mid < middle : 
        return 0;
    elif mid > middle : 
        return start_high + 1;
    elif high == low : 
        return high;

def insort_binary(li:list,x:int,low:int=0,high:int=None)->list:
    # if high None
    if high == None : high = len(li) - 1;

    target_index = binary_find_index(li,x);

    # if target index is outof the list
    if target_index >= len(li) :
        li.append(x); # inject x into the li
        return li;

    # otherwise
    li.append(x); # inject x into the li
    for i in range(len(li)-2,target_index-1,-1):
        li[i+1] = li[i];
        
    li[target_index] = x;
    return li;

if __name__ == "__main__":
    li = [1,2,4,7,8];
    print("li : ",li);

    print("after insort(li,3) :");
    insort_binary(li,3);
    print(li);

    print("after insort(li,10) :");
    insort_binary(li,10);
    print(li);

    print("after insort(li,15) :");
    insort_binary(li,15);
    print(li);

    print("after insort(li,2) :");
    insort_binary(li,2);
    print(li);

    print("after insort(li,-1) :");
    insort_binary(li,-1);
    print(li);
```

output : 
```bash
li :  [1, 2, 4, 7, 8]
after insort(li,3) :
[1, 2, 3, 4, 7, 8]
after insort(li,10) :
[1, 2, 3, 4, 7, 8, 10]
after insort(li,15) :
[1, 2, 3, 4, 7, 8, 10, 15]
after insort(li,2) :
[1, 2, 2, 3, 4, 7, 8, 10, 15]
after insort(li,-1) :
[-1, 1, 2, 2, 3, 4, 7, 8, 10, 15]
```
<hr />
<br />

## bisect

Here a table wich explain bisect functions like :  **bisect_left()**, **bisect_right()**, **bisect()** , **insort_right()**,**insort_left()** and **insort()**.

| function                    | description                                  |
|-----------------------|------------------------------------|
| bisect_right(a,x,lo=0,hi=len(a)) | This function find a index for x in list which is **a**. The index is insort from right |
| bisect(a,x,lo=0,hi=len(a)) | It work like **bisect_right()** |
| bisect_left(a,x,lo=0,hi=len(a))| It work like **bisect_right()** but it return index from left. |
| insort_right(a,x) | Insert x in list **a** insort way from right |
| insort(a,x) | Work like **insort_right()** |
| insort_left(a,x) | Insert x in list **a** insort way from left |

Here example of using bisect :

***Program : using bisect***
```bash
>>> from bisect import bisect, bisect_left, bisect_right
>>> li = [1,3,3,3,4]
>>> 
>>> # bisect_left take list and item and return index where it place well in list as well in sort from left
>>> bisect_left(li,2)
1
>>> bisect_right(li,3)
4
>>> bisect_left(li,3)
1
>>> # bisect_right work like bisect_left but it count index from right
>>> bisect_right(li,3)
4
>>> bisect_left(li,4)
4
>>> bisect_right(li,4)
5
>>> # bisect work like bisect_right
>>> bisect(li,4)
5
>>> 
```

<hr />
<br />

## insort function make by bisect
Make the same **insort()** function using by **bisect** module.

***Program : make_bisect_insort.py***
```python
from bisect import bisect

def insort(li:list,x:int,low:int=0,high:int=None):
    if high == None : 
        high = len(li) - 1;

    # find the index
    index =  bisect(li,x,low,high);
    li.insert(index,x);

    return li;

if __name__ == "__main__":
    for n in range(11):
        li = [1,2,2,3,4,6,8,9];

        print("> li : ",li);
        print("> li <-(",n,") insert");
        insort(li,n);
        print("> li : ",li);
        print("-------------------------------\n");
```

output : 
```bash
# ouput in the 'make_bisect_insort.py' file
```

<hr />
<br />

## using bisect insort function
Using bisect **insort()** function.

***Program : bisect_insort.py***
```python
from bisect import insort 

if __name__ == "__main__":
    for n in range(11):
        li = [1,2,2,3,4,6,8,9];

        print("> li : ",li);
        print("> li <-(",n,") insert");
        insort(li,n);
        print("> li : ",li);
        print("-------------------------------\n");
```

output : same like 'make_bisect_insort.py'

<hr />
<br />

## Example Compare
Here create two function. **calculate_grade()** and **calculate_grade_bisect()**. Both return the grade. But one create to using bisect module. Compare them which is faster.

***Program : cheking_time.py***
```python
import time
from bisect import bisect

# create decorator for calculating funciton run time
def deco(func):
    def wrapper(num:int):
        start = time.time();
        result = func(num);
        end = time.time();
        need_time = end-start;
        return [result,need_time];

    return wrapper;

def calculate_grade(marks:int)->str:
    if marks >= 80 : return "A+";
    elif marks >= 70 :return "A";
    elif marks >= 60 : return "A-";
    elif marks >= 50 : return "B";
    elif marks >= 40 : return "C";
    else : return "F";


def calculate_grade_bisect(marks:int)->str:
    grades = ['F','C','B','A-','A','A+'];
    grade_list = [40,50,60,70,80];
    i = bisect(grade_list,marks);
    return grades[i];

if __name__ == '__main__':
    grade_times = [];
    bisect_times = [];
    grade_func = deco(calculate_grade);
    bisect_func = deco(calculate_grade_bisect);

    for i in range(101):
        gresult = grade_func(i);
        bresult = bisect_func(i);

        assert gresult[0] == bresult[0], "Test Input : "+i;
        grade_times.append(gresult[1]);
        bisect_times.append(bresult[1]); 

    
    average_time_for_grade = sum(grade_times)/len(grade_times);
    average_time_for_bisect = sum(bisect_times)/len(bisect_times);

    print("> calculate_grade need to time average : ",average_time_for_grade);
    print("> calculate_grade_bisect Need to time average : ",average_time_for_bisect);
```

output : 
```bash
>>> calulate_grade time <<<
> average :  3.8241395855894185e-07
> minimum :  2.384185791015625e-07
> maximum :  1.430511474609375e-06

>>> calculate_grade_bisect time <<<
> average :  6.39717177589341e-07
> minimum :  2.384185791015625e-07
> maximum :  1.0013580322265625e-05
```

<hr />
<br />

[< Go Back](./../part_4.md)
-----------------------------