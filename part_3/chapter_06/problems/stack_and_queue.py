'''
problem in details link : 
https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/staque-1-e790a29f/
'''

class Line :
    # constructor :
    def __init__(self,_list,_size,_removing) :
        self.list = _list;
        self.size = _size;
        self.remove = _removing;
        self.head = 0;
        self.tail = _size - 1;
        self.biggest_sum = None;
        self.current_sum = None;
    
    # pop -> pop the item from stack 
    def pop(self):
        temp = self.list[self.head];
        self.head += 1;
        return temp;

    # pop_back -> back pop
    def pop_back(self):
        if self.head == 0:
            return self.list[self.head];

        self.head -= 1;
        return self.list[self.head];

    # initial_sum -> initialize the biggest sum by performing remove times pop
    def initial_sum(self):
        sum = 0;

        for i in range(self.remove):
            sum += self.pop();
        
        self.biggest_sum = sum;
        self.current_sum = self.biggest_sum;
        return self.biggest_sum;

    # dequeue -> remove first item from list and change biggest_sum if find another biggest_sum
    def dequeue(self):
        current_sum = self.current_sum;

        # pop_back first for dequeue
        item = self.pop_back();
        current_sum -= item;

        # update sum by dequeue
        temp = self.list[self.tail];
        current_sum += temp;
        self.tail -= 1;

        # update biggest sum
        if current_sum > self.biggest_sum :
            self.biggest_sum = current_sum;

        # update current sum 
        self.current_sum = current_sum;
    

def main():
    size,removing = tuple(map(int,input().split()));
    array = list(map(int, input().split()));
    numbers = Line(array,size,removing);

    # initial biggest sum
    numbers.initial_sum();

    # dequeue removing time
    for i in range(removing-1):
        numbers.dequeue();
    
    print(numbers.biggest_sum);

main();