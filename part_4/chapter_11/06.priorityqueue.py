import heapq as heap

h = [];

# data with priorityqueue
datas = [
    (3,"write code"),
    (2,"write tests"),
    (1,"create specification"),
    (4,"release product")
];

print("Data inserting in priority queue...............");
print("....");
for data in datas:
    # push the with priority
    heap.heappush(h,data);



print("Data Pop Out from Priority Queue : ");
while h:
    data = heap.heappop(h);
    print(f"> data : {data}");

'''
Data inserting in priority queue...............
....
Data Pop Out from Priority Queue : 
> data : (1, 'create specification')
> data : (2, 'write tests')
> data : (3, 'write code')
> data : (4, 'release product')
'''