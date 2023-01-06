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