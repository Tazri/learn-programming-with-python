from unittest import result


def function() :
    n = input(); # O(1)
    n = int(n); # O(1)
    result = n *(n+1) / 2 # O(1)
    return result; # O(1)

'''
Here function time coplexity : 
O(function) = O(1) + O(1) + O(1) + O(1) 
            = 4 * O(1) 
            = O(1) 

Here function space complexity : 
O(1) -> for n variable
O(1) -> for result variable

total : 2*O(1) -> O(1) 

time complexity : O(1)
space complexity : O(1) 
'''