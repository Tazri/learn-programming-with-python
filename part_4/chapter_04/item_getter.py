from operator import itemgetter

fruits = [
    ('benana',2),
    ('apple',2),
    ('mango',21),
    ('guava',24),
]

print("> fruits ");
print(fruits)

print("> sorted(fruits,key=compare_key) : ");
print(sorted(fruits,key=itemgetter(1,0)));