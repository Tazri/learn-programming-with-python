# binary node
class TreeNode : 
    # constructor 
    def __init__(self,_data=None,_left=None,_right=None,_parent=None):
        self.data = _data;
        self.left = _left;
        self.right = _right;
        self.parent = _parent;

    # show data
    def __repr__(self):
        return str(self.data);

    # add_left -> add node to left
    def add_left(self,_node):
        self.left = _node;
        
        if not _node :
            _node.parent = self;
    
    # add_right -> add node to right
    def add_right(self,_node):
        self.right = _node;
        
        if not _node :
            _node.parent = self;


# pre-order traverse binary tree in recursive
def traverse_pre_order(_root):
    # first print root data
    print(_root);

    # if left child exist than print it first.
    if _root.left :
        traverse_pre_order(_root.left);

    # if right child exist than print it.
    if _root.right :
        traverse_pre_order(_root.right);

# pre-order traverse binary tree in iterative way
def traverse_pre_order_iteravite(_root):
    node = _root;

    while node :
        print(node);

        # left node
        if node.left :
            node = node.left;
        
        # right node 
        if node.right :
            node = node.right;

def create_tree():
    '''
    Create below tree data structure
            _2_
           /   \
          7     9
         / \     \
        1   6     8
           / \   / \
          5  10 3   4
    '''
    # creating 0 and 1 level nodes
    two = TreeNode(2);
    seven = TreeNode(7);
    nine = TreeNode(9)

    # add to data structure 0 and 1 level node
    two.add_left(seven);
    two.add_right(nine);

    # createing 2 level nodes
    one = TreeNode(1);
    six = TreeNode(6);
    eight = TreeNode(8);

    # add 2 level nodes in structure
    seven.add_left(one);
    seven.add_right(six);
    nine.add_right(eight);

    # creating three level node
    five = TreeNode(5);
    ten = TreeNode(10);
    three = TreeNode(3);
    four = TreeNode(4);

    # add 3 level nodes in structure
    six.add_left(five);
    six.add_right(ten);
    eight.add_left(three);
    eight.add_right(four);

    return two;

if __name__ == "__main__" :
    '''
    Create below tree data structure
            _2_
           /   \
          7     9
         / \     \
        1   6     8
           / \   / \
          5  10 3   4
    '''
    root = create_tree();
    
    # pre_order traverse in recursive
    print(">>> Traverse Pre Order in Recursive Way <<<");
    traverse_pre_order(root);
