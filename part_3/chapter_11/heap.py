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

# swap list value
def swap(_list,_ai,_bi)-> list :
    temp = _list[_ai];
    _list[_ai] = _list[_bi];
    _list[_bi] = temp;
    return _list;

# max_heapify
def max_heapify(_heap,_root)-> list :
    last_index = len(_heap) - 1;
    li = get_left(_root); # left index
    ri = get_right(_root);
    l = _heap[li]; # left
    r = _heap[ri]; # right
    rt = _heap[_root]; # root 

    # if root, left or right is equal or greater than last index
    if li >= last_index or ri >= last_index or _root >= last_index :
        return _heap;

    # if is _root less than left or right
    if rt < l or rt < r :
        if l > r : # swaping
            swap(_heap,li,_root);
            max_heapify(_heap,li);
        else :
            swap(_heap,ri,_root);
            max_heapify(_heap,ri);
    
    max_heapify(_heap,_root+1);

if __name__ == '__main__' :
    heap = create_heap();

    print(">>> Heap <<<");
    print(build(heap[1:]));

    print('is_max_heap(heap) : ',is_max_heap(heap));

    # before using max_hapify
    heap_two = create_heap_list();
    print("\n\n>>> Before Max Heapifpy heap two <<<");
    print(build(heap_two[1:]));
    print("is_max_heap(heap_two) : ",is_max_heap(heap_two));

    # after using max_hapify
    print("\n>>> After Max Heapifoy heap two <<<");
    max_heapify(heap_two,1);
    print(build(heap_two[1:]));
    print("is_max_heap(heap_two) : ",is_max_heap(heap_two));
    