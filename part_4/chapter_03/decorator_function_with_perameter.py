def deco(func):
    def wrapper(*args,**kwargs):
        print(">>> call with args",args,"<<<")
        func(*args)
        print(">>> function call is finish <<<\n")
        
    return wrapper

def greeting(greet,name):
    print(greet+",",name);
    
    
fnc = deco(greeting);

fnc('hello','anonymo')