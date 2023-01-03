from queue import PriorityQueue;

pq = PriorityQueue();

# create random priority data
datas = [
    (3,"write code"),
    (2,"write tests"),
    (1,"create specification"),
    (4,"release product")
];

'''
pq.put() use for insert data.
pq.get() use for get data.
pq.qsize() use for know the queue size
'''

print("> pq.put(data).......");
print("......");
for data in datas : 
    pq.put(data);
    
print("\n> pq.get()...........");
while pq.qsize():
    print(f"> pq.get() : {pq.get()}");

'''
ity_queue_package.py 
> pq.put(data).......
......

> pq.get()...........
> pq.get() : (1, 'create specification')
> pq.get() : (2, 'write tests')
> pq.get() : (3, 'write code')
> pq.get() : (4, 'release product')
'''