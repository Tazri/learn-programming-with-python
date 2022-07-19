def insertion_sort(list) :
    n = len(list);

    if (n == 0) or (n == 1) :
        return list 

    for i in range(1,n):
        item = list[i];
        j = i - 1;

        while j >= 0 :
            if list[j] > item :
                list[j+1] = list[j]
            else : 
                break

            j = j - 1;

        list[j+1] = item;

    return list 

'''
Calculate time complexity of insertion sort : 
Here inside loop run 
i = 1 ,     the loop run 0 to j = 0   total 1
i = 2 ,     the loop run 0 to j = 1   total 2
i = 3 ,     the loop run 0 to j = 2   total 3
-------------------------------------------------
-------------------------------------------------
i = n - 3,  the loop run 0 to j = n-2 total n - 3
i = n - 2,  the loop run 0 to j = n-1 total n - 2
i = n - 1,  the loop run 0 to j = n   total n - 1

total loop run : 
= 1 + 2 + 3 + ............ + (n-3) + (n-2) + (n-1) 
= [{(n-1)+1}*(n-1)]/2
= {n*(n-1)}/2
= (n^2-n)/2
= n^2/2 - n/2
total time complexity : O(n^2/2) - O(n/2)
                      : O(n^2/2)
                      : O(n^2)

Calculate space complexity of insertion sort :
O(1) -> for n variable
O(1) -> for item variable
O(1) -> for i variable
O(1) -> for j variable

total space complexity : O(1) + O(1) + O(1) + O(1)
                       : 4 * O(1)
                       : O(1)


time complexity : O(n^2)
space complexity: O(1)
'''

def test_insertion_sort() : 
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
        assert case['expected'] == insertion_sort(case['input']), case['name']



if __name__ == '__main__' : 
    print("insertion_sort([4,3,6,7,5,2,1]) : ",insertion_sort([4,3,6,7,5,2,1]));
    print("insertion_sort([43,554,34,32,1,3]) : ",insertion_sort([43,554,34,32,1,3]));
    print("insertion_sort([4,5,8,2,2,9,2]) : ",insertion_sort([4,5,8,2,2,9,2]));
    print("insertion_sort([4]) : ",insertion_sort([4]));
    print("insertion_sort([]) : ",insertion_sort([]));
    print("insertion_sort([1,2,3,4,5,6,7,8]) : ",insertion_sort([1,2,3,4,5,6,7,8]));