Chapter 8 : Work With String
============================

## **Trutle More**
Here explain one more turtle method. This is **textinput**. 

### **textinput**
**turtle.textinput** is use for input from user by graphical user interface. Syntax is : 
```python
import turtle
input_text = turtle.textinput("window_name","display_text_no_the_input_box");
```
<hr>

## **String Method**
All string method return a new string always. Here some string method with explaination : 

| Method           | Explain                                                                                   |
|------------------|-------------------------------------------------------------------------------------------|
| len(string)      | return length of string                                                                   |
| .find(substr)    | return position of substring otherwise return -1                                          |
| .replace(t,sstr) | return new string with replacing t with sstr                                              |
| .strip()         | return new string with erasing space both side, right in starting and left in ending.     |
| .lstrip()        | return new string with erasing left side space.                                           |
| .rstrip()        | return new string with reasing right side space.                                          |
| .upper()         | return uppercase string.                                                                  |
| .lower()         | return new string with convert every character to lowercase                               |
| .upper()         | return new string with convert every character to uppercase                               |
| .capitalize()    | return new string with convert first character of string                                  |
| .split(c)        | return new list of string which dividing by c. space is by default value of c             |
| .count(substring)| return number of total substring exist in string.                                         |
| .startswith(s)   | return True if string start with s otherwise return False.                                |
| .endswith(s)     | return True if string end with s otherwise return False.                                  |


<hr>


**Let's do some program with string method :**
----------------------------------------------

**Use len function on string.**
```bash
>>> s = "hello"
>>> len(s)
5
>>> l = len(s)
>>> l
5
>>> s = ''
>>> len(s)
0
>>> 
```

**Use escape Character.**
```bash
>>> s = "Dimik's"
>>> print(s)
Dimik's
>>> s = 'Dimik\'s'
>>> s
"Dimik's"
>>> 
```

**Try to access invlid index and get error.**
```bash
>>> country = "Bangladesh"
>>> country[0]
'B'
>>> country[1]
'a'
>>> country[2]
'n'
>>> country[8]
's'
>>> country[9]
'h'
>>> country[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> >>> s = "Dimik's"
  File "<stdin>", line 1
    >>> s = "Dimik's"
    ^
SyntaxError: invalid syntax
```

**For loop on string.**
```bash
>>> country = "Bangladesh"
>>> for c in country : 
...     print(c)
... 
B
a
n
g
l
a
d
e
s
h
>>> 
```

**Try to changing element of string and get error.**
```bash
>>> country = "Bangladesh"
>>> country[0] = 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 
```

**String Concatination**
```bash
>>> country = "Bangla" + "desh"
>>> country
'Bangladesh'
>>> x = '50' +'5'
>>> x
'505'
>>> 
```

**Use find function on string.**
```bash
>>> country = "Bangladesh"
>>> country.find("Ban")
0
>>> country.find("ang")
1
>>> country.find("Bangla")
0
>>> country.find("Bengla")
-1
>>> country.find("desh")
6
>>> 
```

**Using replace function on string.**
```bash
>>> country = "North Korea"
>>> new_country = country.replace("North","South")
>>> new_country
'South Korea'
>>> country
'North Korea'
>>> text = "this is a test. this is another test. this is final test."
>>> new_text = text.replace("this","This")
>>> new_text
'This is a test. This is another test. This is final test.'
>>> text
'this is a test. this is another test. this is final test.'
>>> 
``` 

**Use lstrip, rstrip and strip function on string.**
```bash
>>> text = " this is a string. "
>>> text
' this is a string. '
>>> text.lstrip()
'this is a string. '
>>> text.rstrip()
' this is a string.'
>>> text.strip()
'this is a string.'
>>> 
```

**Use upper, lower and  capitalize function on string.**
```bash
>>> s = "Bangadesh"
>>> s.upper()
'BANGADESH'
>>> s.lower()
'bangadesh'
>>> s.capitalize()
'Bangadesh'
>>> s = "hello"
>>> s.capitalize()
'Hello'
>>> 
```

**Use split function on string.**
```bash
>>> str = "I  am a programmer."
>>> words = str.split()
>>> words
['I', 'am', 'a', 'programmer.']
>>> for word in words : 
...     print(word)
... 
I
am
a
programmer.
>>> 
```

**Use count on string.**
```bash
>>> str = "This is"
>>> str.count("is")
2
```

**Use  startswith and endswith function on string.**
```bash
>>> s = "Bangladesh"
>>> s.startswith("Ban")
True
>>> s.startswith("ban")
False
>>> s.endswith("desh")
True
>>> s.endswith("h")
True
>>> 
```

***Program : hello.py***
```python
import turtle

name = turtle.textinput("name","What is your name?");
name = name.lower()

if name.startswith("mr") : 
    print("Hello Sir, How are you ?");
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms") :
    print("Hello Madam, How are you ?");
else : 
    name = name.capitalize();
    str = "Hi " + name + "! How are you ?";
    print(str);

turtle.exitonclick();
```

***Output : hello.py***
```bash
Hi Tazri! How are you ?
```

***Program : find.py***
```python
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
```

***Output : find.py***
```bash
HT
elloestgood
123123
 !  , .
```
***Program : swap_string.py***
```python
text = input("Enter the text : ");
length = len(text) ;
swap_text = '';

if length & 1 : length -= 1;

for i in range(0,length,2) :
    swap_text += text[i+1];
    swap_text += text[i];

print(swap_text);
```

***Output : swap_string.py***
```bash
Enter the text : bangladesh
abgnaledhs
```

***Program : pallindrome.py***
```python
name = input("Please enter the text : ");
reverse_name = [c for c in name];
reverse_name.reverse();

if name == "".join(reverse_name) : print("The name is pallindrome.");
else : print("The name is not pallindrome.");
```

***Output : pallindrome.py***
```python
Please enter the text : madam
The name is pallindrome.
```

[< Go Back](./../part_1.md)
---------------------------