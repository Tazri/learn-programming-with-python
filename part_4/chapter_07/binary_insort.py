def binary_find_index(li:list,x:int,low:int=0,high=None)->int:
    # if item is 0
    if high == None :
        high = len(li) - 1;

    start_high = high;

    items = high - low + 1; # calculate how many item
    
    # if list was 0
    if items == 0 : return low;
    
    # list contain only one item
    if items == 1 :
        if li[low] > x : return low;
        else : return low+1;


    # otherwise
    middle = (low+high) // 2;
    mid = None;

    while low < high :
        mid = (low+high)//2;
        if li[mid] == x : 
            return mid ;
        elif li[mid] < x : 
            low = mid + 1;
        elif li[mid] > x:
            high = high - 1;


    if mid < middle : 
        return 0;
    elif mid > middle : 
        return start_high + 1;
    elif high == low : 
        return high;

def insort_binary(li:list,x:int,low:int=0,high:int=None)->list:
    # if high None
    if high == None : high = len(li) - 1;

    target_index = binary_find_index(li,x);

    # if target index is outof the list
    if target_index >= len(li) :
        li.append(x); # inject x into the li
        return li;

    # otherwise
    li.append(x); # inject x into the li
    for i in range(len(li)-2,target_index-1,-1):
        li[i+1] = li[i];
        
    li[target_index] = x;
    return li;

if __name__ == "__main__":
    li = [1,2,4,7,8];
    print("li : ",li);

    print("after insort(li,3) :");
    insort_binary(li,3);
    print(li);

    print("after insort(li,10) :");
    insort_binary(li,10);
    print(li);

    print("after insort(li,15) :");
    insort_binary(li,15);
    print(li);

    print("after insort(li,2) :");
    insort_binary(li,2);
    print(li);

    print("after insort(li,-1) :");
    insort_binary(li,-1);
    print(li);