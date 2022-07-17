Chapter 5 : More Task With File and Exception 
=============================================

## **Read File**
Here syntax to read fiel : 
```python
file = open(filename,'r');

# Below all way we can apply one way until close the file

content = file.read(); # return all string inside the file .

lines = file.readlines(); # return a list which contain the all line of inside the file.
 
for line in file :
    line # line is single line of file.
```

<hr />

## **Eception**
Here all about exception : 
```python
try :
    # here statement 
except error_name :
    # this block will run if error_name error is occur in the program.
except error_name_one :
    # this block will run if error_name_one error is occur in the program.
except Exception as e :
    # this program will run if any error occur and above all except can not caught it. here e is the error object.
```

<hr />
<br>

## Let's write some code with read and exception :

***Program : read_file.py***
```python
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

```

***Output : read_file.py***
```bash
>> Inside the file ./text/demo.txt  :
This is first line.
This is secound line.
This is third line.


>> All line in list :
['This is first line.\n', 'This is secound line.\n', 'This is third line.\n']

>> Read the line by for loop : 
This is first line.

This is secound line.

This is third line.

```

***Program : zero_division_error.py*** 
```python
def div(a,b) :
    try :
        return a/b;
    except ZeroDivisionError :
        print("Can not divide by zero.");
    except TypeError :
        print("Unsupported type. Did you use string!");

print(div(10,2));
print(div(3,0));
print(div(9,3));
print(div("12",3));
```

***Output : zero_division_error.py***
```bash
5.0
Can not divide by zero.
None
3.0
Unsupported type. Did you use string!
None
```

***Program : file_error.py***
```python
import io 

filename = "file.txt";
mode = "r";

try :
    with open(filename,mode) as file :
        content = file.read()
        print(content);
except FileNotFoundError :
    print(filename,"not found.Please check if the file's name is correct.");
except io.UnsupportedOperation :
    print("Are you sure", filename,"is readablle ? ");
except Exception as e :
    print(e);
```

***Output : file_error.py***
```bash
file.txt not found.Please check if the file's name is correct.
```

[< Go Back](./../part_2.md)
---------------------------