def stylus_text(text,bg:list[int]=None,tg:list[int]=None,styles:list[int]=None):
    start_text = "\033[";
    all_code:list[str] = [];

    if bg != None : 
        all_code.extend(["48","2"]);
        all_code.extend([str(c) for c in bg]);
    
    if tg != None :
        all_code.extend(["38","2"]);
        all_code.extend([str(c) for c in tg]);

    if styles != None : 
        all_code.extend([str(c) for c in styles]);

    string_code = ";".join(all_code);
    start_text += string_code + "m" + text + "\033[0m";

    return start_text;

def print_red(text,end="\n"):
    print(stylus_text(text,tg=[255,0,0]),end=end);

def print_purple(text,end="\n"):
    print(stylus_text(text,tg=(255,0,255)),end=end);

def print_blue(text,end="\n"):
    print(stylus_text(text,tg=(0,0,255)),end=end);

def print_green(text,end="\n"):
    print(stylus_text(text,tg=(0,255,255)),end=end);

def print_white(text,end="\n"):
    print(stylus_text(text,tg=(255,255,255)),end=end);

def print_blink(text,end="\n"):
    print(stylus_text(text,styles=[5,3,1]),end=end);

if __name__ == "__main__":
    print_red("Hello, World!");
    print_green("Do, You know me ?");
    print_white("I am ",end="");
    print_purple("Anonymo!!");

    print_blink("Bye World!!")

'''
output : 
Hello, World!
Do, You know me ?
I am Anonymo!!
Bye World!!
'''