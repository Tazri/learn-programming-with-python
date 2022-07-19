def selection_sort(list) : 
    n = len(list); # get length

    for i in range(0,n) :
        min_index = i;

        for j in range(i+1,n) : 
            if list[min_index] > list[j] :
                min_index = j;

        if min_index != i : 
            # swap the value between list[min_index] and list[i]
            list[min_index],list[i] = list[i],list[min_index];
    
    return list;

'''
Calculate time complexity : here in loop
when i = 0,   run the inside the loop j = 1 to (n-1)   total (n-1)
when i = 1,   run the inside the loop j = 2 to (n-1)   total (n-2)
when i = 2,   run the inside the loop j = 3 to (n-1)   total (n-3)
------------------------------------------------------------------
------------------------------------------------------------------
when i = n-4, run the inside the loop j = n-3 to (n-1) total 3
when i = n-3, run the inside the loop j = n-2 to (n-1) total 2
when i = n-2, run the inside the loop j = n-1 to (n-1) total 1

total loop run = (n-1) + (n-2) + (n-3) + ......................... + 3 + 2 + 1
               = 1 + 2 + 3 + ..................................... + (n-3) + (n-2) + (n-1)
               = [{(n-1)+1}*(n-1)]/2
               = n*(n-1)/2
               = (n^2-n)/2
               = (n^2)/2 - n/2

total time complexity : O(n^2/2) - O(n/2)
                      : O(n^2)

Calculate space complexity : 
O(1) -> for n variable
O(1) -> for min_index variable
O(1) -> for i variable
O(1) -> for j variable

total space complexity : O(1) + O(1) + O(1) + O(1)
                       : 4 * O(1)
                       : O(1)

time complexity : O(n^2)
space complexity : O(1)
'''

def test_selection_sort() : 
    test_case = [
        {
            'name' : "simple case 0",
            'input' :    [4,3,6,7,5,2,1],
            'expected' : [1,2,3,4,5,6,7]
        },
        {
            'name' : 'simple case 1',
            'input' :    [43,554,34,32,1,3],
            'expected' : [1,3,32,34,43,554]
        },
        {
            'name' : 'simple case 2',
            'input' :    [4,5,8,2,2,9,2],
            'expected' : [2,2,2,4,5,8,9]
        },
        {
            'name' : 'simple case 3',
            'input' :    [4],
            'expected' : [4]
        },
        {
            'name' : 'simple case 4',
            'input' :   [],
            'expected': []
        },
        {
            'name' : 'simple case 5',
            'input' :    [1,2,3,4,5,6,7,8],
            'expected' : [1,2,3,4,5,6,7,8]
        }
    ]

    for case in test_case : 
        assert case['expected'] == selection_sort(case['input']), case['name']

if __name__ == '__main__' : 
    print("selection_sort([4,3,6,7,5,2,1]) : ",selection_sort([4,3,6,7,5,2,1]));
    print("selection_sort([43,554,34,32,1,3]) : ",selection_sort([43,554,34,32,1,3]));
    print("selection_sort([4,5,8,2,2,9,2]) : ",selection_sort([4,5,8,2,2,9,2]));
    print("selection_sort([4]) : ",selection_sort([4]));
    print("selection_sort([]) : ",selection_sort([]));
    print("selection_sort([1,2,3,4,5,6,7,8]) : ",selection_sort([1,2,3,4,5,6,7,8]));
    