from binarytree import build;

class Priority_Queue:
    pass;

class Priority_Queue: 
    # constructor
    def __init__(self,_list:list=None)-> None:
        if list == None:
            self.heap = [None];
        else :
            self.heap = [None] + _list;

            # build max heap
            self.build_max();
    
    # get maximum value
    def get_maximum(self)->int: return self.heap[1];

    # get_left_index
    def get_left_index(self,i:int)->int: return i*2;
    
    # get_left
    def get_left(self,i:int)->int : return self.heap[i*2]

    # get_right_index
    def get_right_index(self,i:int)->int : return i*2 + 1;

    # get_right 
    def get_right(self,i:int)-> int : return self.heap[i*2 + 1];

    # get_parent_index
    def get_parent_index(self,i:int)->int : return i//2;

    # get_parent
    def get_parent(self,i:int)->int: return self.heap[i//2];

    # get_value
    def get_value(self,i:int)->int : return self.heap[i];

    # swap
    def swap(self,ai:int,bi:int)->Priority_Queue:
        self.heap[ai],self.heap[bi] = self.heap[bi],self.heap[ai];
        return self;

    # max_heapify
    def max_heapify(self,heap:list,size:int=None,root_index:int=1)->Priority_Queue:
        size = size or len(heap) - 1;
        left_index = self.get_left_index(root_index);
        right_index = self.get_right_index(root_index);

        # find largest index
        largest = root_index;
        if left_index <= size and self.get_left(root_index) > self.get_value(root_index):
            largest = left_index;
        if right_index <= size and self.get_right(root_index) > self.get_value(largest):
            largest = right_index;

        # if largest value is root_index
        if largest == root_index : return self;

        # if largest is not root_index
        self.swap(largest,root_index); # swap value between largest and root_index
        self.max_heapify(self.heap,size,largest); # 

        # find 
        return self;

    # build_max
    def build_max(self)->list:
        size = len(self.heap) - 1;

        for i in range(size//2,0,-1):
            self.max_heapify(self.heap,size,i);

        return self.heap;

    # __repr__
    def __repr__(self) -> str:
        return str(self.heap);

    # show_tree
    def show_tree(self)->None:
        print(build(self.heap[1:]));

    # extract_max
    def extract_max(self)->int:
        if len(self.heap) <= 1 :
            print("-> Heap is totally empty :(");
            return 0;

        # replace the first with last
        popped = self.heap.pop();
        first = self.heap[1];

        self.heap[1] = popped;
        self.max_heapify(self.heap); # other is by default None and 1

        return first;

    # insert_node
    def insert_node(self,n:int)->Priority_Queue:
        self.heap.append(n);
        n_index = len(self.heap) - 1

        # bubble up for n right place
        while n_index > 1:
            parent = self.get_parent_index(n_index);

            if self.get_value(n_index) > self.get_parent(n_index):
                self.swap(n_index,parent);
                n_index = parent;
                continue;
            
            break;

        return self;

    # increase_key
    def change_key(self,i:int,new_value:int)->Priority_Queue:
        # first change the value from heap
        self.heap[i] = new_value;

        # if it bigger then parent
        if self.get_parent(i) != None and self.get_parent(i) < new_value:
            n_index = i;
            while n_index > 1:
                parent = self.get_parent_index(n_index);

                if self.get_value(n_index) > self.get_parent(n_index):
                    self.swap(n_index,parent);
                    n_index = parent;
                    continue;
                
                break;
            
            return self;
        
        # if by change child is small
        self.max_heapify(self.heap,len(self.heap)-1,i);

        return self;

if __name__ == "__main__":
    queue = Priority_Queue([12,7,1,3,10,17,19,2,5]);

    print("--> cheking is queue work perfectly <--");
    print(queue);
    print('queue.show_tree()');
    queue.show_tree();
    print("queue.get_maximum() : ",queue.get_maximum());

    print("extract first item");
    print("queue.extract_max() : ",queue.extract_max());
    print(queue);
    queue.show_tree();

    print("\nqueue.insert_node(19).show_tree() : ");
    queue.insert_node(19).show_tree();
    print(queue);

    print("\n-> queue.change_key(5,21).show_tree() <-");
    queue.change_key(5,21).show_tree();
    print(queue);

    print("\n-> quue.change_key(1,7).show_tree() <-");
    queue.change_key(1,7).show_tree();
    print(queue);