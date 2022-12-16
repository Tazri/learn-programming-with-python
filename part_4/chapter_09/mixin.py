class Puzzle:
    def __init__(self,name,price):
        self.name,self.price = name,price;

# create class with classes which class want to add another class
class PuzzlePriceMixin:
    def last_price(self):
        return self.price*0.7;
    
    def details(self):
        print(f"{self.name}(price : {self.price})");

# add the method to Puzzle class
class PuzzleStore(Puzzle,PuzzlePriceMixin):
    pass;

if __name__ == "__main__":
    my_store = PuzzleStore("Rubik Cube",43.444);

    print(f"my_store.last_price : {my_store.price}");
    my_store.details()

'''
ouptut ; 
my_store.last_price : 43.444
Rubik Cube(price : 43.444)
'''