import subprocess

result = subprocess.run(["rm","xyz.xyz"],capture_output=True);

print("> result.returncode : ",result.returncode);
print("> result.stdout : ",result.stdout);
print("> result.stderr :",result.stderr);

'''
output : 
$ python3 ./08.sub_process_error.py 
> result.returncode :  1
> result.stdout :  b''
> result.stderr : b"rm: cannot remove 'xyz.xyz': No such file or directory\n"
'''