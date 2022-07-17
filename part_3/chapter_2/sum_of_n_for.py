def n_sum() :
    n = input(); # O(1)
    n = int(n); # O(1)
    sum = 0; # O(1)

    for i in range(1,n+1) : # iterate n'th time
        sum += i; # O(n)

    return sum; # O(1)

'''
Calculate function time complexity : 
O(n_sum()) = O(1) + O(1) + O(1) + O(n) + O(1)
           = 4 * O(1) + O(n) 
           = O(n)

Calculate function space complexity : 
O(1) -> for n variable
O(1) -> for sum variable
O(1) -> for i variable
total space complexity : O(1) + O(1) + O(1) 
                       : O(1) 

Time complexity    : O(n)
Space complexity   : O(1)
'''