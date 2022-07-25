def fibonacci(n) :
    if n in [1,2] :
        return 1;
    else :
        return fibonacci(n-1) + fibonacci(n-2);

if __name__ == "__main__":
    print('fibonacci(1) : ',fibonacci(1));
    print('fibonacci(2) : ',fibonacci(2));
    print('fibonacci(3) : ',fibonacci(3));
    print('fibonacci(4) : ',fibonacci(4));
    print('fibonacci(5) : ',fibonacci(5));
    print('fibonacci(6) : ',fibonacci(6));