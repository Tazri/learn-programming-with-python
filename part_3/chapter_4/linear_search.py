def linear_search(li,x):
    # store length in n
    n = len(li); # O(1)
    i = 0; # O(1)

    while i < n : # n'th iterate
        if li[i] == x : # O(n)
            return i; # O(1)
        
        i = i + 1;  # O(n)
    
    return -1; # O(1)

'''
Calculate Time Complexity :  O(1) + O(1) + O(n) + O(1) + O(n) + O(1)
                           = 4 * O(1) + 2 * O(n)
                           = O(n)

Calculate Space complexity : 
O(1) -> for n variable
O(1) -> for i variable
total space complexity : O(1) + O(1)
                       = 2 * O(1)
                       = O(1)

Time Complexity : O(n)
Space Complexity : O(1)
'''

def test_linear_search() : 
    test_cases = [
        {
            "name" : "simple case 0",
            "input" : [[3,5,6],5],
            "expected" : 1
        },
        {
            "name" : "simple case 1",
            "input" : [[3,5],3],
            "expected" : 0
        },
        {
            "name" : "simple case 2",
            "input" : [[3,5,8,7,5,1,6],1],
            "expected" : 5
        },
        {
            "name" : "simple case 3",
            "input" : [[2,5,6,2],1],
            "expected" : -1
        },
        {
            "name" : "simple case 4",
            "input" : [[],0],
            "expected" : -1
        }
    ]

    for case in test_cases :
        input_list = case['input'];
        assert case["expected"] == linear_search(input_list[0],input_list[1]), case['name']

if __name__ == "__main__" : 
    print('linear_search([3,5,6],5) : ',linear_search([3,5,6],5));
    print('linear_search([3,5],3) : ',linear_search([3,5],3));
    print('linear_search([3,5,8,7,5,1,6],1) : ',linear_search([3,5,8,7,5,1,6],1));
    print('linear_search([2,5,6,2],1) : ',linear_search([2,5,6,2],1));
    print('linear_search([],0) : ',linear_search([],0));
    