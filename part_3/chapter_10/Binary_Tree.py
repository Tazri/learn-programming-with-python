# create binary node class
class Node : 
    def __init__(self,_data = None,_left = None,_right = None,_parent=None):
        self.data = _data;
        self.left = _left;
        self.right = _right;
        self.parent = _parent;

    def __repr__(self):
        return str(self.data);

    def add_left(self,_node):
        self.left = _node;
        if _node != None :
            self.left.parent = self;

    def add_right(self,_node):
        self.right = _node;
        if _node != None :
            self.right.parent = self;

    def copyfrom(self,_node):
        self.data = _node.data;
        self.left = _node.left;
        self.right = _node.right;
        self.parent = _node.parent

def traverse_inorder_r(_root):
    if _root.left :
        traverse_inorder_r(_root.left);

    print(_root,end="  ");

    if _root.right :
        traverse_inorder_r(_root.right);