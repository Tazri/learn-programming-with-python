import subprocess,time

start = time.perf_counter();

result = subprocess.run(["sleep","5"]);

end = time.perf_counter();
spent = end - start;

print("> result.returncode : ",result.returncode);
print("> total time spent : ",round(spent,2));

'''
$ python3 ./06.subprocess_sleep.py 
> result.returncode :  0
> total time spent :  5.0
$ 
'''