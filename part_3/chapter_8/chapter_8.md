Chapter 8 : Recursion
=====================

## What is Recursion
Recursion means **"defining a problem in terms of itself."** This can be very powerful tool in writting algorithms. Recursion comes directly from Mathematics, where there are many examples of expressions written in terms of themselves. For example, the Fibonacci is defined as : 
> F(i) = F(i-1) + F(i-2)

------------------------------------------------------

## What is Recursive Function 
When a function in the program which can capable to called itslef directly or indirectly called **Recursive Function**.

**Example of recursion function in python :**
```python
def function():
    # statement
    function() # called it self
```
------------------------------------------------------

## Example of Recursive Funciton in Python
**Find factorial by recursive function :**
```python
def factorial(n):
    if n < 0 :
        return 1;
    elif n in [0,1] :
        return 1;
    else :
        return n*factorial(n-1);

if __name__ == "__main__":
    print('factorial(5)',factorial(5));
    print('factorial(0)',factorial(0));
    print('factorial(-5)',factorial(-5));
    print('factorial(1)',factorial(1));
    print('factorial(3)',factorial(3));
    print('factorial(4)',factorial(4));
```


```bash
$python3 factorial.py 
factorial(5) 120
factorial(0) 1
factorial(-5) 1
factorial(1) 1
factorial(3) 6
factorial(4) 24
```

**Example of find fibonacci term by recursive function :**
```python
def fibonacci(n) :
    if n in [1,2] :
        return 1;
    else :
        return fibonacci(n-1) + fibonacci(n-2);

if __name__ == "__main__":
    print('fibonacci(1) : ',fibonacci(1));
    print('fibonacci(2) : ',fibonacci(2));
    print('fibonacci(3) : ',fibonacci(3));
    print('fibonacci(4) : ',fibonacci(4));
    print('fibonacci(5) : ',fibonacci(5));
    print('fibonacci(6) : ',fibonacci(6));
```

```bash
$python3 fibonacci.py 
fibonacci(1) :  1
fibonacci(2) :  1
fibonacci(3) :  2
fibonacci(4) :  3
fibonacci(5) :  5
fibonacci(6) :  8
```

**Implament Binary Search by recursive function :**
```python
def binary_search(_list,_target,_left = 0,_right = None):
    # by default value of right
    if _right == None :
        _right = len(_list) - 1;


    # calculate mid 
    mid = (_left+_right)//2;

    # if left > right, that means target not in list
    if _left > _right :
        return None;

    # if mid index is target index
    if _list[mid] == _target : 
        return mid;


    # if mid index is less than target index
    if _list[mid] < _target:
        _left = mid + 1;
        return binary_search(_list,_target,_left,_right);
    
    # if mid index is greater than target index
    _right = mid - 1;
    return binary_search(_list,_target,_left,_right);
```

Test Code :
```python
if __name__ == "__main__":
    L = [1,2,3,5,6,7,8,9];
    

    is_fail = False;
    for x in range(1,11):
        position = binary_search(L,x);


        if position == None :
            print(position);
            if x in L :
                print(L);
                print(">>>",x,"is in L but function returned None");
                is_fail = True;
            else:
                print('>>> ',x,'not in list');
        else :
            if L[position] == x :
                print(">>>",x,"found in correct position.");
            else :
                print(">>> return",position,"for",x,"which is not correct.");
                is_fail = True;

    
    print("\n.....\n....\n...\n..\n.");
    if is_fail :
        print(">>> Test Failed :( <<<");
        print(">>> Debug Your Code <<<");
    else :
        print(">>> Test Successfully Passed :) <<<");
        print(">>> Go To Drink A Cup Of Tea <<<");

```

Test Result : 
```bash
$python3 binary_serach.py 
>>> 1 found in correct position.
>>> 2 found in correct position.
>>> 3 found in correct position.
None
>>>  4 not in list
>>> 5 found in correct position.
>>> 6 found in correct position.
>>> 7 found in correct position.
>>> 8 found in correct position.
>>> 9 found in correct position.
None
>>>  10 not in list

.....
....
...
..
.
>>> Test Successfully Passed :) <<<
>>> Go To Drink A Cup Of Tea <<<
```

<hr />
<br />

[< Go Back](./../part_3.md)
-------------------------