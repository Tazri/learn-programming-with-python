class Queue:
    # constructur
    def __init__(self) :
        self.queue = [];

    # is_empty -> check queue is empty of not
    def is_empty(self) :
        if len(self.queue) :
            return False ;
        
        return True 

    # dequeue -> remove first element from list
    def dequeue(self) :
        if self.is_empty() :
            return None;
        
        return self.queue.pop(0);

    # enqueue -> add element from list at last
    def enqueue(self,item) :
        self.queue.append(item);


# using queue data structure
if __name__ == '__main__' : 
    line = Queue();

    line.enqueue('Eren');
    line.enqueue('Erwin');
    line.enqueue('levi');
    line.enqueue("Reiner");

    while not line.is_empty() : 
        print(line.dequeue()+" is ok done.");