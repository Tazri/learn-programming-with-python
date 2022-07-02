import timeit

def is_prime(n = 51) : 
    if n == 1 : 
        return False;
    elif n == 2 : 
        return True
    elif n % 2 == 0 : 
        return False;
    else :
        rt_n = int(n**0.5);

        for i in range(3,rt_n+1,2) : 
            if not n % i :
                return False;
        
        return True;


t = timeit.timeit(is_prime);

print("Total time for timeit : ",t);