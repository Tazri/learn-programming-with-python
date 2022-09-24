Chapter 05 : Some Library of Python
==============================

***Program : sum max and min***
```bash
>>> li = [1,3,5,6]
>>> sum(li)
15
>>> max(li)
6
>>> min(li)
1
>>> 
KeyboardInterrupt
>>> 
```

***Program : pow and abs***
```bash
>>> pow(2,4)
16
>>> abs(-1)
1
>>> abs(1)
1
```

***Program : divmod***
```bash
>>> # division result
>>> 10 // 3
3
>>> # remainder
>>> 10 % 3
1
>>> # divmod return division result and remainder
>>> divmod(10,3)
(3, 1)
>>> 
```

***Program : bin oct and hex***
```bash
>>> n = 10
>>> bin(n) # convert to binary (2)
'0b1010'
>>> oct(n) # convert to octal (8)
'0o12'
>>> hex(n) # convert to hexadecimal (16)
'0xa'
>>> n = -10
>>> bin(n)
'-0b1010'
>>> oct(n)
'-0o12'
>>> hex(n)
'-0xa'
>>> 
```

***Program : reversed()***
```bash
>>> li = [3, 2, 1]
>>> reversed(li) # reversed the list and return iterative 
<list_reverseiterator object at 0x7fb789bd3c10>
>>> [x for x in reversed(li)] # list conprehension
[1, 2, 3]
>>> list(reversed(li)) # convert reversed iterativable object to list
[1, 2, 3]
>>> # reversed string using reversed() function
>>> s = "Python"
>>> reversed(s)
<reversed object at 0x7fb789bd3c10>
>>> "".join(reversed(s)) # 
'nohtyP'
>>> 
```

***Program : math.round()***
```bash
>>> import math
>>> math.pi
3.141592653589793
>>> round(math.pi,2)
3.14
>>> round(math.pi,3)
3.142
>>> round(math.pi,4)
3.1416
>>> 
```

***Program : ord() and chr***
```bash
>>> ord('d')
100
>>>
>>> for item in ['a','b','A','B','0','9']:
...     ord(item) # convert character to ascii number
... 
97
98
65
66
48
57
>>> for item in [97, 98,66,48,57]:
...     chr(item) # convert number to ascii character
... 
'a'
'b'
'B'
'0'
'9'
>>> 
```

***Program : any() and all()***
```bash
>>> cond1, cond2, cond3, cond4, cond5, cond6 = 1== 1, 2 > 1, 3 < 4 , 1 == 0, 2 < 1, 3 > 4
>>> all([cond1, cond2, cond3]) # return True if every item is True otherwise return False
True
>>> all([cond1, cond2, cond3, cond4])
False
>>> any([cond4, cond5, cond6]) # return True if any item is True otherwise return False
False
>>> any([cond1, cond2, cond3, cond4, cond5, cond6])
True
>>> 
```

***Program : enumerate()***
```bash
>>> # enumerate return key value pair tuples list where first item of tuple is index and secound item is list item.
>>> prog_lang = ['C', 'C++','Python','Java','Go']
>>> enumerate(prog_lang,start=1) # start is by default 0
<enumerate object at 0x7fb789b332c0>
>>> [x for x in enumerate(prog_lang,start = 1)]
[(1, 'C'), (2, 'C++'), (3, 'Python'), (4, 'Java'), (5, 'Go')]
>>> list( enumerate(prog_lang,start = 1) )
[(1, 'C'), (2, 'C++'), (3, 'Python'), (4, 'Java'), (5, 'Go')]
>>> 
```

***Program : zip()***
```bash
>>> for item in zip([1,2,3],['one','two','three']):
...     item
... 
(1, 'one')
(2, 'two')
(3, 'three')
>>> 
>>> # zip take a iterable object and return their value in tuples by serial.
>>>
>>> li0 = ['one','two','three','four']
>>> li1 = [1,2,3,4]
>>> li2 = [1,4,9,16]
>>> li3 = [1,8,27, 64]
>>> list(zip(li0,li1,li2,li3))
[('one', 1, 1, 1), ('two', 2, 4, 8), ('three', 3, 9, 27), ('four', 4, 16, 64)]
>>> 
```

***Program : map()***
```bash
>>> # map take funciton and a list, and pass the all item one by one in funciton and store the function return value and make them iterable value and return it.
>>> map(int,['1', '10', '100'])
<map object at 0x7fb789b1bfa0>
>>> list(map(int,['1', '10', '100']))
[1, 10, 100]
>>> list(map(int,'1 10 100'.split()))
[1, 10, 100]
>>> 
>>> 
>>> sqr = map(lambda x : pow(x,2),[1,2,3])
>>> list(sqr)
[1, 4, 9]
>>> 
>>> names = ["anonymo", 'sirius', 'alyath']
>>> names = list(map(lambda x : x.title(),names))
>>> names
['Anonymo', 'Sirius', 'Alyath']
>>> 
>>> def add_100(x) : return x + 100;
... 
>>> list(map(add_100,[1,2,3]))
[101, 102, 103]
>>> 
```


***Program : filter()***
```bash
>>> nums = list(range(1,21))
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> even_nums = filter(labda x : x % 2 == 0, nums)
  File "<stdin>", line 1
    even_nums = filter(labda x : x % 2 == 0, nums)
                             ^
SyntaxError: invalid syntax
>>> even_nums = filter(lambda x : x % 2 == 0, nums)
>>> even_nums
<filter object at 0x7fb789b1bf10>
>>> list(even_nums)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> 
```

***Program : eval()***
```bash
>>> # eval -> expression evaluation
>>> x = 1
>>> eval('x+1')
2
>>> x = 100
>>> eval('divmod(10,3)')
(3, 1)
>>> eval('4 > 3 and 3 > 2')
True
>>> 
```

***Program : exec()***
```python
'''
# exec() function execute whole python program where eval() execuate just a expression. 
# 'sample.py' content : 
name = "Anonymo";
print("Hello Anonymo!");
'''

with open('./sample.py','r') as file : 
    content = file.read();
    exec(content);
```

output : 
```bash
Hello Anonymo!
```

<hr />
<br />

[< Go Back](./../part_4.md)
------------------------------