class Greeting :
    def __init__(self,name:str):
        self.name = name;

    # __repr__ return the output
    def __repr__(self)->str:
        return "Hello, " + self.name + "!";

if __name__ == "__main__" :
    me = Greeting("Anonymous");
    print(me);