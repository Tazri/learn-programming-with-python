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
## Create multi threading program

Here the syntax to create multi threading program : 
```py
import threading # threding package use for create mutliple thread

# create thread with function
thread = threading .Tread(target=function_name);

# run the thread
thread.start()

# join the thread with main join
thread.join()
```

Here the example of multi threading : 

```py
import time
import threading

def please_sleep(sec=2.2): # i/o bound task
    print(".......sleep :)");
    time.sleep(sec);

# counting the time
t1 = time.perf_counter();

# create five thread with 'please_sleep' function
thread_list = [threading.Thread(target=please_sleep) for _ in range(5)];

# start the thread
for thread in thread_list:
    thread.start();

# joint the thread with main thread
for thread in thread_list:
    thread.join();

t2 = time.perf_counter();
time_spent = t2 - t1;

print(f'\n> Time Spent : {round(time_spent,2)}');

'''
.......sleep :)
.......sleep :)
.......sleep :)
.......sleep :)
.......sleep :)

> Time Spent : 2.2
'''
```

***try to run a function which is **cpu bound task** with multithreadin :***

```py
import time
import threading

def compute_fnc(): # cpu bound task
    print("Computing..........");
    for x in range(1000000):
        _ = pow(x,123);
    print(".....Compute finished.\n");

# counting time
t1 = time.perf_counter();

# create 5 thread for 'compute_func'
thread_list = [threading.Thread(target=compute_fnc) for _ in range(5)];

# start the thread
for thread in thread_list:
    thread.start();

# join the thread with main thread
for thread in thread_list:
    thread.join();

# calculate total time spent
t2 = time.perf_counter();
time_spent = round(t2-t1,2);

print(f"\n\n> Total Time spent : {time_spent}");

'''
output : 
Computing..........
Computing..........
Computing..........
Computing..........
Computing..........
.....Compute finished.

.....Compute finished.

.....Compute finished.

.....Compute finished.

.....Compute finished.



> Total Time spent : 17.79
'''
```

<hr />

## Create multi processing program

Here the syntax to create multi processing program : 
```py
import multiprocessing
process = multiproessing.Process(target=function_name);

# start the process
process.start();

# waiting for finis the process
process.join();
```

Here the example of multi processing program in python : 

```py
import time
import multiprocessing

def compute_fnc(): # cpu bound task
    print("Computing..........");
    for x in range(1000000):
        _ = pow(x,123);
    print(".....Compute finished.\n");

# counting time
t1 = time.perf_counter();

# create 5 process of 'compute_fnc()'
process_list = [
    multiprocessing.Process(target=compute_fnc) for _ in range(5)
]

for process in process_list:
    process.start();

for process in process_list:
    process.join();

t2 = time.perf_counter();

time_spent = round(t2-t1,2);

print("\n\n> Time Spent :",time_spent);

'''
Computing..........
Computing..........
Computing..........
Computing..........
Computing..........
.....Compute finished.

.....Compute finished.

.....Compute finished.

.....Compute finished.

.....Compute finished.



> Time Spent : 8.86
'''
```

<hr />

[< Go Back](./../part_4.md)
---------------------------