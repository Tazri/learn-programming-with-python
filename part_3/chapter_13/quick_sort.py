# swap -> swap two list element by their index
def swap(l:list,ai:int,bi:int)->list:
    l[ai],l[bi] = l[bi],l[ai];
    return l;

# partition
def partition(l:list,low:int=0,high:int=None):
    if high == None : high = len(l) - 1;
    index = low - 1;
    pivot = l[high];

    # place the pivot correct place
    for i in range(low,high):
        if l[i] <= pivot :
            swap(l,index+1,i);
            index += 1;
    
    swap(l,index+1,high);
    return index+1; # return index of pivot

# quick sort
def quick_sort(l:list,low:int=0,high:int=None):
    if high == None :
        high = len(l) -1;
    
    if low >= high : 
        return l;

    # partition whole array first
    pivot_index = partition(l,low,high);
    quick_sort(l,low,pivot_index-1);
    quick_sort(l,pivot_index+1,high);

    return l;

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
        result = quick_sort(case['input']);
        print("output : ",result);
        print("Expected : ",case['output']);

        if result == case['output'] : 
            print("status : Passed");
            print("------------------------------------");
        else : 
            print("status : Failed");
            assert False and "test name is : "+case['name'];

    print("\n\n>>>\n>>\n> All Test Case is Passed. Go do Other Work :)");