import subprocess

try : 
    result = subprocess.run(["sleep","5"],capture_output=True,timeout=1);
except subprocess.TimeoutExpired:
    print("Timeout Expired");

'''
output : 
$ python3 ./09.subprocess_timeout.py 
Timeout Expired
'''