import subprocess

result = subprocess.run(["date"]);
print("> result.returncode : ",result.returncode);

'''
output : 
$ python3 ./05.run_subprocess_date.py 
Tue 17 Jan 2023 08:07:35 PM +06
> result.returncode :  0
$ 

'''