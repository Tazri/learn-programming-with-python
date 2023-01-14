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