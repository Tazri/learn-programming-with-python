Chapter 06 : Python and Unicode
===========================

Python can not use **ASCII** code but use **UNICODE**.  In python we see the ascii number character by using **chr()** function Here example : 

***Program : ascii all character***
```bash
>>> for i in range(32,128):
...     print("ascii",i,":",chr(i));
... 
```

We see all ascii character by above code. But We can not explain all character in ascii. This is the why come unicode. So many unicode encoding exist but frquently use utf-8. Here the feature of utf-8 : 

- All code can pointed by utf-8 in unicode. 
- All character not use same byte. Character use necessary byte what needed. Ascii character use 1 byte where bangla use only 2 byte.
- A document using **ASCII** encoding can read by **UTF-8**

Python 3 and after python 3 using unicode for string.  Here some example  : 

```bash
>>> ord('a')
97
>>> ord('ক')
2453
>>> ord('1')
49
>>> ord('১')
2535
>>> chr(2535)
'১'
>>> chr(0x995)
'ক'
>>> chr(97)
'a'
>>> 
```

***Program : bangla variable***
```bash
>>> country = "বাংলাদেশ"
>>> print(country)
বাংলাদেশ
>>> দেশ = "বাংলাদেশ"
>>> print(দেশ)
বাংলাদেশ
>>> 
```

***Program : find***
```bash
>>> দেশ = "বাংলাদেশ"
>>> দেশ.find("দেশ")
5
>>> দেশ.find("বাংলা")
0
>>> 
```

***Program : using bangla in regex***
```bash
>>> import re
>>> 
>>> pat = re.compile(r'(\d+)')
>>> text = "১৯৭১ সালে বাংলাদেশ স্বাধীন হয়।"
>>> re.findall(pat,text)
['১৯৭১']
>>> 
```

***Program : using byte array***
```bash
>>> x = b'this is a byte array'
>>> type(x)
<class 'bytes'>
>>> 
>>> s = x.decode(encoding='utf-8') # utf-8 is default value
>>> s
'this is a byte array'
>>> 
```

<hr />
<br />

[< Go Back](./../part_4.md)
------------------------------