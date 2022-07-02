string = input("Please write something : ");
letter = "abcdefghijklmnopqrstuvwxyz";
digit = '0123456789';
lc = uc = dc = oc = "";

for c in string : 
    if c in letter : lc += c;
    elif c in letter.upper() : uc += c;
    elif c in digit : dc += c;
    else : oc += c;

uc and print(uc);
lc and print(lc);
dc and print(dc);
oc and print(oc);