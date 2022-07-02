import random

number = random.randint(0,1000);
high = 1000;
low = 0;
attempt = 0;


while high >= low : 
    input_number = (high + low)//2;
    print("My guess is  : ",input_number);
    attempt += 1;

    if input_number == number : 
        print("Your guess is correct in attemp",attempt,"Number is ",number,":)");
        break;

    elif input_number < number :
        print("Your number is not correct. :("); 
        low = input_number + 1;
    
    elif input_number > number :
        print("your number is not correct. :(");
        high = input_number - 1;
