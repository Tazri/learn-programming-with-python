# binary node
from multiprocessing import current_process


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
    # create root stack
    root_stack = [_root];

    while root_stack:
        # get root from stack and print
        current_root = root_stack.pop();
        print(current_root);

        # if right root exist then append it to root stack
        if current_root.right :
            root_stack.append(current_root.right);
        
        # if left root exist then append it to root stack
        if current_root.left :
            root_stack.append(current_root.left);


# post-order traverse binary tree in recursive 
def traverse_post_order(_root):
    # if left exist 
    if _root.left :
        traverse_post_order(_root.left);

    # if right exist
    if _root.right :
        traverse_post_order(_root.right);
    
    # and print the root
    print(_root);

# post-order traverse binary tree in iterative
def traverse_post_order_iterative(_root):
    # if _root is None 
    if _root == None :
        return;

    # create node_stack and print_stack
    node_stack = [_root];
    print_stack = []; # here contain data to print 

    while node_stack :
        popped_node = node_stack.pop();

        # if left and right exist then first left push after right push to node stack
        if popped_node.left :
            node_stack.append(popped_node.left);

        if popped_node.right :
            node_stack.append(popped_node.right);

        # push the popped node to print_stack
        print_stack.append(popped_node);
             
    while print_stack :
        print(print_stack.pop());



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
    
    output will : 2 7 1 6 5 10 9 8 3 4
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

    # pre_roder traverse in iterative way
    print("\n>>> Traverse Pre Order in Iterative Way <<<");
    traverse_pre_order_iteravite(root);

    # post_order traverse in recursive 
    print("\n>>> Traverse Post Order in Recursive Way <<<");
    traverse_post_order(root);

    # post_order traverse in iterative 
    print("\n>>> Traverse Post Order in Iterative Way <<<");
    traverse_post_order_iterative(root);