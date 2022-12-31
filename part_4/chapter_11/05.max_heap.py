import heapq

class MaxHeap:
    def __init__(self,items=[]):
        self.h = [x*-1 for x in items];

        if items:
            heapq.heapify(self.h);
        
    def __len__(self):
        return len(self.h);

    def push(self,item):
        heapq.heappush(self.h,-item);
        return self;
    
    def pop(self):
        return -heapq.heappop(self.h);

    def look(self):
        return -self.h[0];
    

if __name__ == "__main__":
    items = [1,3,5,7,9,2,4,6,8,0];
    mx_heap = MaxHeap();
    
    for item in items:
        mx_heap.push(item);

    li = [mx_heap.pop() for _ in range(len(mx_heap))];
    print(f"items : {items}")
    print(f"li : {li}");

'''
output : 
items : [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
li : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
'''