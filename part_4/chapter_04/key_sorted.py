fruits = [
    ('benana',4),
    ('apple',10),
    ('mango',21),
    ('guava',2),
]

def compare_key(item):
    return item[1];

print("> fruits ");
print(sorted(fruits))

print("> sorted(fruits,key=compare_key) : ");
print(sorted(fruits,key=compare_key));