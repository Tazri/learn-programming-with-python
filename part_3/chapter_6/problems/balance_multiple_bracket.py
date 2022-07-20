'''
problem : 
You will take a bunch of brackets until 0 and check
that brackets are balanced and not. 

simple input : 
{}[]()[()]
[]][
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
        
        return True 

    # push method
    def push(self,item) : 
        self.stack.append(item);
    

    # pop method 
    def pop(self) :
        return self.stack.pop();



def is_balanced(brackets):
    brackets_stack = Stack();

    for char in brackets :
        # if bracket was left
        if char in '([{' :
            brackets_stack.push(char);
            continue;

        # check is stack empty or not for right bracket
        if brackets_stack.is_empty() :
            return False 
        
        # if bracket was right
        left_bracket = brackets_stack.pop();

        if left_bracket == '(' and char != ')' :
            return False;
        elif left_bracket == '{' and char != '}' :
            return False;
        elif left_bracket == '[' and char != ']' :
            return False;

    
    # check brackets stack are empty or not
    if brackets_stack.is_empty() :
        return True;
    else :
        return False;


while True : 
    n = input();

    if n == '0' :
        print('Program Finish'); 
        break;

    if is_balanced(n) :
        print("Bracket are balanced.");
    else : 
        print("Braket are not balanced.");