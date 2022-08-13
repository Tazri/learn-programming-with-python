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

# transplant
def bst_transplant(_target:Binary_Tree.Node,_new:Binary_Tree.Node):
    # extract target
    tp = _target.parent;
    tl = _target.left;
    tr = _target.right;

    # create new node
    new = Binary_Tree.Node();
    new.copyfrom(_new);

    # start transplant
    new.parent = tp;
    new.left = tl;
    new.right = tr;

# transplant
def delete_bst_by_successor(_root:Binary_Tree.Node,data):
    # find the target 
    target = search_bst(_root,data);

    # if target is not found
    if target == None :
        return _root;

    parent_node = target.parent;
    # if target left child has none
    if target.left == None and target.right != None:
        target.right.parent = parent_node;
        del target;
        return _root;

    # if target right child has none
    if target.right == None and target.left != None:
        target.left.parent = parent_node;
        del target;
        return _root;

    # if target has two child
    successor = bst_successor(target);
    successor_right_child = successor.right;
    successor_parent = successor.parent;

    # link child with parent
    successor_parent.right = successor_right_child;

    target.copyfrom(successor);

    return root;

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
    root.parent = 'root';

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

    print("\n\n>>> maximum and minium in root <<<");
    print("maximum_bst(root) : ",maximum_bst(root));
    print("minimum_bst(root) : ",minimum_bst(root));


    print("\n\n>>>Predecessor and successor<<<");
    print('bst_predecessor(root) : ',bst_predecessor(root));
    print('bst_successor(root) : ',bst_successor(root));

    print("\n\n>>> removing <<<");
    Binary_Tree.traverse_inorder_r(root);
    print('\n');
    thirteen = search_bst(root,13);
    print(thirteen);
    delete_bst_by_successor(root,13);