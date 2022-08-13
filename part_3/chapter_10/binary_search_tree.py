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

# find maximum item
def maximum_bst(_root):
    right_root = _root;

    while right_root.right : right_root = right_root.right;

    return right_root;

# find minimum item in bst
def minimum_bst(_root):
    left_root = _root;
    while left_root.left : left_root = left_root.left;

    return left_root;

# find successor
def bst_successor(_root):
    right_child = _root.right;

    return minimum_bst(right_child);

# find predecessor
def bst_predecessor(_root:Binary_Tree.Node):
    left_child = _root.left;

    return maximum_bst(left_child);

# find pre

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
    root.parent = 'root';

    items = [5,17,3,7,12,19,1,4];
    
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
           / \
          1   4
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

    print("\n\n>>> maximum and minium in root <<<");
    print("maximum_bst(root) : ",maximum_bst(root));
    print("minimum_bst(root) : ",minimum_bst(root));


    print("\n\n>>>Predecessor and successor<<<");
    print('bst_predecessor(root) : ',bst_predecessor(root));
    print('bst_successor(root) : ',bst_successor(root));
    