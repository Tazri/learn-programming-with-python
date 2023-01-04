Chapter 12 : Multi Threading and Multi Processing
==================================================

```py
import time;

def please_sleep(sec=1.1):
    print("Sleeping........ for 1.1 sec");
    time.sleep(sec);

def compute_fnc():
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
