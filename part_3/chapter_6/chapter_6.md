Chapter 6 : Stack and Queue
===========================

## Stack 

Stack is simple linear data structure which follows a particular order in which the operations are performed. The order may be LIFO (Last In First Out) or FILO(First in Last Out). Here stack all feature : 

1. stack has **push** method to append value in the last in data stack.
1. stack has **pop** method to remove last value in data stack.
1. **is_empty** to check is stack full or not. 


**Implement the Stack :**
```python
class Stack :
    # constructor 
    def __init__(self) :
        self.stack = [];

    # is_empty method
    def is_empty(self) :
        if len(self.stack) :
            return False;
        else : 
            return True;

    # push method
    def push(self,item) :
        self.stack.append(item);

    # pop method 
    def pop(self) : 
        if self.is_empty() :
            return None 
        else : 
            return self.stack.pop();

```

**Using the Stack :**
```python
if __name__ == "__main__" : 
    books = Stack();
    books.push("Nimikh Pane");
    books.push("Programminger Adonpanto");
    books.push("message");
    books.push("python die programming shikha");

    while not books.is_empty() : 
        print("Books name : ",books.pop());
```

```bash
$python3 stack.py 
Books name :  python die programming shikha
Books name :  message
Books name :  Programminger Adonpanto
Books name :  Nimikh Pane
```

Here all problem about stack structure : 
1. [First Bracket is Balanced.](./problems/balanced_first_bracket.py)
1. [Brackets are Balanaced](./problems/balance_multiple_bracket.py)
1. [Fun Game](./problems/fun_game.py)

<hr />
<br />

Queue 
=====
Queue is a linear data structure which follows a particular order in which operations are performed. The order is **First in First Out (FIFO)**. Here all Queue method :

1. **enqueue** method to remove first element from queue.
1. **dequeue** method to remove last element from queue.
1. **is_empty** method to check is queue is empty or not. 


**Implement Queue :**
```python
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

```

**Using Queue :**
```python
# using queue data structure
if __name__ == '__main__' : 
    line = Queue();

    line.enqueue('Eren');
    line.enqueue('Erwin');
    line.enqueue('levi');
    line.enqueue("Reiner");

    while not line.is_empty() : 
        print(line.dequeue()+" is ok done.");
```

```bash
$python3 queue.py 
Eren is ok done.
Erwin is ok done.
levi is ok done.
Reiner is ok done.
```

**Here all problem about queue data structure :**

1. [Fun Game](./problems/fun_game.py)
1. [stack and queue](./problems/stack_and_queue.py)

<hr />
<br />

## Circular Queue 
A **Circular Queue** is the extended version of a **regular queue** where last element is connected to first element. Thus forming a circle-like structure. Circular queue work as follows :

1. two pointers **head or front** and **tail or rear**.
1. **head** track first element and **tail** track last element.
1. initially, set value of **head** and **tail** is -1

**Circular Queue Operations :**

1. Enqueue Operations
    1. check is queue full 
    1. for the first element, set head = 0
    1. increase the tail index by 1
    1. add element at index head
2. Dequeue Operations 
    1. check is queue is empty
    1. return value pointed by head
    1. increase the head index by 1
    1. for the last element, reset the head and tail to 0

**Implement Circular Queue :**
```python
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
```

**Using Circular Queue :**
```python
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
```

```bash
$python3 circular_queue.py 
Queue [ md tazri,alyath,farabi,arabi ]
4
md tazri
Queue [ alyath,farabi,arabi ]
3
Queue [ alyath,farabi,arabi,tazri ]
4
alyath
farabi
Queue [ arabi,tazri ]
2
Queue [ arabi,tazri,analyzer,driner ]
4
Queue [ arabi,tazri,analyzer,driner,atra ]
5
>> Queue is fulled! <<
Queue [ arabi,tazri,analyzer,driner,atra ]
5
Hello arabi
Hello tazri
Hello analyzer
Hello driner
Hello atra
[ Queue is Empty!!! ]
0
```

**Here all problem sove with circular queue :**

1. [stack and queue](./problems/stack_and_queue.py)

<hr />
<br />

[< Go Back](./../part_3.md)