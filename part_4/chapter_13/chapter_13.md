Chapter 13 : Work With Operating System
=======================================

Table of Conent : 

<hr />

## OS Module
Here some method of os : 

Get information by *os.uname()*
```py
>>> import os
>>> os_info = os.uname();
>>> os_info
posix.uname_result(sysname='Linux', nodename='debian', release='5.10.0-19-amd64', version='#1 SMP Debian 5.10.149-2 (2022-10-21)', machine='x86_64')
>>> 
```

More about *os.uname()* : 
```py
>>> os_info = os.uname();
>>> 
>>> os_info.machine
'x86_64'
>>> os_info.sysname
'Linux'
>>> os_info.nodename
'debian'
>>> 
```

> 🔴 os.uname() dose not work in windows :(

<hr />

## Create directory wity python

We can create directory with *os.mkdir()* : 
```py
import os

# here the directory name 
image_directory_name = "images";

# create directory by 'os.mkdir()' method
os.mkdir(image_directory_name);
```

*os.path.exists(directory)* use for check directory is exist or not.
```py
import os

# directory name
dir_name = "images";

if os.path.exists(dir_name) == True : 
    print("> Directory is already exists.");
else : 
    os.mkdir(dir_name);
    print("> Directory is created successfully");

'''
Output :
> Directory is already exists.
'''
```

## scandir