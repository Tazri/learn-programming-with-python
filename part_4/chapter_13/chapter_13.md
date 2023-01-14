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