# create Node class
class Node:
    def __init__(self,_data = None,_next = None):
        self.data = _data;
        self.next = _next;
    
    def __repr__(self):
        return self.data;


# create linked list 
class Linked_List:
    # constructor 
    def __init__(self):
        # set head of link list
        self.head = Node();

    # repr -> print the linked list
    def __repr__(self):
        datas = [];
        current_node = self.head.next;

        while current_node :
            datas.append(current_node.data);
            current_node = current_node.next;

        datas = 'linked_list'+str(datas);
        return datas;

    # append -> add node in last position of linked list
    def append(self,_data):
        # create node 
        node = Node(_data);

        current_node = self.head;

        while current_node.next :
            current_node = current_node.next;
        
        current_node.next = node;

        return 1;
    
    # appends -> add multiple item in linked list in last position
    def appends(self,_items):
        for _item in _items :
            self.append(_item);
        return 1;

    # prepend -> add node in first position of linked list
    def prepend(self,_data):
        # create node
        node = Node(_data);

        first_node = self.head.next;
        self.head.next = node;
        self.head.next.next = first_node;

        return 1;

    # prepends -> add multiple item in linked list in first position
    def prepends(self,_items):
        for _item in _items:
            self.prepend(_item);
        return 1;

    # search -> finding the node
    def search(self,_item):
        current_node = self.head.next;

        while current_node :
            if current_node.data == _item :
                return current_node;
            
            current_node = current_node.next;
        
        return None

    # insert -> insert a item next to spacify node
    def insert(self,_data,_insert_data):
        # searhing _data in list
        target_node = self.search(_data);

        if target_node is None :
            return False;

        # insert data
        next_node = target_node.next;
        new_node = Node(_insert_data,next_node);
        target_node.next = new_node;
        return True;

    # dequeue
    def dequeue(self):
        # if linked list was empty
        if self.head.next == None :
            return None;
        
        first_node = self.head.next;
        secound_node = first_node.next;
        self.head.next = secound_node;

        return first_node;

    # remove -> remove the first item from list
    def remove(self,_item):
        # if list was empty
        if self.head.next == None :
            return None;

        # if it was first data
        if self.head.next.data == _item :
            remove_node = self.dequeue();
            return remove_node;

        # remove item 
        current_node = self.head.next;
        while current_node :
            next_node = current_node.next;

            # if next node is None
            if next_node == None :
                return None;
            
            # if find the data in next node then delete it
            if next_node.data == _item :
                current_node.next = next_node.next;
                return next_node;

            current_node = current_node.next;

        return None;

if __name__ == "__main__":
    li = Linked_List()

    print(">>> Testing append and prepend <<<");
    li.append("tazri");
    li.append("neon");

    print(li);

    li.prepend('boson');
    print(li);
    
    li.prepend('altra');
    print(li);

    li.append('hellos');
    print(li);

    print("\n>>> Testing search <<<");
    altra = li.search('altra')
    print(altra.data);
    print(altra.next);

    person = li.search('neon');
    print(person);
    print(person.next);
    print(person.next.next);

    person_one = li.search('alyath');
    print(person_one);

    print("\n>>> Testing dequeue method <<<");
    print(li);
    n = li.dequeue();
    print(n);
    print(li);
    li.dequeue();
    print(li);

    li.prepend('boson');
    li.prepend('altra');
    

    print("\n>>> Testing remove method <<<");
    print(li);
    r = li.remove("altra");
    print(li);
    print(r);
    r = li.remove('neon');
    print(r);
    print(li);
    r = li.remove('alayth');
    print(r);
    print(li);
    r = li.remove("hellos");
    print(r);
    print(li);
    li.remove('boson');
    li.remove('tazri');
    print(li);
    r = li.remove('3');
    print(r);
    print(li);

    print("\n>>> Testing appends method <<<");
    li.appends(["ultra","focasa","tazri","hellos","farabi","levi"]);
    print(li);

    print("\n>>> Testing prepends method <<<");
    li.prepends(["antra","alayth"]);
    print(li);
    li.dequeue();
    li.dequeue();
    li.dequeue();

    print("\n>>> Testing insert <<<");
    print(li);
    li.insert("tazri","ultra");
    print(li)
    li.insert("levi","erwine");
    print(li);
    li.insert("unkown",'nobody');
    print(li);