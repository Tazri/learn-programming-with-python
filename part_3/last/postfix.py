def operate(sa:str,sb:str,op:str):
    na = int(sa);
    nb = int(sb);

    if op == '+' : return na + nb;
    elif op == '-' : return na - nb ;
    elif op == '*' : return na * nb ;
    elif op == '/' : return na / nb ;
    elif op == '%' : return na % nb;

# postfix_evalute -> evalute the postfix expression
def postfix_evaluate(expression:str)->int: 
    # split the number and create necessary variable
    expression_list = expression.split(','); 
    number_stack = [];
    operators = '+*-/%';

    # start to evalute postfix
    for char in expression_list :
        if char.isdigit() : 
            number_stack.append(char);
        if char in operators :
            print(number_stack);
            o_two = number_stack.pop();
            o_one = number_stack.pop();
            result = operate(o_one,o_two,char);
            number_stack.append(result);
    
    print(number_stack);
    return number_stack[0];

# terminate -> finish the program here
def terminate()->None:
    print("-----------------------");
    print("---------------------");
    print("-------------------");
    print("-----------------");
    print("---------------");
    print("-> Program Terminate <-");
    exit();

# show result 
def show_result(s:str)->None:
    result = postfix_evaluate(s);
    print("Result : ",result);
    print("----------------");
    print("\n")


if __name__ == '__main__': 
    print("comand 'exit' to terminate the program")

    while 1:
        n = input("Enter Expression : ")

        if n == "exit":
            terminate();
            break;
        
        show_result(n);