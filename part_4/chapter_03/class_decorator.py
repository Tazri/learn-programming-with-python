class deco:
    def __init__(self,func):
        self.func = func;
        
    def __call__(self,*args,**kwargs):
        print(self.func.__name__);
        self.func(*args,**kwargs);
        print(">>> program finish <<<");
    
@deco
def greeting(g,n):
    print(g+",",n+"!");
    
greeting('Hello',"Anonymo");