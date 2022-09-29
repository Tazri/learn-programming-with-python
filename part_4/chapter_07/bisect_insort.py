from bisect import insort 

if __name__ == "__main__":
    for n in range(11):
        li = [1,2,2,3,4,6,8,9];

        print("> li : ",li);
        print("> li <-(",n,") insert");
        insort(li,n);
        print("> li : ",li);
        print("-------------------------------\n");