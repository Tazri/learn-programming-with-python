class Stack :
    # constructor 
    def __init__(self) :
        self.stack = [];

    # is_empty method
    def is_empty(self) :
        if len(self.stack) :
            return False;
        else : 
            return True;

    # push method
    def push(self,item) :
        self.stack.append(item);

    # pop method 
    def pop(self) : 
        if self.is_empty() :
            return None 
        else : 
            return self.stack.pop();


if __name__ == "__main__" : 
    books = Stack();
    books.push("Nimikh Pane");
    books.push("Programminger Adonpanto");
    books.push("message");
    books.push("python die programming shikha");

    while not books.is_empty() : 
        print("Books name : ",books.pop());