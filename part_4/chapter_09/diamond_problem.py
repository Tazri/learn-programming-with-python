# make inheritance like below
#      A
#     / \
#    B   C
#     \ /
#      D


class A:
    def __call__(self):
        print("I am A");
    
    def hello(self):
        print("Hell World! ",end="");
        print(self.__class__.__name__);


class B(A):
    def __call__(self):
        print("I am B");

class C(A):
    def __call__(self):
        print("I am C");

class D(B,C):
    def __call__(self):
        print("I am D");

print("D",D);
print("D.mro() : ",D.mro()); # mro method resulatoin order

print("\n\n");
object_d = D();
object_d.hello();