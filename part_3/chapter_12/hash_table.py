# node class
class Table_Node :
    pass;

class Table_Node:
    def __init__(self,_data=None,_key=None,_next:Table_Node=None,_prev:Table_Node=None):
        self.data,self.key,self.next,self.prev = _data,_key,_next,_prev;

    # insert data in table node
    def insert(self,_data,_key):
        # if it is first _data in node
        if self.data == None :
            self.data = _data;
            self.key = _key;
        else :
            # create a node
            new_node = Table_Node(_data,_key);
            current_node = self;
            while current_node.next : current_node = current_node.next;
            current_node.next = new_node;
            new_node.prev = current_node;

    # search item by key
    def search(self,_key):
        current_node = self;
        while current_node : 
            if current_node.key == _key : 
                return current_node;
            
            current_node = current_node.next;
        
        return False;


# hash table
class Hash_Table:
    # constructor
    def __init__(self,_size:int=None,_hash=None):
        self.size,self.hash = _size,_hash;

        if self.is_positive_int(_size) :
            self.table = [];

            for i in range(_size):
                self.table.append(Table_Node());

            self.last_index = _size - 1;
        else : 
            self.table = [];

    # set hash function
    def set_hash(self,_hash)->int:
        self.hash = _hash;
        return 1;

    # check is int positive integer or not
    def is_positive_int(self,_n:int):
        return int(_n) == _n and _n > 0;

    # set size
    def set_size(self,_size:int):
        # check is self.size is define
        assert not (self.size != None) and ">>> Size is define already. if define the size again then clear the the table first using clear() method."

        # check is _size is positive integer value
        assert not self.is_positive_int(_size) and ">>> Please pass a positive non zero parameter for set_size() method.";

        self.size = _size;
        self.last_index = _size - 1;
        self.table = [Table_Node] * _size;
        return self;
    
    # clear -> clear the whole hash table
    def clear(self):
        del self.table;
        self.size = None;
        self.last_index = None;
        return self;

    # generate_index -> generate the index by hash function
    def generate_index(self,_key)->int:
        index = self.hash(_key);

        if self.is_positive_int(index) and index <= self.last_index and index >= 0:
            return index;
        else : 
            assert False and ">>> Please define the hash function like it return positive integer between 0 and " + str(self.last_index);

    def insert(self,_key,_data):
        # if hash not define
        assert not(self.hash == None) and ">>> Please Define the Hash First using set_hash.";
        
        # if size is not define
        assert not(self.size == None) and ">>> Please Define the size using set_size methods.";    
        
        # generate index
        index = self.hash(_key);
        # get nodx from array at index
        table_node = self.table[index];
        table_node.insert(_data,_key);
        return self;

    def search(self,_key)->list:
        # creating index and find the index node
        index = self.hash(_key);

        # if index was not range
        if index < 0 and index > self.last_index :
            return [index,False];

        target_node = self.table[index];
        searched_item = target_node.search(_key);

        if not searched_item :
            return [index,False];
        else:
            return [index,searched_item];

if __name__ == "__main__":
    # setup student list with hash function and size.
    student_list = Hash_Table(10);

    def hash_function(_roll):
        return (_roll%1000);

    student_list.set_hash(hash_function);

    # insert some student in student_list
    student_list.insert(1003,"Rapid");
    student_list.insert(1004,"anonymo");
    student_list.insert(1000,"sirius");
    student_list.insert(1003,"dridon");

    # print stduent list
    print("Stduent List : ");
    print(student_list);
    print("stduent_list.table : ");
    print(student_list.table);

    # checking is element placed perfect placed
    print("\n\n>>> Checking Every element placed perfect placed ?");
    print("stdutend_list.table[3].data : must be Rapid");
    print(student_list.table[3].data);
    print("studentd_list.table[3].next.data : Must be dridon");
    print(student_list.table[3].next.data);
    print("student_list.table[0].data : must be sirius");
    print(student_list.table[0].data);
    print("student_list.table[4].data : must be anonymo");
    print(student_list.table[4].data);

    # check searching
    print("\n\n>>> Check searching");
    result = student_list.search(1000);
    print(result);
    print("result[1].data : must be sirius");
    print(result[1].data);
    
    result = student_list.search(1007);
    print("result : must be not found");
    print(result);

    result = student_list.search(1003);
    print("result[1].data : must be Rapid");
    print(result[1].data);
    print(result);