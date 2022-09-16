def my_range(start:int,end:int=None,step:int=1):
    if end == None : 
        end = start;
        start = 0;

    while start < end :
        yield start;
        start += step;

if __name__ == "__main__":
    # say hello from 0 to 4
    print(">>> say hello from 0 to 4 <<<");
    for i in my_range(5):
        print("Hello, Mr.",i);

    print("\n>>> say ok for every even number between 10 and 20 <<<");
    for i in my_range(10,20,2):
        print("Everythink ok : ",i);