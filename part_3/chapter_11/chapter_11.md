Chapter : Heap, Heap Sort and Priority Queue
============================================

Here discust about :
- Full and complete binary tree.
- Heap.
- Implement max heap and min heap.
- Implement heap sort.
- Implement Priority Queue.
<hr />

## Full and Complete Binary tree
***Full Binary Tree :*** Full binary tree is a kind of binary tree where every node has either two children or no children. Here example : 

![Full Binary Tree](./../../asset/data_structure/full_binary_tree.png)

***Complete Binary Tree :*** Complete binary tree is a tree which all level fill except last level, which filled from the left. Here example : 

![Complete Binary Tree](./../../asset/data_structure/complete_binary_tree.png)

We can store complete binary tree into array. In that case every node left child index is double of it's index and right child index is more than one of left child index.

```python
def left(n):
    return n*2;

def right(n):
    return (n*2) + 1;
```
Visual Example : 

![Complete binary store in array](./../../asset/data_structure/store_complete_binary_tree_into_array.png)

<hr />
<br />

## Heap
Heap is one kind of complete data structure. Where value of root is less than or equal of children or greater than or equal of children. They are two type of heap.

1. Min heap. Here root are equal or smaller than children.
2. Max heap. Here root are equal or greater than childre.

Example : 

![Heap](./../../asset/data_structure/heap.png)


## How to check a list or a array is max heap or min heap ?

First Traverse the array from last with checking is node is bigger or smaller than parent. Here algorithm to check is a array or a list is max heap. 

0. input : list l 
1. traverse the array from last to secound first and do step two every traverse. if traverse is done then go 4.
2. array element n and index ni. check n > l[ni//2] or check n is smaller then parent. if it false then stop traversing do step 3.
3. return false. stop here.
4. return true. stop here.

Same with heap sort. just check is parent greater than from node or not. Here implementation : 

***Program : checking is heap or not :***
```python
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

# is_min_heap
def is_min_heap(_heap):
    n = len(_heap) - 1;

    for i in range(n,1,-1):
        if _heap[get_parent(i)] > _heap[i] :
            return False;
    
    return True;

```

<hr />
<br />

## How to build a array to heap ?
Before learn how to build a array to heap, we need to learn how to build a single sub tree to heap. In that case first. The algorithm is : 

0. input a list l, size, and root_index
0. figure out bigger value index from first tree. the index is i.
0. i == root_index ? if false then go step 4.
0. swap root_index value with i and set root_index = i. Go to the step 1.
0. return the l. end here.

