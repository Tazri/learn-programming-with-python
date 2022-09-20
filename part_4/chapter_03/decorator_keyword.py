def deco(func):
    def wrapper(*args,**kewargs):
        print("start calling function with :",args,"and",kewargs);
        func(*args,**kewargs);
        print(">>> Function Finish <<<\n\n");
        
    return wrapper;
    

@deco
def greeting(g,name):
    print(g+",",name+"!");
    
greeting("Hi","Anonymo");