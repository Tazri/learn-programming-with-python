Chapter 12 : Multi Threading and Multi Processing
==================================================
Table of Content of this chapter : 

<hr />

## Process and Thread
In Computer Science, a **process** mean a programm running state in computer. Other hand **thread** is a path of execution within a process.

> 🟢 A process is an instance of a program running in a computer.


> 🟢 A thread is a path of execution with a process. In other word, thread is a path.

<hr />

## CPU bound and IO bound Task
A task which defend on cpu that called **CPU bound task.** A task which dose not depend on cpu int called **IO-bound Task.** Here simple diagram on Process : 

![State of Process](./../../asset/diagrams/state_of_process.png)

<hr />

## Create CPU bound and IO bound Task
Here Create two function, one is depend on CPU and another don't. **please_sleep** function is not depend on cpu and **compute_fnc** function is depend on cpu.

```py
import time;


def please_sleep(sec=1.1): # io-bound Task
    print("Sleeping........ for 1.1 sec");
    time.sleep(sec);

def compute_fnc(): # cpu bound task
    print("Computing..........");
    for x in range(1000000):
        _ = pow(x,123);

for func in [please_sleep,compute_fnc]:
    print(f">>>> {func.__name__} :");

    t1 = time.perf_counter();
    func();
    print("after calling finish :")
    t2 = time.perf_counter();
    time_spent = t2 - t1;
    print(f"time spent : {round(time_spent,2)}s");
    print();

'''
>>>> please_sleep :
Sleeping........ for 1.1 sec
after calling finish :
time spent : 1.1s

>>>> compute_fnc :
Computing..........
after calling finish :
time spent : 3.47s
'''
```
