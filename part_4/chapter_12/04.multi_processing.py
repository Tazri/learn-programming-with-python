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