import subprocess

result = subprocess.run(["cal"],capture_output=True);

print("> result.returncode : ",result.returncode);
print("> output result.stdout.decode() : ");
print(result.stdout.decode());

'''
$ python3 ./07.subprocess_stdout.py 
> result.returncode :  0
> output result.stdout.decode() : 
    January 2023      
Su Mo Tu We Th Fr Sa  
 1  2  3  4  5  6  7  
 8  9 10 11 12 13 14  
15 16 17 18 19 20 21  
22 23 24 25 26 27 28  
29 30 31              
   
'''
