def fibo(n) :
    if n <= 2 :
        return 1;
    else :
        past_n = 1;
        present_n = 1;

        for i in range(n-2) :
            tem_present_n = present_n;
            present_n = tem_present_n + past_n;
            past_n = tem_present_n;

        return present_n;


while True :
    n = input("Please Enter N or 0 to exit : ");
    n = int(n);

    if not n :
        print("\n>>> PROGRAM TERMINATE <<<");
        break;
    else :
        print(n,"th finbonacci number is : ",fibo(n));