# create a simple iteration object
class my_range:
    def __init__(self,start:int,end:int=None,step:int=1):
        self.step = step;
        if end == None : 
            self.start = 0;
            self.end = start;
        else : 
            self.start = start;
            self.end = end;



    # __iter__ method must return self
    def __iter__(self):return self;

    # __next__ method return the next iteration data
    def __next__(self):
        if self.start < self.end :
            temp = self.start;
            self.start += self.step; 
            return temp;
        else :
            # if iteration complete then raise StopIteration error 
            raise StopIteration;
        

# say hello from 0 to 4
print(">>> say hello from 0 to 4 <<<");
for i in my_range(5):
    print("Hello, Mr.",i);

print("\n>>> say ok for every even number between 10 and 20 <<<");
for i in my_range(10,20,2):
    print("Everythink ok : ",i);
