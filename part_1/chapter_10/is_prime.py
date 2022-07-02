def is_prime(n) : 
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


while True :
    n = input("Please enter the number or 0 to exit : ");
    n = int(n);

    if not n : 
        print(">>> PROGRAM TERMINATE <<<");
        break;
    
    elif is_prime(n) :
        print(n,"is prime number.");
    else : 
        print(n,"is not prime number.");