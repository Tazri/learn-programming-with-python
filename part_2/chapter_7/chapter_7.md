Chapter 7 : Regular Expression
==============================


## **Regex**
**Here all syntax meaning in table :**
| syntax | meaning                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------|
| .      | dot(.) mean any character except new line. If S flag use then new line character include.           |
| \\w    | any single letter a to z.                                                                           |
| \\d    | any single digit 0 to 9.                                                                            |
| \\s    | single space.                                                                                       |
| []     | any character inside [] them.                                                                       |
| ()     | select only inside the character () in them.                                                        |
| +      | .+,\\w+,\\d+,\\s+ mean only one or more than one.                                                   |
| *      | .\*,\\w\*,\\d\*,\\s\* mean none or more exist one or more than one.                                 |
| ?      | .?,\\w?,\\d?,\\s? mean if it exist, only one or none.                                               |
| {}     | {} spacify the character how many exist by them.                                                    |
| $      | last of the line must be multiline flag on.                                                         |
| ^      | first of the line must be multiline flag on.                                                        |



**All flag and meaning :**
| flag | meaning                                                                                               |
|------|-------------------------------------------------------------------------------------------------------|
| g    | select not single. globally select.                                                                   |
| i    | select case insensitive way.                                                                          |
| m    | if m flag on then we use $ and ^ syntax.                                                              |
| s    | if s flag on then dot(.) mean all type of character include new line.                                 |

<hr />

## **re**
**re** is python module for work with regex. Here explain re with syntax : 
```python
import re

# here all pattern mean regex, must of the case it write row string way like r'regex'

match = re.search(pattern,string,flag); # return the first sub string if matching with pattern otherwise return None
match.group() # return the matching sub str if it matcing otherwise throw error.

re.findall(pattern,string); # return the list of matcing substring form string with pattern otherwisr return []


cpat = re.compile(pattern,flat); # return compiler
cpat.findall(string); # now pattern not necessary to give again.
cpat.search(string); # now pattern not necessary to give again.


re.sub(pattern,replacing_text_or_pattern,string,flag); # return a string with replacing with string or pattern what it give 2nd parameter. 

# flag in re
re.I, re.IGNORECASE; # use for on i flag
re.S; # use for on s flag.
re.MULTILINE # use for on m flag

# using multiple flag 
re.search(pattern,s,re.I|re.S|re.MULTILINE);
```

<hr />

## **Creating Directory.**
```python
import os

os.mkdir(name); # create directory if not exist name otherwise throw error
```
<hr />

<br />

## Let's write some program with regex :

**Sperate the all country in the list which is end with land.**
```bash
>>> s = "Afganistan, America, Bangladesh, Canada, Denmark, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"
>>> countries = s.split(",")
>>> countries
['Afganistan', ' America', ' Bangladesh', ' Canada', ' Denmark', ' England', ' Greenland', ' Iceland', ' Netherlands', ' New Zealand', ' Sweden', ' Switzerland']
>>> li = [item for item in countries if item.endswith("land")]
>>> li
[' England', ' Greenland', ' Iceland', ' New Zealand', ' Switzerland']
>>> 
```

**Sperate the all country in the list which is end with land or lands.**
```bash
>>> countries
['Afganistan', ' America', ' Bangladesh', ' Canada', ' Denmark', ' Greenland', ' Iceland', ' Netherlands', ' New Zealand', ' Sweden', ' Switzerland']
>>> li = [item for item in countries if item.endswith('land') or item.endswith('lands')]
>>> li
[' Greenland', ' Iceland', ' Netherlands', ' New Zealand', ' Switzerland']
>>> 
```

**Use search function of re module.**
```bash
>>> import re
>>> match = re.search('Bangla','Bangladesh')
>>> match
<re.Match object; span=(0, 6), match='Bangla'>
>>> match.group()
'Bangla'
>>> match = re.search('desh','Bangladesh')
>>> match.group()
'desh'
>>> match = re.search('des','Bangladesh')
>>> match.group()
'des'
>>> match = re.search('dets','Bangladesh')
>>> match.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> match
>>> type(match)
<class 'NoneType'>
>>> match is None
True
>>> 
```

**Use search function of re module and use dot(.) in regular expression.**
```bash
>>> import re
>>> s = "Bangladesh"
>>> match = re.search('.',s)
>>> match.group()
'B'
>>> match = re.search('B.n',s)
>>> match.group()
'Ban'
>>> match = re.search('B.n...',s)
>>> match.group()
'Bangla'
>>> s = 'Bangladesh is our homeland'
>>> match = re.search('...........',s)
>>> match.group()
'Bangladesh '
>>> 
```

**Use \w in regular expression.**
```bash
>>> import re
>>> s = "Bangladesh is our homeland"
>>> match = re.search("o\w\w",s)
>>> match.group()
'our'
>>> match = re.search("i\w\w",s)
>>> print(match)
None
```

**Use \w+ in regular expression.**
```bash
>>> import re
>>> s = "Bangladesh is our homeland"
>>> match = re.search('B\w+h',s)
>>> match.group()
'Bangladesh'
>>> 
```

**Use .+ in regular expression.**
```bash
>>> import re
>>> s = "Bangladesh is our homeland"
>>> match = re.search('B.+h',s)
>>> match.group()
'Bangladesh is our h'
>>> 
```

**Use .+? in regular expression.**
```bash
>>> import re
>>> s = "Bangladesh is our homeland"
>>> match = re.search('B.+?h',s)
>>> match.group()
'Bangladesh'
>>> 
```

**Use \d+ in regular expression.**
```bash
>>> import re
>>> text = "Phone number : 01711101001."
>>> match = re.search('\d+',text)
>>> match.group()
'01711101001'
>>> 
```

**Use \d+ in  regular expression again.**
```bash
>>> import re
>>> text = "house number : 5, phone number : 01711101001."
>>> match = re.search("\d+",text)
>>> match.group()
'5'
>>> 
```

**Use \d{11} in regular expression.**
```bash
>>> import re
>>> text = "house number : 5, phone number : 01711101001."
>>> match = re.search('\d{11}',text)
>>> match.group()
'01711101001'
>>> 
```

**Use * and \s in regular expression.**
```bash
>>> import re
>>> text = "house number : 5, phone number : 017 11101001."
>>> match = re.search('\d{3}\s*\d{8}',text)
>>> match.group()
'017 11101001'
>>> 
```

**Use findall method of re mdoule.**
```bash
>>> import re
>>> text = "multiple phone number, 01711111111, 01811111111, 01910101010, 00000000000 123-123"
>>> result = re.findall(r'\d{3}\s*\d{8}',text)
>>> result
['01711111111', '01811111111', '01910101010', '00000000000']
>>> 
```

**Use [] in regular expression.**
```bash
>>> import re
>>> text = "multiple phone number, 01711111111, 01811111111, 01910101010, 00000000000 123-123"
>>> result = re.findall(r'01[56789]\s*\d{8}',text)
>>> result
['01711111111', '01811111111', '01910101010']
>>> 
```

**Use ^ and $ symbol in regular expression.**
```bash
>>> import re
>>> s = "Bangla english bangla"
>>> re.findall(r'english',s);
['english']
>>> re.findall(r'english$',s);
[]
>>> re.findall(r'^Bangla',s);
['Bangla']
>>> re.findall(r'^bangla$',s);
[]
>>> re.findall(r'bangla$',s);
['bangla']
>>> 
```

**Case Ignore flag.**
```bash
>>> import re
>>> s = "Bangla english Bangla"
>>> re.findall(r'bangla$',s)
[]
>>> re.findall(r'bangla$',s,re.IGNORECASE)
['Bangla']
>>> re.findall(r'bangla$',s,re.I)
['Bangla']
>>> 
```

**Use re.MULTILINE flag.**
```bash
>>> import re
>>> with open('./text/file.txt','r') as f :
...     text = f.read()
... 
>>> text
'Bangladesh is our country.\nBangla is our language.\nPython is a programming language.'
>>> re.findall(r'^.*?',text)
['', 'B']
>>> re.findall(r'^.*?$',text)
[]
>>> re.findall(r'^.*?$',text,re.MULTILINE)
['Bangladesh is our country.', 'Bangla is our language.', 'Python is a programming language.']
>>> 
```

**Use first bracket.**
```bash
>>> s = '<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominul</li>'
>>> result = re.findall(r'<li>(.*?)</li>',s)
>>> result
['Tamim', 'Shakib', 'Mahmudullah', 'Mominul']
>>> 
```


**re.compile to create pattern.**
```bash
>>> import re
>>> text = "This is line 1. Date is 2017/06/01. And there is another date : 2017-07-01. The third and final date is 2017/08/30."
>>> import re
>>> pat = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
>>> pat
re.compile('(\\d{4})[-/](\\d{2})[-/](\\d{2})')
>>> type(pat)
<class 're.Pattern'>
>>> result = pat.findall(text)
>>> result
[('2017', '06', '01'), ('2017', '07', '01'), ('2017', '08', '30')]
>>> 
```

**More about re.compile(pattern)**
```bash
>>> dir(pat)
['__class__', '__class_getitem__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'findall', 'finditer', 'flags', 'fullmatch', 'groupindex', 'groups', 'match', 'pattern', 'scanner', 'search', 'split', 'sub', 'subn']
>>> 
>>> text2 = "New date : 2017/06/15"
>>> result = pat.findall(text2)
>>> result
[('2017', '06', '15')]
>>> 
```

**Use re.sub method.**
```bash
>>> import re
>>> s = 'Abcd 1234 - 33'
>>> result = re.sub(r'\d','0',s)
>>> result
'Abcd 0000 - 00'
>>> 
```

**Use re.sub and changing date format.**
```bash
>>> import re
>>> s = '22/07/2017, 20/01/2017, 01/01/2018'
>>> new_s = re.sub('(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',s)
>>> new_s
'2017-07-22, 2017-01-20, 2018-01-01'
>>> 
```

**Use \g<> in re.sub to changing date format in string.**
```bash
>>> import re
>>> s = '22/07/2017, 20/01/2017, 01/01/2018'
>>> new_s = re.sub('(\d{2})/(\d{2})/(\d{4})',r'\g<3>-\g<2>-\g<1>',s)
>>> new_s
'2017-07-22, 2017-01-20, 2018-01-01'
>>> 
```

***Program : criketer.py***
```python
import re

file_path = './text/cricater.html';

with open(file_path,'r') as file :
    text = file.read();

# remove the all \n and space 
text = text.replace('\n','');
text = re.sub(r'\s','',text)

# select the all country with player
text = re.findall(r'<li>(.*?)<ol><li>(.*?)</li><li>(.*?)</li>',text)

for c,p1,p2 in text :
    print(c+" - "+p1+", "+p2);
```

***Output : cricater.py***
```bash
$python3 criketer.py 
Australia - StevenSmith, DavidWarner
Bangladesh - MashrafeMortaza, TamimIqbal
England - EoinMorgan, JosButtler
```

**Try to caught email by \\w+@\\w+.\\w+ pattern.**
```bash
>>> import re
>>> text = "Email our feedback here : book@subeen.com book@subeen thank you"
>>> result = re.findall('\w+@\w+.\w+',text)
>>> result
['book@subeen.com', 'book@subeen thank']
>>> 
```

**Try to caguht email by \\w+@\\w+\\.\\w+ pattern.**
```bash
>>> import re
>>> text = "Email our feedback here : book@subeen.com book@subeen thank you"
>>> result = re.findall("\w+@\w+\.\w+",text)
>>> result
['book@subeen.com']
>>> 
```

**Another example of finding gmail.**
```bash
>>> text = "Email your feedback here : book@subeen.com py.book@subeen.com book_py@subeen.com thank you"
>>> result = re.findall(r'(\w+@\w+[.]\w+)',text)
>>> result
['book@subeen.com', 'book@subeen.com', 'book_py@subeen.com']
>>> 
```

**Another example of finding gmail.**
```bash
>>> text = "Email your feedback here : book@subeen.com py.book@subeen.com book_py@subeen.com thank you"
>>> result = re.findall(r'([.\w]+@\w+[.]\w+)',text)>>> result
['book@subeen.com', 'py.book@subeen.com', 'book_py@subeen.com']
>>> 
```

**Select complex email by regular expression.**
```bash
>>> text = "book at subeen.com, book At subeen.com, book (at) subeen dot com, book [at] subeen [dot] com"
>>> text = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+','@',text,flags=re.I)
>>> text
'book@subeen.com, book@subeen.com, book@subeen dot com, book@subeen [dot] com'
>>> 
```

**Seleclt complex email by regular expression.**
```bash
>>> text
'book@subeen.com, book@subeen.com, book@subeen dot com, book@subeen [dot] com'
>>> text = re.sub(r'\s+[\(\[]*\s*dot\s*[\)\]]*\s+','.',text)
>>> text
'book@subeen.com, book@subeen.com, book@subeen.com, book@subeen.com'
>>> 
```

***Program : bk.py***
```python
import re

file_url = "./text/book.html"

with open(file_url,'r') as file :
    text = file.read();


regex = r'<div class="book-cover">.*<a href="(.*?)">[\.\s]*<img src="(.*?)">.*?<h2 class="sd-title">.*<a .*?>(.*?)<';

compiler = re.compile(regex,re.S);

text = compiler.findall(text);

print(text);

```

***Output : bk.py***
```bash
$python3 bk.py 
[('http://dimik.pub/book/525/java-web-programing-by-anm-bazlur-rahman', 'http://dimik.pub/wp-content/uploads/2020/02/javaWeb.jpg', 'জাভা ওয়েব প্রোগ্রামিং')]
```

***Program : small_project.py***
```python
import os,re
import requests
import sys

def create_dir(name) : # this function for create directory
    try :
        os.mkdir(name);
    except FileExistsError :
        print(name,"already exists");


def get_site_html(url) : # send the request and get the url
    response = requests.get(url);

    if response.ok :
        return response.text;
    else :
        sys.exit(">>> Bad Request <<<");


def download_img(img_url,file_name) : # download img
    print("> Downloading......",img_url);
    r = requests.get(img_url);

    with open(file_name,'wb') as f :
        f.write(r.content); 


def get_books_from_html(regex,html) :
    return re.findall(regex,html);


def get_dir_name(regex,url) : # extract the dir name form url
    result = re.findall(regex,url);
    return "_".join(result[0]);


def process() : # main process
    # nesecarry variable
    main_dir = "dimik_pub";
    site_url = "http://dimik.pub";
    books_regex = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<',re.S);
    folder_name_regex = re.compile(r'book/(\d+)/(\w+)-(\w+)-');

    # create main dir
    create_dir(main_dir);

    # create page content
    page_content = get_site_html(site_url);
    books = get_books_from_html(books_regex,page_content)
    

    # create folder for every book 
    for book in books :
        # extract the book information
        name = book[2];
        url = book[0];
        img_url = book[1];

        # book folder
        dir_name = main_dir + '/' + get_dir_name(folder_name_regex,url);
        create_dir(dir_name);

        # create info text
        file_name = dir_name+"/"+"info.text"
        with open(file_name,'w') as file :
            file.write(name+'\n');
            file.write(url);

        img_file_name = dir_name+"/" + "image.jpg";
        download_img(img_url,img_file_name);


if __name__ == "__main__" :
    process();
    
```

***Output : small_project.py***
```bash
$python3 small_project.py 
dimik_pub already exists
dimik_pub/627_learn_programming already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2022/01/Asset-5.png
dimik_pub/629_programming_contest already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2022/01/271685794_1313970962442371_1405864604028126740_n.jpg
dimik_pub/588_object_oriented already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2021/03/OOP-outlined_Front-Cover.png
dimik_pub/572_ethical_hacking already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2021/01/ethical_hack.png
dimik_pub/555_preparation_for already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2021/01/IMG-20210114-WA0004.jpg
dimik_pub/553_php_web already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2021/01/IMG-20210114-WA0003-1.jpg
dimik_pub/525_java_web already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2020/02/javaWeb.jpg
dimik_pub/475_coding_interview already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2020/01/codingInterview.png
dimik_pub/456_introduction_to already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2019/05/comb-2-1.jpg
dimik_pub/439_kritikothon_story already exists
> Downloading...... http://dimik.pub/wp-content/uploads/2019/03/kriti-kothon-front-cover-350x450.jpg
```

[< Go back](./../part_2.md)
---------------------------