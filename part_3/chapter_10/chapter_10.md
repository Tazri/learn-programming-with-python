Chapter 10 : Binary Search Tree
===============================
Binary Search Tree is a kind of tree which left child is smaller than root and right child greater than root. Here simple example : 

![Binary Search Tree Data Structure](./../../asset/data_structure/binary_search_tree.png)


## Point of Binary Search Tree
- Every left child is smaller than root.
- Every right child is greater than root.
- Every child of right child must be greater than root.
- Every child of left child must be smaller than root.
- In order traverse of Binary Search Tree Then it produce sorted item. 

## Inorder Predecessor and Successor
When traverse the binary search tree and this time every given node's neighbors called **predecessor** and **successor**. The node behind the given node called **predecessor** and the node ahead the given node called **successor**. Here example : 

![In order successor and predecessor](./../../asset/data_structure/inorder_predeseccor_and_successor.png)


## How to insert a node in binary search tree. 
Here algorithm for insert a node in binary search tree :

input : root, node 
1. if root is empty then set node as root. and go 4
1. if node is smaller then root then check left. if left child is empty then insert it and go 4 left other wise traverse left and go back 2.
1. if node is greater then root then check right. if right child is empty then insert it and go 4 other wise traverse right node and go back 2.
1. return the root.

***Insert a node in binary search tree : insert_bst***
```python
# insert node as binary search tree
def insert_bst(root,node) :
    last_root = None;
    current_root = root;

    # traverse the root until find a place
    while current_root :
        last_root = current_root;

        # if node < root
        if current_root.data > node.data :
            current_root = current_root.left;

        # if node > root
        elif current_root.data < node.data :
            current_root = current_root.right;

        # if node == root
        else :
            return False;

    if node.data < last_root.data :
        last_root.add_left(node);
    elif node.data > last_root.data :
        last_root.add_right(node);
    else : 
        root == last_root;

    return root;
```


### How to find minimum node in binary search tree.
Minimum node of binary search tree is last node of left child. Traverse the left child again and again until reach the last level of tree then we can find the minimum node of binary tree.

> first left node of last level is minimum node of binary search tree.

***Find minimum in binary search tree: bst_minimum***
```python
# minimum
def bst_minimun(_root:Binary_Tree.Node)->Binary_Tree.Node:
    left = _root;

    while left.left : left = left.left;

    return left;
```

### How to find maximum node in binary search tree. 
Maximum node of binary search tree is last node of right child. Traverse 