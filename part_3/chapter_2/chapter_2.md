Chapter 2 : Time and Space Complexity 
=====================================

## Time Complexity
The **time complexity** of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input.

<hr />

## Space Complexity
The **space complexity** of an algorithm quantifies the amount of space by a an algorithm to run as a function of the length of the input.Space complexity of an algorithm denotes the total space used or needed by the algorithm for its working, for various input sizes. 

<hr />

## Cases
An algorithm can have different time and space for different inputs. It may take 1 second for some input and 10 seconds for some other input. So algorithm take different time for different input case. This ca be divided into three cases : 

### **Best Case** 
This is **lower bound** on running time of an algorithm. We must know that case that causes the minimum number of operations to be executed.

### **Average Case**
We calculate the running time for all possible inputs, sum all the calculated values and divide the sum by the total number of inputs. We must know (or predict) distrubution of cases.

### **Worst Case**
This is **upper bound** on running time of an algorithm. We must know the case that causes the maximum number of operations to be executed

<hr />

## Asymptotic Notation 
We use **Asymptotic Notation** to analyse any algorithm and based on that we find the most efficient algorithm . Here in asymptotic notation, we do not consider the system configaration, rather we consider the order of growth of the input. We try to find how the time or the space taken by the algorithm will increase/decrease after increasing/decreasing the input size. 

There are three asymptotic notation that are used to represent the time complexity of an algorithm. They are : 

1. θ Notation (theta)
1. Big O Notation
1. Ω Notation


### **θ Notation**
The **θ notation** is used to find the average bound of an algorithm. It defines an upper bound and a lower bound, and your algorihtm will lie in between these level. So if a function is g(n), then the theta representation is showen as **θ(g(n))** and the relation is showen as : 

> θ(g(n)) = {f(n) : there exist positive constants c1, c2 and n0 such that 0 <= c1g(n) <= f(n) <= c2g(n)  for all n >= n0}

### **Ω Notation**
The **Ω notation** denotes the lower bound of an algorithm. The time taken by the algorithm can't be lower that this. In other words, this is ths fastest time in which the algorithm will return a result. Its time taken by the algorithm when provided with its best-case input. So if a function is g(n), then the omega representation is showen as **Ω(g(n))** and the relation is showen as : 

> Ω(g(n)) = {f(n) : there exist positive constants c and n0 such that 0 <= cg(n) <= f(n) for all  n >= n0}

### **Big O Notation**
The **big O notation** defines the upper bound of any algorithm. You algorithm can't take more time than this time. In other words we can say that the big O notation denotes the maximum time taken by an algorithm or the worst case time complexity of an algorithm. So, big O notation is the must used notation for the time complexity of an algorithm. So, if a function is g(n), then the big O representation of g(n) is shown as O(g(n)) and the relation is showen as: 

> O(g(n)) = {f(n) : there exist positive constants c and n0 such that 0 <= f(n) <= cg(n) for all n >= n0}

Some big o complexity : 

1. O(1) -> constant time
1. O(n) -> linear time
1. O(n²) -> quadratic time
1. O(log n) -> logarithmic time

<hr />

### Example some time complexity : 

***Program : sum.py***
```python
number_first = 10; # O(1)
number_second = 20; # O(1)
result = number_first + number_second; # O(1)

'''
Calculate above code time coplexity is : 
O(1) + O(1) + O(1) 
= 3 * O(1)

3*O(1) write as O(1) 

O(1) called order of 1
'''
```

***Program : sum_of_n.py***
```python
from unittest import result


def function() :
    n = input(); # O(1)
    n = int(n); # O(1)
    result = n *(n+1) / 2 # O(1)
    return result; # O(1)

'''
Here function time coplexity : 
O(function) = O(1) + O(1) + O(1) + O(1) 
            = 4 * O(1) 
            = O(1) 

Here function space complexity : 
O(1) -> for n variable
O(1) -> for result variable

total : 2*O(1) -> O(1) 

time complexity : O(1)
space complexity : O(1) 
'''
```

***Program : sum_of_n_for.py***
```python
def n_sum() :
    n = input(); # O(1)
    n = int(n); # O(1)
    sum = 0; # O(1)

    for i in range(1,n+1) : # iterate n'th time
        sum += i; # O(n)

    return sum; # O(1)

'''
Calculate function time complexity : 
O(n_sum()) = O(1) + O(1) + O(1) + O(n) + O(1)
           = 4 * O(1) + O(n) 
           = O(n)

Calculate function space complexity : 
O(1) -> for n variable
O(1) -> for sum variable
O(1) -> for i variable
total space complexity : O(1) + O(1) + O(1) 
                       : O(1) 

Time complexity    : O(n)
Space complexity   : O(1)
'''
```

***Program : count.py***
```python
def demo(n) : 
    n = int(n); # O(1)

    count = 0; # O(1)

    for i in range(n) : # iterate n'th time
        for j in range(n) : # iterate n²'th time
            count += 1; # O(n * n) = O(n²)

    return count; # O(1)

'''
Calculate demo time complexity : 
O(demo(n)) = O(1) + O(1) + O(n²) + O(1)
           = 3*O(1) + O(n²)
           = O(n²)

Calculate demo space complexity : 
O(1) -> for n variable
O(1) -> for count variable
total space complexity : O(1) + O(1) 
                       = O(1)

Time Complexity : O(n²)
Space Complexity : O(1)

'''


if __name__ == "__main__" : 
    print("demo(5) : ",demo(5));
    print("demo(3) : ",demo(3));
    print("demo(6) : ",demo(6));
    print("demo(7) : ",demo(7));
    print("demo(2) : ",demo(2));
```

***Output : count.py***
```bash
$python3 count.py 
demo(5) :  25
demo(3) :  9
demo(6) :  36
demo(7) :  49
demo(2) :  4
```
<hr />
<br />

[< Go Back](./../part_3.md)
---------------------------