# Node class
class Node : 
    # intial the data
    def __init__(self,_data = None,_prev = None,_next = None):
        self.data,self.prev,self.next = _data,_prev,_next;

    # repr -> for what show node in print
    def __repr__(self):
        return str(self.data);


# Doubly_Linked_List
class Doubly_Linked_List:
    # constructor for intial the value
    def __init__(self):
        self.head = Node('head');
        self.length = 0;

    # repr -> for show the value
    def __repr__(self):
        nodes = [];
        current_node = self.head.next;

        if current_node is None : 
            return 'Doubly_Linked_List[ !! Empty !! ]'

        while current_node :
            nodes.append(current_node.data);
            current_node = current_node.next;

        return 'Doubly_Linked_List' + str(nodes);

    
    # append -> add item in linked list at last position 
    def append(self,_data):
        # create nodes 
        new_node = Node(_data);

        # append the node 
        current_node = self.head;

        while current_node.next :
            current_node =  current_node.next;

        current_node.next = new_node;
        new_node.prev = current_node;

        self.length += 1;
        return self;

    # appends -> add multiple item in linked list at last position
    def appends(self,_datas):
        total_data = 0;
        for _data in _datas:
            self.append(_data);
            total_data += 1;

        return self;

    # prepend -> add item in linked list at first position
    def prepend(self,_data):
        # create node
        new_node = Node(_data);

        # add item at first position
        first_node = self.head.next;
        new_node.next = first_node;

        if first_node != None :
            first_node.prev = new_node

        self.head.next = new_node;

        self.length += 1;
        return self;
    
    # prepends -> add multiple item in linked list at first position
    def prepends(self,_datas):
        datas = _datas.copy();

        while datas :
            self.prepend(datas.pop());

        return self;

    # insert -> add a value after a spacify value
    def insert(self,_target_data,_new_data):
        # find the target node
        target_node = self.search(_target_data);

        if not target_node :
            return None;

        # create node
        new_node = Node(_new_data);

        # get next node
        next_node = target_node.next;
        # add new node in list
        target_node.next = new_node;
        new_node.prev = target_node;
        new_node.next = next_node;

        if not None : 
            next_node.prev = new_node;

        return self;

    # search -> return the finding item in linked list
    def search(self,_data):
        # if linked list is empty
        if self.head.next == None :
            return None;

        current_node = self.head.next;

        while current_node :
            if current_node.data == _data :
                return current_node;

            current_node = current_node.next;

        return None;

    # remove -> remove the item in linked list at position in linked list
    def remove(self,_data):
        target = self.search(_data);

        # if item is not exist
        if target == None : return None;

        # if target node is first node then 

        # get next and prev node
        prev_node = target.prev;
        next_node = target.next;

        # remove target node
        prev_node.next = next_node;
        if next_node != None :
            next_node.prev = prev_node;
        
        return target;

if __name__ == "__main__":
    line = Doubly_Linked_List();
    print(line);
    
    print("\n>>> use append method <<<");
    line.append("Tazri");
    line.append("Alyth").append("Focasa");
    print(line);

    print("\n>>> use appends method <<<");
    line.appends(['Ash','Draw']).appends(['Levi','Serius']);
    print(line);


    print("\n>>> use prepend method <<<");
    line.prepend('Cyclone');
    line.prepend("Hexon").prepend("Farabi");
    print(line);

    print("\n>>> use prepends method <<<");
    line.prepends(["oxyzen","neon"]);
    line.prepends(['Salfar']).prepends(['Nytrozen']);
    print(line);
    print(line.length);

    print("\n>>> use insert method <<<");
    line.insert('neon','xenon');
    print(line);
    line.insert("Alyth","Right").insert("Right","Left");
    print(line);
    what_return_insert = line.insert("unkown",'d');
    print(line);
    print(what_return_insert);

    print("\n>>> use search method <<<");
    person = line.search("Tazri");
    none_person = line.search("tazri");
    print(person);
    print(person.next);
    print(person.next.next);
    print(person.prev);
    print(person.prev.prev);
    print(none_person);

    print("\n>>> use remove method <<<");
    print(line);
    d = line.remove('Left');
    print(line);
    print(d);
    d = line.remove("unknown");
    print(line);
    print(d);
    line.remove("Alyth");
    line.remove("Focasa");
    line.remove("Ash");
    line.remove("Salfar");
    line.remove("Draw");
    line.remove("Nytrozen");
    line.remove("Serius");
    print(line);