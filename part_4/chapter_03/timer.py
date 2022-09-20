import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time();
        print(func.__name__);
        func(*args,**kwargs);
        end = time.time();
        
        details = ">>> Function took {:.2f} seconds <<<".format(end-start);
        print(details,"\n");
        
    return wrapper
    
@timer 
def sleep_func(s):
    time.sleep(s);
    
@timer
def serial_sum(n):
    s = 0;
    for i in range(1,n+1):
        s += i;

    print(str(n)+"nth","Sum is : ",s);

@timer
def serial_sum_two(n):
    s = ((n+1)*n)//2;
    print(str(n)+"nth","Sum is : ",s);

n = 10000000;   
sleep_func(1.5);
serial_sum(n);
serial_sum_two(n);