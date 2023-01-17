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