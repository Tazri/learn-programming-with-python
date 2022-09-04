def binary_search(_list,_target,_left = 0,_right = None):
    # by default value of right
    if _right == None :
        _right = len(_list) - 1;


    # calculate mid 
    mid = (_left+_right)//2;

    # if left > right, that means target not in list
    if _left > _right :
        return None;

    # if mid index is target index
    if _list[mid] == _target : 
        return mid;


    # if mid index is less than target index
    if _list[mid] < _target:
        _left = mid + 1;
        return binary_search(_list,_target,_left,_right);
    
    # if mid index is greater than target index
    _right = mid - 1;
    return binary_search(_list,_target,_left,_right);


if __name__ == "__main__":
    L = [1,2,3,5,6,7,8,9];
    

    is_fail = False;
    for x in range(1,11):
        position = binary_search(L,x);


        if position == None :
            print(position);
            if x in L :
                print(L);
                print(">>>",x,"is in L but function returned None");
                is_fail = True;
            else:
                print('>>> ',x,'not in list');
        else :
            if L[position] == x :
                print(">>>",x,"found in correct position.");
            else :
                print(">>> return",position,"for",x,"which is not correct.");
                is_fail = True;

    
    print("\n.....\n....\n...\n..\n.");
    if is_fail :
        print(">>> Test Failed :( <<<");
        print(">>> Debug Your Code <<<");
    else :
        print(">>> Test Successfully Passed :) <<<");
        print(">>> Go To Drink A Cup Of Tea <<<");

