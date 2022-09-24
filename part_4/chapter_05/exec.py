'''
# 'sample.py' content : 
name = "Anonymo";
print("Hello Anonymo!");
'''

with open('./sample.py','r') as file : 
    content = file.read();
    exec(content);
