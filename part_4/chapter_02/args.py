def give_me_tuple(*args):
    print(type(args));
    print(args);

give_me_tuple(2,4,65,7,3);


def hello_every_one(g,*names):
    print("\n");
    for name in names:
        print(g+",",name);
        
hello_every_one("Hi","Anonymous","Sirius","Alpha");

# don't do below code. it dose not work
# hello_every_one(names=("Trition","lion","throw"),g="hello")
# hello_every_one(names="Trition","lion","throw",g="hello")