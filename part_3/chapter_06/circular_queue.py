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
        return (self.tail+1)%self.maxsize == self.head;

    # length -> return length of queue
    def length(self) :
        if self.is_empty():
            return 0;
        elif self.head == self.tail :
            return 1
        elif self.head < self.tail :
            return self.tail - self.head + 1
        else : 
            return (self.maxsize - self.head + self.tail + 1)


    # enqueue -> add element in queue at last position
    def enqueue(self,item) :
        # check is full or not 
        if self.is_full() :
            print(">> Queue is fulled! <<");
            return None;
        
        # if is first element of queue
        if self.is_empty() :
            self.head = 0;
        

        # increase the tail and add item
        self.tail = (self.tail+1) % self.maxsize;
        self.queue[self.tail] = item;

    # dequeue -> remove element from first position of queue
    def dequeue(self) :
        # check is queue empty or not
        if self.is_empty() :
            print(">> Queue is empty! <<");
            return None;
        
        # if it was last element
        if self.head == self.tail :
            temp = self.queue[self.head];
            self.head = -1;
            self.tail = -1;
            return temp;

        # if it was not last element
        temp = self.queue[self.head];
        self.head = (self.head + 1) % self.maxsize;

        return temp;
    
    # print queue
    def __repr__(self):
        # if queue is empty
        if self.is_empty():
            return '[ Queue is Empty!!! ]';

        queue = 'Queue [ ';
        head,tail = self.head,self.tail;

        while head != tail : 
            queue += str(self.queue[head]) + ",";
            head = (head+1) % self.maxsize;

        queue += (self.queue[head]) + " ]";
        
        return queue;


# using circular queue
if __name__ == '__main__' : 
    line = Circular_Queue(5);

    line.enqueue("md tazri");
    line.enqueue("alyath");
    line.enqueue("farabi");
    line.enqueue("arabi");

    print(line);
    print(line.length())

    person = line.dequeue();
    print(person);
    print(line);
    print(line.length())

    line.enqueue("tazri");
    print(line);
    print(line.length())
    print(line.dequeue());
    print(line.dequeue());
    print(line);
    print(line.length())

    line.enqueue("analyzer");
    line.enqueue("driner");
    print(line);
    print(line.length());

    line.enqueue("atra");
    print(line);
    print(line.length());

    line.enqueue("serius");

    print(line);
    print(line.length());


    while not line.is_empty() :
        print("Hello",line.dequeue());

    print(line);
    print(line.length());
