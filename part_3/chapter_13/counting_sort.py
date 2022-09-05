# counting_sort
def counting_sort(l:list,high:int):
    counting_list = [0]*(high + 1);
    sorted_list = [];

    # counting start 
    for i in l : 
        counting_list[i] += 1;
    
    # create sorted list based on counting list
    for i in range(high+1):
        if counting_list[i]: 
            for j in range(counting_list[i]):
                sorted_list.append(i);
    
    return sorted_list;

if __name__ == "__main__" : 
    test_cases = [
        {   
            'name' : "simple case 1",
            'input' : [[4,7,2,3],7],
            'output' : [2,3,4,7]
        },
        {
            'name' : 'simple case 2',
            'input' : [[10],10],
            'output' : [10]
        },
        {
            'name' : 'simple case 3',
            'input' : [[10,9,8,7,6],10],
            'output' : [6,7,8,9,10]
        },
        {
            'name' : 'simple case 4',
            'input' : [[2,3,1],3],
            'output' : [1,2,3]
        },
        {
            'name' : 'simple case 5',
            'input' : [[1,2],2],
            'output' : [1,2]
        },
        {
            'name' : "simple case 6",
            'input' : [[2,1],2],
            'output' : [1,2]
        },
        {
            'name' : "simple case 7",
            'input' : [[3,4,1,6,2,4,9,7,8,4,2,1],10],
            'output' : [1,1,2,2,3,4,4,4,6,7,8,9]
        }
    ]

    for case in test_cases:
        print("----------->",case['name'],'<------------');
        print("> input :",case['input']);
        result = counting_sort(case['input'][0],case['input'][1]);
        print("> output :",result);
        print("> expected : ",case['output']);

        if result == case['output']:
            print("> status : passed");
            print("----------------------------------------\n\n");
        else:
            print("> status : Failed");
            assert False and "Failed Test Name : " + case['name'];

    print(">>>>\n>>>\n>> SUCCESSFULLY PASSED\n> GO TO DO OTHER WORK :) ");