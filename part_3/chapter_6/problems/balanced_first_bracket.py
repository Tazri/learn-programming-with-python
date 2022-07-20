'''
problem : 
You will take a bunch of first bracket until 0 and check
that brackets are balanced and not. 

simple input : 
()()((()))
()()(()))
0

simple output : 
Bracket are balanced
Bracket are not balanced
Program Finish
'''

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

def is_balanced(brackets) : 
    bracket_stack = Stack() 

    for char in brackets :
        if char == "(" :
            bracket_stack.push(char);
        else : 
            if bracket_stack.is_empty() :
                return False;
            
            bracket_stack.pop();
    
    if bracket_stack.is_empty() : 
        return True;
    else : 
        return False;

if __name__ == "__main__" : 
    while True : 
        n = input();

        if n == '0' :
            print('Program Finish');
            break;

        if is_balanced(n) : 
            print('Bracket are balanced');
        else : 
            print("Bracket are not balanced");