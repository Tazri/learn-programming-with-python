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
