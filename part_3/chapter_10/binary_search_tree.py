import Binary_Tree

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

# search item in bst
def search_bst(_root,_key):
    current_node = _root;

    while current_node :
        if current_node.data == _key :
            return current_node;
        elif current_node.data > _key :
            current_node = current_node.left;
        else :
            current_node = current_node.right;

    return current_node;

# minimum
def bst_minimun(_root:Binary_Tree.Node)->Binary_Tree.Node:
    left = _root;

    while left.left : left = left.left;

    return left;

# maximum
def bst_maximum(_root:Binary_Tree.Node)->Binary_Tree.Node:
    right = _root;

    while right.right : right = right.right;

    return right;

# transplant
def bst_transplant(_root:Binary_Tree.Node,_current_node:Binary_Tree.Node,_new_node:Binary_Tree.Node):
    if _current_node.parent == None :
        _root = _new_node;
    elif _current_node == _current_node.parent.left :
        _current_node.parent.add_left(_new_node);
    else :
        _current_node.parent.add_right(_new_node);
    
    return _root;


# delete
def bst_delete(_root:Binary_Tree.Node,_node:Binary_Tree.Node):
    # if left dose not exist or both dose not exist
    if _node.left == None :
        bst_transplant(_root,_node,_node.right);
        return _root;
    
    # if right dose not exist
    if _node.right == None:
        bst_transplant(_root,_node,_node.left);
        return _root;

    # if left and right both exist 
    # find the successor
    successor = bst_minimun(_node.right);

    # if node was parent
    if _node.parent == None :
        p_left = _root.left;
        p_right = _root.right;

        bst_transplant(_root,successor,successor.right);
        bst_transplant(_root,_node,successor);
        successor.add_left(p_left);
        successor.add_right(p_right);      
        return successor;

    # if node was not parent
    node_parent = _node.parent;
    n_left = _node.left;
    n_right = _node.right;
    bst_transplant(_root,successor,successor.right);
    bst_transplant(_root,_node,successor);
    successor.add_left(n_left);
    successor.add_right(n_right);
    successor.parent = node_parent;
    return _root;

# create on kind of bst
def create_bst():
    """
                 10 
               /    \
              5     17
             / \   /  \
            3   7 12  19
           / \      \
          1   4     13
    """

    
    root = Binary_Tree.Node(10);

    items = [5,17,3,7,12,19,1,4,13];
    
    for item in items:
        node = Binary_Tree.Node(item);
        insert_bst(root,node);

    return root;


if __name__ == '__main__':
    """
                 10 
               /    \
              5     17
             / \   /  \
            3   7 12  19
           / \      \
          1   4     13
    """

    root = create_bst();
    print(root);
    print("Traverse the root : ");
    Binary_Tree.traverse_inorder_r(root);
    print();

    print("\n\n> Serach 5 in bst :");
    node_five = search_bst(root,5);
    print('node_five :',node_five);
    print('node_five.left :',node_five.left);
    print('node_five.right :',node_five.right);

    print('\n\n> Search 8 in bst : ');
    node_eight = search_bst(root,8);
    print(node_eight);


    print("\n\n>>> check bst_minimum <<<");
    print("bst_minimum(root) : ",bst_minimun(root));
    print("bst_minimum(root.right) : ",bst_minimun(root.right));
    print("bst.minimum(root.left) : ",bst_minimun(root.left));

    print("\n\n>>> Check bst_maximum <<<");
    print("bst_maximum(root) : ",bst_maximum(root));
    print("bst_maximum(root.left) : ",bst_maximum(root.left));

    print("\n\n>>> check bst_delete <<<");
    delete_result = bst_delete(root,root);

    """
                 12 
               /    \
              5     17
             / \   /  \
            3   7 13  19
           / \      
          1   4     
    """


    root = delete_result;
    print("After bst_delete(root,root) : ");
    print(delete_result);
    print(delete_result.left);
    print(delete_result.right);
    print(delete_result.right.right);


    delete_result = bst_delete(root,node_five);
    print("\n>>> After bst_delete(root,node_five) <<<");
    """
             12 
           /    \
          7     17
         /     /  \
        3     13  19
       / \      
      1   4     
    """
    print(root);
    print(root.left);
    print(root.left.left);
    print(root.left.left.left);
    print(root.left.left.right);