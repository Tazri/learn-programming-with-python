Chapter 3 : System of Test Code 
===============================

## Using For loop to test function : 
First create the function and test the function as well.
***Program : average_list.py***
```python
def average_list(l) :
    if not l : 
        return None;

    return sum(l) / len(l);


if __name__ == "__main__" : 
    ## Test the average list function
    test_cases = [
        [[45,6,4,3,2,6],11],
        [[3,2],2.5],
        [[3,4],3.5],
        [[2,2,2,2],2],
        [[4,6,8,10],7],
        [[],None],
        # [test_case,expected_result]
    ]

    print(">>>🧪🧪🧪 Test Case Started 🧪🧪🧪<<<\n");

    for case in test_cases :
        result = average_list(case[0]);
        expected_result = case[1];

        if result == expected_result : 
            print(">>> ✅✅✅ Test Pass. Expected Result : ", expected_result," received result : ",result);
        else : 
            print(">>> ❌❌❌ Test Failed. Expected Result : ", expected_result," received result : ",result);
            break;
```
***Output : average_list.py***
```bash
$python3 average_list.py 
>>>🧪🧪🧪 Test Case Started 🧪🧪🧪<<<

>>> ✅✅✅ Test Pass. Expected Result :  11  received result :  11.0
>>> ✅✅✅ Test Pass. Expected Result :  2.5  received result :  2.5
>>> ✅✅✅ Test Pass. Expected Result :  3.5  received result :  3.5
>>> ✅✅✅ Test Pass. Expected Result :  2  received result :  2.0
>>> ✅✅✅ Test Pass. Expected Result :  7  received result :  7.0
>>> ✅✅✅ Test Pass. Expected Result :  None  received result :  None
```

<hr />
<br />

## Using assert keyword 
**assert** throw error if code return error. Here example : 

```bash
>>> assert 2 == 2
>>> assert 2 == 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> assert 2 == 4, "2 is not equal to 4"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: 2 is not equal to 4
>>> 
```

It also print message if throw error. Here test **average_list** function by assert : 
***Program : assert_average_list.py***
```python
def average_list(l) :
    if not l : 
        return None;

    return sum(l) / len(l);


if __name__ == "__main__" : 
    ## Test the average list function
    test_cases = [
        [[45,6,4,3,2,6],11],
        [[3,2],2.5],
        [[3,4],3.5],
        [[2,2,2,2],2],
        [[4,6,8,10],7],
        [[],None],
        [[],3], # wrong result
        # [test_case,expected_result]
    ]

    for case in test_cases : 
        result = average_list(case[0]);
        expected_result = case[1];

        assert result == expected_result, "💣💣 Test Failed 💣💣 Produced Incorrect Result" 
```

***Output : assert_average_list.py***
```bash
$python3 assert_average_list.py 
Traceback (most recent call last):
  File "/home/tazri/Documents/work-place/python/learn-programming-with-python/part_3/chapter_3/assert_average_list.py", line 25, in <module>
    assert result == expected_result, "💣💣 Test Failed 💣💣 Produced Incorrect Result" 
AssertionError: 💣💣 Test Failed 💣💣 Produced Incorrect Result
```
<hr />
<br />

## Unit test by pytest
Here test average_list by pytest module : 

***Program : pytest_average_list.py***
```python
def average_list(l) :
    if not l : 
        return None;

    return sum(l) / len(l);


def test_average_list() : 
    assert 3.0 == average_list([1,2,3,4,5])
```

***Output : pytest_average_list.py***
```bash
 $pytest pytest_average_list.py 
============================= test session starts ==============================
platform linux -- Python 3.9.2, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/tazri/Documents/work-place/python/learn-programming-with-python/part_3/chapter_3
collected 1 item                                                               

pytest_average_list.py .                                                 [100%]

============================== 1 passed in 0.01s ===============================
```

<hr />
<br />

## Table Driven Test 
Here table driven tested **average_list** function by pytest module : 
***Program : table_driven_average_list.py***
```python
def average_list(l) :
    if not l : 
        return None;

    return sum(l) / len(l);


def test_average_list() :
    test_cases = [
        {
            "name" : "simple case 1",
            "input" : [45,6,4,3,2,6],
            "expected" : 11
        },
        {
            "name" : "simple case 2",
            "input" : [3,2],
            "expected" : 2.5
        },
        {
            "name" : "simple case 3",
            "input" : [3,4],
            "expected" : 3.5
        },
        {
            "name" : "simple case 4",
            "input" : [2,2,2,2],
            "expected" : 2
        },
        {
            "name" : "simple case 5",
            "input" : [4,6,8,10],
            "expected" : 7
        },
        {
            "name" : "simple case 6",
            "input" : [],
            "expected" : None
        }
    ]

    for case in test_cases :
        assert case['expected'] == average_list(case['input']), case['name']
```

***Output : table_driven_average_list.py***
```bash
$pytest table_driven_average_list.py 
============================= test session starts ==============================
platform linux -- Python 3.9.2, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/tazri/Documents/work-place/python/learn-programming-with-python/part_3/chapter_3
collected 1 item                                                               

table_driven_average_list.py .                                           [100%]

============================== 1 passed in 0.01s ===============================
```

<hr />
<br />

[< Go Back](./../part_3.md)
----------------------------