terminate = False;

while not terminate : 
    number_1 = int(input("Please Enter A Number : "));
    number_2 = int(input("Please Enter Another Number : "));

    while True : 
        operation = input("Please enter add/sub or quit to exit : ");
        
        # this for quit
        if operation == "quit" : 
            terminate = True;
            break;
        
        # this for others operation
        if operation not in ["add","sub"] : 
            print("Uknown operation!");
            continue;

        # this for add
        if operation == "add" : 
            print("Result is : ",number_1 + number_2);
            break;
        
        # this for sub 
        if operation == "sub" : 
            print("Result is : ",number_1 - number_2);
            break;
