def bubble_sort(list) :
    n = len(list);

    for i in range(n) :
        for j in range(n-1-i) :
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

    return list 


'''
Calculate time complexity : 
Here inside the loop run, 
when i = 0,      inside loop run j = 0 to (n-1) total n - 1
when i = 1,      inside loop run j = 0 to (n-2) total n - 2
when i = 2,      inside loop run j = 0 to (n-3) total n - 3
when i = 3,      inside loop run j = 0 to (n-4) total n - 4
------------------------------------------------------------
------------------------------------------------------------
when i = n - 3,  inside loop run j = 0 to 2     total 2
when i = n - 2,  inside loop run j = 0 to 1     total 1
when i = n - 1,  inside loop run j = 0 to 0     total 0

total time complexity : 
    1 + 2 + 3 + ..... + (n-4) + (n-3) + (n-2) + (n-1)
  = [{(n-1)+1}(n-1)] / 2
  = {n(n-1)}/2
  = (n^2-n)/2
  = n^2/2 - n/2
  = O(n^2) - O(n/2)
  = O(n^2)


Calculate space complexity : 
O(1) -> for i variable
O(1) -> for j variable
O(1) -> for n variable

total space complexity is : O(1) + O(1) + O(1)
                          = 3 * O(1)
                          = O(1)

time complexity : O(n^2) 
space compexity : O(1)  
'''


def test_bubble_sort() : 
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
        assert case['expected'] == bubble_sort(case['input']), case['name']





if __name__ == '__main__' : 
    print("bubble_sort([4,3,6,7,5,2,1]) : ",bubble_sort([4,3,6,7,5,2,1]));
    print("bubble_sort([43,554,34,32,1,3]) : ",bubble_sort([43,554,34,32,1,3]));
    print("bubble_sort([4,5,8,2,2,9,2]) : ",bubble_sort([4,5,8,2,2,9,2]));
    print("bubble_sort([4]) : ",bubble_sort([4]));
    print("bubble_sort([]) : ",bubble_sort([]));
    print("bubble_sort([1,2,3,4,5,6,7,8]) : ",bubble_sort([1,2,3,4,5,6,7,8]));