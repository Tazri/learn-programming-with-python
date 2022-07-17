import sys

# sys.argv return the list of command line argument
print(sys.argv);
print(type(sys.argv));

# get arguments
arg = sys.argv

a = arg[1];
b = arg[2];

print(int(a) + int(b));