import io 

filename = "file.txt";
mode = "r";

try :
    with open(filename,mode) as file :
        content = file.read()
        print(content);
except FileNotFoundError :
    print(filename,"not found.Please check if the file's name is correct.");
except io.UnsupportedOperation :
    print("Are you sure", filename,"is readablle ? ");
except Exception as e :
    print(e);