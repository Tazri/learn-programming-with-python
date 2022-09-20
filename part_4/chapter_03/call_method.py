class Person:
    # constructor
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
    
    # meke the object callable
    def __call__(self):
        print("name :",self.name);
        print("age :",self.age);
        
me = Person("Anonymo","99");

# call the object
me();