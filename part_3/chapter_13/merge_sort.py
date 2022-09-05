# merge function -> merge two sorted list
def merge(_list_one:list,_list_two:list)->list:
    len_one = len(_list_one);
    len_two = len(_list_two);
    index_one = 0;
    index_two = 0;

    # merge list
    merged_list = [];

    # start to merging
    while index_one < len_one and index_two < len_two:
        if _list_one[index_one] < _list_two[index_two]:
            merged_list.append(_list_one[index_one]);
            index_one += 1;
        else:
            merged_list.append(_list_two[index_two]);
            index_two += 1;

    if index_one < len_one:
        merged_list += _list_one[index_one:];

    if index_two < len_two:
        merged_list += _list_two[index_two:];

    return merged_list;

# merge sort
def merge_sort(_list:list)->list:
    if len(_list) <= 1:
        return _list;

    mid = len(_list)//2;
    left = merge_sort(_list[:mid]);
    right = merge_sort(_list[mid:]);
    return merge(left,right);

if __name__ == "__main__":
    test_cases = [
        {   
            'name' : "simple case 1",
            'input' : [4,7,2,3],
            'output' : [2,3,4,7]
        },
        {
            'name' : 'simple case 2',
            'input' : [10],
            'output' : [10]
        },
        {
            'name' : 'simple case 3',
            'input' : [10,9,8,7,6],
            'output' : [6,7,8,9,10]
        },
        {
            'name' : 'simple case 4',
            'input' : [2,3,1],
            'output' : [1,2,3]
        },
        {
            'name' : 'simple case 5',
            'input' : [1,2],
            'output' : [1,2]
        },
        {
            'name' : "simple case 6",
            'input' : [2,1],
            'output' : [1,2]
        }
    ]

    for case in test_cases:
        print("---------->",case['name'],'<----------');
        print("input : ",case['input']);
        result = merge_sort(case['input']);
        print("output : ",result);
        print("Expected : ",case['output']);

        if result == case['output'] : 
            print("status : Passed");
            print("------------------------------------");
        else : 
            print("status : Failed");
            assert False and "test name is : "+case['name'];

    print("\n\n>>>\n>>\n> All Test Case is Passed. Go do Other Work :)");