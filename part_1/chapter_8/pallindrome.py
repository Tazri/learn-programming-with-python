name = input("Please enter the text : ");
reverse_name = [c for c in name];
reverse_name.reverse();

if name == "".join(reverse_name) : print("The name is pallindrome.");
else : print("The name is not pallindrome.");