# import from postfix
import postfix;

# get_precedence -> return precedence number
def get_precedence(_s:str)->int:
    if _s == '+' : return 1;
    elif _s == '-' : return 1;
    elif _s == '*' : return 2;
    elif _s == '/' : return 2;

# infix to postfix
def infix_to_postfix(expresition:str)->str:
    # create necessary variable
    expresition_list = expresition.split(',');
    postfix = [];
    operators = [];

    # start converting
    for char in expresition_list :
        # if char is digit 
        if char.isdigit() :
            postfix.append(char);
            continue;
        
        # if char is not digit
        while operators: # do this until operator is empty
            poped_op = operators.pop();

            if get_precedence(poped_op) >= get_precedence(char):
                postfix.append(poped_op);
            else: # back pop operator in stack with char.
                operators.append(poped_op);
                operators.append(char);
                break;

        if not operators: # if operator is empty    
            operators.append(char);
    
    # finish the loop then
    while operators: 
        postfix.append(operators.pop());

    result =  ','.join(postfix);
    return result;

# test infix to postfix
def test_infix_to_postfix()->None:
    test_cases = [
        {
            'name' : "simple case 1",
            "input" : '1,+,3,*,2',
            'expected' : '1,3,2,*,+'
        },
        {
            'name' : "simple case 2",
            'input' : '1,+,3,*,2,+,4',
            'expected' : '1,3,2,*,+,4,+'
        },
        {
            'name' : 'simple case 3',
            'input' : '1,+,3,-,2',
            'expected' : '1,3,+,2,-'
        },
        {
            'name' : 'simple case 4',
            'input' : '1,+,2,+,3,*,4,-,5',
            "expected" : '1,2,+,3,4,*,+,5,-'
        }
    ];

    for case in test_cases:
        result = infix_to_postfix(case['input']);

        assert result == case['expected'] and case['name'];
    return None;

# show result
def show_result(_input:str)->None:
    print("> input :",_input);
    result = infix_to_postfix(_input);
    print("> Output :",result);
    print("----------------------\n");

if __name__ == '__main__':
    print("Enter exit to terminate the program.\n");

    while 1 :
        command = input("Enter expresition : ");
        
        if command == 'exit' :
            postfix.terminate();
            exit();
        
        show_result(command);
        