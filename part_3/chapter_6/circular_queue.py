from sys import maxsize


class Circular_Queue:
    # constructor
    def __init__(self,size,deli = 0) :
        self.queue = [deli]*size;
        self.maxsize, self.head,self.tail = size,-1,-1

    # is_empty -> check queue is empty or not
    def is_empty(self):
        if self.head == -1 :
            return True;
        return False;
    
    # is_full -> check queue is full or not
    def is_full(self):
        return self.tail+1 == maxsize;

    # length -> return length of queue
    def length(self) :
        return len(self.queue);

    # enqueue -> add element in queue at last position
    def enqueue(self,item) :
        if self.is_empty() :
            head = 0;
        
        # check is full or not 
        if self.is_full() :
            print(">> Queue is fulled! <<");
            return None;

        # increase the tail and add item
        tail = (tail+1) % self.maxsize;
        self.queue[tail] = item;

    # dequeue -> remove element from first position of queue
    def dequeue(self) :
        # check is queue empty or not
        if self.is_empty() :
            print(">> Queue is empty! <<");
            return None;
        
        # remove head element
        self.queue