lines = [
    "This is first line.",
    "This is secound line.",
    "This is third line."
]

file_name = "./text/demo.txt";

# write the line in the file
with open(file_name,"w") as file :
    for i in range(len(lines)) :
        file.write(lines[i]+"\n");


# read the line
print(">> Inside the file",file_name," :");
# read the file by read function 
with open(file_name,"r") as file :
    content = file.read();
    print(content);


# read the file by readlines
with open(file_name,'r') as file :
    print('\n>> All line in list :');
    file_lines = file.readlines()
    print(file_lines)


# read the file by for loop 
with open(file_name,'r') as file : 
    print("\n>> Read the line by for loop : ");
    for line in file :
        print(line);
