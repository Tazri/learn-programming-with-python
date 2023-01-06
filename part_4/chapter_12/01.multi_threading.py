import time
import threading

def please_sleep(sec=3.1): # i/o bound task
    print(".........Sleeping :)");
    time.sleep(sec);

t1 = time.perf_counter();

thread_list = [threading.Thread(target=please_sleep) for func in range(5)];

for th in thread_list:
    th.start();

t2 = time.perf_counter();
time_spent = t2 - t1;

print(f"\n> time spent : {round(time_spent,2)}");

'''
output : 
.........Sleeping :)
.........Sleeping :)
.........Sleeping :)
.........Sleeping :)
.........Sleeping :)

> time spent : 0.0
'''