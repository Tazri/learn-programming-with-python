from binarytree import build;

# create array for heap
def create_heap()->list:
    '''
            ___19___
           /        \
        _7_        _17_
       /   \      /    \
      3     5    12    10
     / \
    1   2
    '''

    root = 1;
    heap = [None]*10;

    # adding item in heap
    heap[root] = 19;
    heap[get_left(root)] = 7;
    heap[get_right(root)] = 17;
    
    # secound level
    heap[get_left(2)] = 3;
    heap[get_right(2)] = 5;
    heap[get_left(3)] = 12;
    heap[get_right(3)] = 10;

    # third level
    heap[get_left(4)] = 1;
    heap[get_right(4)] = 2; 
    

    return heap;

# create another heap list
def create_heap_list()->list: return [None,7,12,1,3,10,17,19,2,5];

# left child
def get_left(_i:int)-> int : return _i *2;

# right child
def get_right(_i:int)-> int : return (_i * 2) + 1;

# parent
def get_parent(_i)-> int : return _i // 2;

# is_max_heap
def is_max_heap(_heap):
    n = len(_heap) - 1;

    for i in range(n,1,-1):
        # check parent is less than child ??
        if _heap[get_parent(i)] < _heap[i] :
            return False;
    
    return True;

# is_min_heap
def is_min_heap(_heap):
    n = len(_heap) - 1;

    for i in range(n,1,-1):
        if _heap[get_parent(i)] > _heap[i] :
            return False;
    
    return True;

# swap list value
def swap(_list:list,_ai:int,_bi:int)-> list :
    temp = _list[_ai];
    _list[_ai] = _list[_bi];
    _list[_bi] = temp;
    return _list;

# max_heapify
def max_heapify(_heap:list,_heap_size:int=None,_root:int=1)->list:
    heap_size =_heap_size or len(_heap)-1;
    left = get_left(_root);
    right = get_right(_root);

    # find largest value index between left, right and _root;
    if left <=heap_size and _heap[left] > _heap[_root]:
        largest = left;
    else:
        largest = _root;

    if right <= heap_size and _heap[right] > _heap[largest]:
        largest = right;
    
    # root is largest
    if largest == _root :
        return _heap;
    
    # if not root i largest
    swap(_heap,largest,_root); # swap first;
    max_heapify(_heap,_heap_size,largest);


# max_build
def max_heap_build(_list:list)->list:
    size = len(_list)-1;

    for i in range(size//2,0,-1):
        max_heapify(_list,size,i);

    return _list;

# min_heapify
def min_heapify(_heap:list,_heap_size:int=None,_root:int=1)->list:
    heap_size = _heap_size or len(_heap_size) - 1;
    left = get_left(_root);
    right = get_right(_root);

    # find smallest value index between left, right and _root
    if left <= heap_size and _heap[left] < _heap[_root]:
        smallest = left;
    else:
        smallest = _root;
    
    if right <= heap_size and _heap[right] < _heap[smallest]:
        smallest = right;
    
    # if smallest is _root then finish it
    if smallest == _root:
        return _heap;
    
    # swap root with smallest
    swap(_heap,smallest,_root);
    min_heapify(_heap,_heap_size,smallest);

# min_heap_build
def min_heap_build(_list:list)->list:
    size = len(_list) - 1;

    for i in range(size//2,0,-1):
        min_heapify(_list,size,i);

    return _list;

# status heap details
def heap_details(_heap):
    print("is_max_heap(heap) : ",is_max_heap(_heap));
    print("is_min_heap(heap) : ",is_min_heap(_heap));

if __name__ == '__main__' :
    heap = create_heap();

    print(">>> Heap <<<");
    print(build(heap[1:]));

    print('is_max_heap(heap) : ',is_max_heap(heap));

    # before using max_hapify
    heap_two = create_heap_list();
    print("\n\n>>> Before Max Heapifpy heap two <<<");
    print(build(heap_two[1:]));
    heap_details(heap_two);

    # after using max_hapify
    print("\n>>> After Max Heapify heap two <<<");
    max_heap_build(heap_two);
    print(build(heap_two[1:]));
    heap_details(heap_two);

    print("\n>>> After Min Heapify heap two <<<");
    min_heap_build(heap_two);
    print(build(heap_two[1:]));
    heap_details(heap_two);