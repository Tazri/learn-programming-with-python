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

# transplant
def transplant(_root:Binary_Tree.Node,_current_node:Binary_Tree.Node,_new_node:Binary_Tree.Node):
    if _current_node.parent == None :
        _root = _new_node;
    elif _current_node == _current_node.parent.left :
        _current_node.parent.add_left(_new_node);
    else :
        _current_node.parent.add_right(_new_node);
    
    return _root;


# create on kind of bst
def create_bst():
    """
                 10 
               /    \
              5     17
             / \   /  \
            3   7 12  19
           / \
          1   4
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
