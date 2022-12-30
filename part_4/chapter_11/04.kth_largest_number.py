from typing import List
import heapq

def kth_largest(li:List[int],k:int)->int:
    heap_list = []; # create for heap list 

    for i in li:
        heapq.heappush(heap_list,i*-1);

    largest = heapq.heappop(heap_list);
    k -= 1;
    while k : 
        largest = heapq.heappop(heap_list);
        k-= 1;
    
    return -largest;

if __name__ == "__main__":
    test_case = [
        {
            'number' : 0,
            'input' : [[3,4,5,6,2,1,3,4],3],
            'expected' : 4
        },
        {
            'number' : 1,
            'input' : [[-2,3,45,3,21],4],
            'expected' : 3,
        },
        {
            'number' : 2,
            'input' : [[-45,43,2,1,3,4,23,4],1],
            'expected' : 43
        },
        {
            'number' : 2,
            'input' : [[3,4,5,11,2,4],5],
            'expected' : 3
        }
    ]

    for case in test_case:
        output = kth_largest(case['input'][0],case['input'][1]);

        print(f">>>> Case No {case['number']}");
        print(f"> input    : {case['input']}");
        print(f"> expected : {case['expected']}");
        print(f"> output   : {output}\n");