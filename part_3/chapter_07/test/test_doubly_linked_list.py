import sys 

sys.path.append('.');

import Doubly_Linked_List

# test append
def test_append():
    dll = Doubly_Linked_List.Doubly_Linked_List();
    
    # is head next pointed None
    assert dll.head.next == None , 'Head must pointed None';

    # is head next point first node
    dll.append("item one");
    assert dll.head.next.data == "item one", "Head should point the first node";

    # is first node prev point head 
    first_node = dll.head.next;
    assert first_node.prev.data == "head", "First node previous pointed is must be head";

    # check again is head pointed first node after add secound item
    dll.append("item two");
    assert dll.head.next.data == "item one", "Head should point the first node";

    # is first node pointed the second node
    secound_node = first_node.next;
    assert first_node.next.data == secound_node.data, "First node must be pointed secound node";

    # is secound node pointed first node previously
    assert secound_node.prev.data == first_node.data, "Secound node must be previously pointed first node";

    # check dll string presentation
    assert str(dll) == "Doubly_Linked_List['item one', 'item two']", "Doubly_Linked_List object can show string presentation properly";


def test_prepend():
    dll = Doubly_Linked_List.Doubly_Linked_List();

    item = 1;
    dll.prepend(item);

    # head should pointed first node
    assert dll.head.next.data == item, "Head should pointed the first node after prepend";

    new_item = 2;
    dll.prepend(new_item);

    # cehck head can point the new node after prepend
    assert dll.head.next.data == new_item, "Head should pointed the new node after prepend";

    new_node = dll.head.next;
    old_node = new_node.next;

    # check is old node pointed the None ?
    assert old_node.next == None, "First prepend item after secound prepend item, first prepend item must be next point to None";

    # check is old node prev point to new node ?
    assert old_node.prev.data == new_node.data, "First prepend item after secound prepend item, first prepend item must be prev point to previous node";

    # check is new node next point to old node ?
    assert new_node.next.data == old_node.data, "First prepend item after secound prepend item, first prepend item must be point next to old node"

    # check dll string presentation
    assert str(dll) == "Doubly_Linked_List[2, 1]", "Prepend : Doubly_Linked_List object can show string presentation properly";

def test_search():
    dll = Doubly_Linked_List.Doubly_Linked_List();

    item = 5;
    assert dll.search(item) == None, "item shouldn't be found in an empty list";

    dll.append(item);
    node = dll.search(item);
    assert node.data == item, "item should be found in the list";

    dll.append(10);
    dll.append(15);
    node = dll.search(10);
    assert node.data == 10, "10 should be found in the list";

    node = dll.search(20);
    assert node == None, "20 should not be found in the list";

def test_remove():
    dll = Doubly_Linked_List.Doubly_Linked_List();

    dll.append(5);
    dll.append(10);
    dll.append(15);
    dll.append(20);

    node_5 = dll.search(5);
    node_10 = dll.search(10);
    node_15 = dll.search(15);
    node_20 = dll.search(20);

    assert node_10.next == node_15, "simple remove test 1";
    assert node_15.prev == node_10, "simple remove test 2";
    
    # remove from the middle of list
    dll.remove(15)
    assert node_10.next == node_20, "now next of 10 should be 20";
    assert node_20.prev == node_10, "now prev of 20 should be 10";
    # check dll string presentation
    assert str(dll) == "Doubly_Linked_List[5, 10, 20]", "15 should not be in the list anymore";


    # Remove from end
    dll.remove(20);
    assert node_10.next == None, "now next of 10 should be None";
    assert str(dll) == "Doubly_Linked_List[5, 10]", "20 should not be in the list anymore";

    # Remove from start
    dll.remove(5);
    assert dll.head.next == node_10, "now head should point to 10";
    assert node_10.prev.data == 'head', "10 is the first node, so prev should be head";

    assert str(dll) == "Doubly_Linked_List[10]", "dll should only contain 10";

