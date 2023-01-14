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