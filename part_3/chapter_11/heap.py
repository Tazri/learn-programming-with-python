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
def create_heap_list()->list: return [None,12,7,1,3,10,17,19,2,5];

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
def max_heapify(_heap:list,_root_index:int=0)-> list :
    last_index = len(_heap) - 1;
    li = get_left(_root_index); # left index
    ri = get_right(_root_index); # right index.

    # if traverse the last
    if _root_index >= (last_index // 2)+1:
        return _heap;
    
    # greater index
    gi = None;
    if ri > last_index and li <= last_index :
        gi = li;
    elif ri <= last_index and li > last_index:
        gi = ri;
    elif ri <= last_index and li <= last_index :
        if _heap[ri] > _heap[li] :
            gi = ri;
        else:
            gi = li;

    # if _heap[gi] > _heap[_root_index]
    if gi != None and (_heap[gi] > _heap[_root_index]):
        swap(_heap,gi,_root_index);
        rpi = get_parent(_root_index) or 1; # root_parent_index
        max_heapify(_heap,rpi);

    # call max heapify for other
    max_heapify(_heap,_root_index+1);

# min_heapify
def min_heapify(_heap:list,_root_index:int=0)-> list:
    last_index = len(_heap) - 1;
    li = get_left(_root_index); # root index
    ri = get_right(_root_index); # right index

    if _root_index >= (last_index//2) + 1:
        return _heap;

    # smaller node
    si = None; # smaller_index
    if ri > last_index and li <= last_index:
        si = li;
    elif ri <= last_index and li > last_index:
        si = ri;
    elif ri <= last_index and li <= last_index:
        if _heap[ri] > _heap[li] :
            si = li;
        else:
            si = ri;

    # swap root with si if _heap[si] < _heap[_root_index]
    if si != None and (_heap[si] < _heap[_root_index]):
        swap(_heap,si,_root_index);
        rpi = get_parent(_root_index) or 1; # root_parent_index
        min_heapify(_heap,rpi); # call min heapify for parent
    
    # call min heapify for other
    min_heapify(_heap,_root_index+1);

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
    max_heapify(heap_two,1);
    print(build(heap_two[1:]));
    heap_details(heap_two);

    print("\n>>> After Min Heapify heap two <<<");
    min_heapify(heap_two,1);
    print(build(heap_two[1:]));
    heap_details(heap_two);