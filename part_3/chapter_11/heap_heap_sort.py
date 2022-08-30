from binarytree import build;

# create get_parent,get_left,get_right and swap function
get_parent = lambda _i : _i//2;
get_left = lambda _i : _i*2;
get_right = lambda _i : _i *2+1;
def swap(_list:list,_ai:int,_bi:int)->list:
    _list[_ai],_list[_bi] = _list[_bi],_list[_ai];
    return list;

# create max_heapify
def max_heapify(_heap:list,_heap_size:int=None,_root:int=1)->list:
    heap_size = _heap_size or len(_heap) - 1;
    rt = _root;
    left = get_left(rt);
    right = get_right(rt);

    # find largest value's index
    largest = rt;
    if left <= heap_size and _heap[left] > _heap[largest]:
        largest = left;
    
    if right <= heap_size and _heap[right] > _heap[largest]:
        largest = right;
    
    # if largest is rt
    if largest == rt :
        return _heap;

    # if largest is not rt
    swap(_heap,rt,largest); # swap value between largest and rt
    max_heapify(_heap,_heap_size,largest); # call it again for smallest value where placed

# build_max_heap
def build_max_heap(_heap:list)->list:
    size = len(_heap) - 1;

    for i in range(size//2,0,-1):
        max_heapify(_heap,size,i);

    return _heap;

# create heap heap sort
def heap_sort(_list:list)->list:
    size = len(_list) - 1;
    # build list to max_heap
    build_max_heap(_list);

    for i in range(size,1,-1):
        # swap with last index
        swap(_list,1,i);
        size -= 1;
        max_heapify(_list,size,1);

    return _list;

# create analysis_heap_sort for anlysis
def analysis_heap_sort(_list:list)->list:
    size = len(_list) - 1;
    # build list to max_heap
    build_max_heap(_list);

    for i in range(size,1,-1):
        # swap with last index
        swap(_list,1,i);
        size -= 1;
        max_heapify(_list,size,1);
        print("--------case--------");
        print(build(_list[1:size+1]));
        print(_list);
        print("---------------------\n")

    return _list;


if __name__ == "__main__":
    unorder_list = [None,3,2,4,6,2,10,2,3,4,5];
    print("pinrt unorder_list before sorting : ")
    print(unorder_list);
    heap_sort(unorder_list);
    print("print order list after sort : ");
    print(unorder_list);

    # analysis
    in_book_list = [None,12,7,1,3,10,17,19,2,5];
    print("\n\nprint the list before sorting :")
    print(in_book_list);
    print(build(in_book_list[1:]));
    print("The heap tree : ");
    build_max_heap(in_book_list);
    print(build(in_book_list[1:]));
    print(in_book_list);
    print("----> start to analysis <----");
    analysis_heap_sort(in_book_list);
    print("result : ",in_book_list);