def decorator(func):
    def wrapper():
        print("Here work some functionality before call function.");
        
        print("function calling.");
        func();
        
        print("\nafter the function here work some functionality after call function.");
    
    return wrapper
def hello():
    print("\n>>> Hello, I am Hello function.");
    
fnc = decorator(hello);

print("fnc : ",fnc,"\n");
fnc();