def find_fibo(n) :
    if n <= 2 :
        return 1;
    else : 
        past = 1;
        present = 1;

        for i in range(n - 2) :
            past, present = present, past+present;

        return present;

def list_fibo(n) :
    if n <= 2 :
        if n == 2 : return [1,1];
        return [1]
    
    fibo_list = [1,1]

    i = 2;

    while i < n :
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2]);

        i+= 1;

    return fibo_list;


for x in range(1,11) :
    print(find_fibo(x));

print(list_fibo(1));
print(list_fibo(2));
print(list_fibo(10));