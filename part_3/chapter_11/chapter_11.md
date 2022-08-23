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

# Heap
Heap is one kind of complete data structure. Where value of root is less than or equal of children or greater than or equal of children. They are two type of heap.

1. Min heap. Here root are equal or smaller than children.
2. Max heap. Here root are equal or greater than childre.

Example : 

![Heap](./../../asset/data_structure/heap.png)

