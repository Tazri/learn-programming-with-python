# find_index -> find index for x in list li
def find_index(li:list,x:int)->int:
    for i in range(len(li)):
        if li[i] > x : 
            return i;
    
    return len(li);

# insort -> insert element in list
def insort(li:list,x:int)->list : 
    index = find_index(li,x);

    li.append(x);

    for i in range(len(li)-2,index-1,-1):
        li[i+1] = li[i];

    li[index] = x;

    return li;


if __name__ == "__main__":
    li = [1,2,4,7,8];
    print("li : ",li);

    print("after insort(li,3) :");
    insort(li,3);
    print(li);

    print("after insort(li,10) :");
    insort(li,10);
    print(li);

    print("after insort(li,15) :");
    insort(li,15);
    print(li);