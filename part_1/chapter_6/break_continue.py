while True : 
    n = input("Please enter a number : ");
    n = int(n);

    if n < 0 : 
        print("We only allow positive number. Please try again.");
        continue;

    if not n : break;

    print("Square of",n,"is",n*n);

