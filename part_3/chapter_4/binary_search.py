def binary_search(list,x) :
    left = 0; # O(1)
    right = len(list) - 1; # O(1)

    while left <= right : # O(log n)
        mid = (left + right) // 2; # O(log n)

        if list[mid] == x : # O(log n)
            return mid; # O(log n)
        elif list[mid] < x : # O(log n)
            left = mid + 1; # O(log n)
        else : # O(log n)
            right = mid - 1; # O(log n)

    return -1 # O(1)

'''
calculate time complexity : O(1) + O(1) + 7 * O(log n) + O(1)
                          = 3 * O(1) + 7 * O(log n)
                          = O(log n)

calculate space complexity : 
O(1) -> for left variable
O(1) -> for right variable
O(1) -> for mid variable
total space complexity : 3 * O(1)
                       = O(1)

time complexity : O(log n)
space complexity : O(1)

'''


def test_binary_search() :
    # run pytest binary_search.py

    test_case = [
        {
            'name' : 'simple case 0',
            'input' : [[2,4,5,7,8,9,12,17,21],12],
            'expected' : 6
        },
        {
            'name' : 'simple case 1',
            'input' : [[1,2,3,4,5],4],
            'expected' : 3
        },
        {
            'name' : 'simple case 2',
            'input' : [[33,36,41,52],45],
            'expected' : -1
        },
        {
            'name' : 'simple case 3',
            'input' : [[15,18,19,21,22],21],
            'expected' : 3
        },
        {
            'name' : 'simple case 4',
            'input' : [[11,15,21,23,24,26,27],26],
            'expected' : 5
        },
        {
            'name' : 'simple case 5',
            'input' : [[23,34,37,38],35],
            'expected' : -1
        }
    ]


    for case in test_case :
        test_name = case['name'];
        input_list = case['input'];

        assert case['expected'] == binary_search(input_list[0],input_list[1]), test_name



if __name__ == '__main__' : 
    print("binary_search([11,15,21,23,24,26,27],26) : ",binary_search([11,15,21,23,24,26,27],26));
    print("binary_search([15,18,19,21,22],21) : ",binary_search([15,18,19,21,22],21));
    print("binary_search([23,34,37,38],35) : ",binary_search([23,34,37,38],35));

