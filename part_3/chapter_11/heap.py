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

if __name__ == '__main__' :
    heap = create_heap();

    print(">>> Heap <<<");
    print(build(heap[1:]));

    print('is_max_heap(heap) : ',is_max_heap(heap));