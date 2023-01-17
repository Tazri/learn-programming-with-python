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
**scandir** is a os dir method which can take a **path as a string** or take a **DirEntry**  as parameter and return a **ScandirIterator**. **ScandirIterator** is a iterator of **DirEntery**. Some important **DirEntry** Method and property : 

|   Important DirEntery Property   | 
|----------------------------------|

| Method or Property | Description |
|--------------------|-------------|
| .is_dir()          | check is directory or not, return True if it is directory other wise return False |
| .is_file()         | check is file or not, return True if it is file otherwise return False |
| .is_symlink()  | check is symlink or not, return True if it is symlink otherwise return False |
| .name | return the name as string, if it is file then return the name with extention. |

**Here a Program to traverse the directory :**
```py
import os

def get_files_and_directories(path):
    files = [];
    dirs = [];

    with os.scandir(path) as it :
        for entry in it:
            if entry.name.startswith("."):
                continue;
            elif entry.is_dir():
                dirs.append(entry);
            elif entry.is_file():
                files.append(entry.name);

    return (files,dirs);


def traverse_dir(path):
    files = [];
    dirs = [path];

    while dirs:
        dir = dirs.pop(0);
        files,dirs = get_files_and_directories(dir);
        files.extend(files);
        dirs.extend(dirs);

    return files;

if __name__ == "__main__":
    target_path = "./test";
    
    files_and_folders = get_files_and_directories(target_path);

    print("\033[38;2;255;0;255m>>> Path ./test : \033[0m");
    print("\033[38;2;255;0;0m> Files : \033[0m");
    print(files_and_folders[0]);

    print("\n\033[38;2;255;0;0m> Folders : \033[0m");
    print(files_and_folders[1]);


    print("\n\n\033[38;2;255;0;255m>>> all files : ./test\033[0m");
    files = traverse_dir(target_path);
    print(files);

'''
output : 
>>>Path ./test : 
> Files : 
['index.html']

> Folders : 
[<DirEntry 'style'>, <DirEntry 'js'>]


>>> all files : ./test
['button.css', 'text.css', 'img.css', 'button.css', 'text.css', 'img.css']
'''
```


**[Here the biggest program to traverse the folder which is I create :](./markdown/01.traverse_folder.md)**

<hr />

## glob
**glob** is a python package which is use for searhing file or folder which **regex pattern syntax.** Which is frequently use in linux terminal. Here example : 
```py
>>> import glob
>>> 
>>> file_list = glob.glob("./*");
>>> file_list
['./00.create_directory.py', './01.create_folder_if_not_exist.py', './chapter_13.md', './02.traverse_folders.py', './test', './markdown', './03.traverse_directory_in_book.py', './images']
>>> len(file_list)
8
>>> 
```

See all **.py** file by using **recurisve=True** :
```py
>>> import glob
>>> 
>>> file_list = glob.glob("./**/*.py",recursive=True);
>>> file_list
['./00.create_directory.py', './01.create_folder_if_not_exist.py', './02.traverse_folders.py', './03.traverse_directory_in_book.py', './usless_python_file/add.py', './usless_python_file/stylus_text.py']
>>> len(file_list)
6
>>> 
```

## shutil

**shutil** is a python package use for copy all file and folder from one directory to another directory. Here all about shutil in one example :

```python
import shutil

target_dir = "/home/tazri/Documents/work/python/learn-programming-with-python/part_4/chapter_13/empty";
source_dir = "/home/tazri/Documents/work/python/learn-programming-with-python/part_4/chapter_13/usless_python_file";


try:
    shutil.copytree(source_dir,target_dir);
except FileExistsError as err:
    print(err);
except :
    print("Unknown Error - terminating program!");
    raise;


'''
Here all about shutil

shutil.copytree(source_directory_path,target_directory_path);

# don't create the directory for target, it create automatically otherwise it throw error.

shutil.copytree(source_directory_path,target_directory_path,ignore = shutil.ignore_patterns("*.temp"));

here below thing will ignore all file with .temp extention
ignore = shutil.ignore_patterns("*.temp");
'''
```

## os.path
Some os.path function : 

| Function Name | Description                                                                           |
|---------------|---------------------------------------------------------------------------------------|
| os.path.join  | take the two path as a string and return a on path as a string                        |
| os.path.dirname| take the filename with path and return the directory name with path                  |
| os.split      | take a path as string and split the string path into directory name with path and filename |

> 🟢 It safe to add two path using **os.path.join". Because path writing system is vary on os to os. In linux path write like "directory_name/filename" and in windows path write like "directory_name\filename". So use os.path.join is safe.

Here using join method : 
```py
>>> 
>>> os.path.join("home/tazri","documents/")
'home/tazri/documents/'
>>> 
```

Here using dirname : 
```py
>>> import os
>>> 
>>> os.path.dirname("a/b/c/d.py");
'a/b/c'
>>> os.path.dirname("a/b/c/d/");
'a/b/c/d'
>>> 
```

Here using split : 
```py
>>> import os
>>> 
>>> os.path.split("abc/defg/hijk.py");
('abc/defg', 'hijk.py')
>>> os.path.split("abc/defg/");
('abc/defg', '')
>>> 
```

## Environment Variable
**os.getenv** use for get environment variable. Here descripton of **os.getenv** : 

```py
os.getenv("environment_variable_name");

# set default value if environment variable not exist
os.getenv("variable_name",default="default value");

# if value dose not exist then it return None
```

Here the example : 
```py
$ export APIkey="abc1234"
$ 
$ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> 
>>> os.getenv("APIkey");
'abc1234'
>>> os.getenv("secret",default="here is default value");
'here is default value'
>>> 
```

## subprocess
**subprocess** is a package of python which is use for run a process in computer. When subprocess is run then parent process it stop untill sub process is finished. Here the syntax to run a process in python : 

```py
import subprocess

subprocess.run(["command","pass","it","as","list"]);

# example command : ls -l
subprocess.run(["ls","-l"]);
```

**Subprocess.run()** function return a **subprocess.CompletedProcess** object. Here sum important property of **subprocess.CompletedProcess** : 

| property    | description                                                                        |
|-------------|------------------------------------------------------------------------------------|
| .returncode | returncode value 0 if process is successfully completed otherwise 1                |
| .stdout     | store the output as binary string (b'string') decode it by b"string".decode()      |
| .stderr     | store the error as inary string  (b'string') decode it by b"string".decode()       |

```py
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
```

```py
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
```

**capture_output** parameter use for capture the output and store it in the **.stdout** as binary string (b"string"). If throw error then error store in **.stderr** as binary string (b"string").Must be dcode by decode mtheod. For example : **b"string".decode()**. Otherwise output dose not print properly.

Example of **capture_output** :
```py
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
   
```
Example of **.stderr** :
```py
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
```
**timeout** Parameter limit the subprocess run time. If it take more time to run then raise the **subprocess.TimeoutExpired** error. Here example : 
```py
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
```

<hr />
<br />

[< Go Back](./../part_4.md)
--------------------------