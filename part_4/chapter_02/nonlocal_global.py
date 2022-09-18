name = "anonymo";

print(">>> name is : ",name)
def outer_add(a,b):
    result = 0;
    
    def inner_add(a,b):
        nonlocal result; 
        result = a + b;
        print("> inner_add result : ",result);
    
    inner_add(a,b)
    
    print("> outer_add result : ",result);
    # change global name varibale
    global name; 
    name = "sirius";
    print("name in function : ",name)
    
outer_add(3,4);
print(">>> after calling outer_add name :",name)