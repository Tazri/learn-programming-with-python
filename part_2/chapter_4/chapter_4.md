Chapter 4 : Request Module and Creating File
--------------------------------------------

## **requests**
Here explain requests module with syntax :
```python
import requests 

response = requests.get(url) # send the resuest to url and get response to store vairable

response = requests.post(url,info_data) # send the post request to url with info_data. Here info data must be a dictionary.

response.ok # return true if request was successy full gone

response.status_code # 200 for success and 404 for not found

response.reason # write 'not found' for 404 and 'ok' for 200 status_code

response.text # contain the string what caught from server.

response.conent # contain the binary what caught from server
```

<hr />

## **open**
Here explain **open** function and **file** object by syntax : 

```python
file = open(file_name_with_url,mode); # for open the file in mode

with open(file_name_with_url,mode) as file :
    # we do anything with file in with block.
    # after with block file is atomatic close.

file.close() # for close the file. after that we can use any task of file

file.write(content_or_text) # write the file in string or binary mode.
```

**File Mode :**
| Mode  | Explain                                 |
| ----- | --------------------------------------- |
| r     | Read mode                               |
| r+    | Reading and Write mode                  |
| w     | Write mode                              |
| w+    | Write and Reading mode                  |
| rb    | Reading only binary format              |
| rb+   | Reading and Writing only binary format  |
| wb    | Writing binary format mode              |
| wb+   | Writing and Reading only binary format  |
| a     | Append mode                             |
| a+    | Appending and Reading mode              |
| ab    | Appending only binary format            |
| ab+   | Appending and Reading only binary format|

<hr />

## **sys**
Here explain some **sys** module function and attribute with syntax : 
```python
import sys 

sys.argv # return the list of command line arguments
# where first element is file name

sys.exit() # close the whole program.

sys.exit(string) # close the whole program and print the string.

sys.exit(1) # close the program and inform the os that program was successfully close.

sys.exit(0) # close the program and inform the os that program was not successfully close.
```

<hr />

## **os**
**os** module contain about the system information and some file information. **os.path.realpath()** return the file absotule path.

<hr />
<br /> <br />

## Let's write some program with open, request, os, sys module : 

<br /> 

**Send request the server and get the response in response variable by requests module.**
```bash
>>> import requests
>>> url = "http://subeen.com/allposts/"
>>> response = requests.get(url)
>>> type(response)
<class 'requests.models.Response'>
```

**See the details about response variable by dir function.**
```bash
>>> dir(response)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
>>> 
```

**See the some resposne attribute.**
```bash
>>> response.ok
True
>>> response
<Response [200]>
>>> response.status_code
200
>>> response.reason
'OK'
>>> 
```

**Send the bed request by requests module and see response ok, status_code and reason attribut.**
```bash
>>> res = requests.get("http://dimikcomputing.com/abc.html")
>>> res.ok
False
>>> res.reason
'Not Found'
>>> res.status_code
404
>>> 
```

**Send the request to http://example.com by requests module and see the response text by text attribute.**
```bash
>>> res = requests.get("http://example.com")
>>> res.ok
True
>>> res.text
'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
>>> 
```

**Open the test.text file and write something and close it.**
```bash
>>> fp = open("test.text","w")
>>> fp.write("This file was created using Python!")
35
>>> fp.close()
>>> 
```

**See what is return open function in details.**
```bash
>>> type(fp)
<class '_io.TextIOWrapper'>
>>> fp
<_io.TextIOWrapper name='test.text' mode='w' encoding='UTF-8'>
>>> 
```

**Try to write something in closed file and get error.**
```bash
>>> fp.close()
>>> fp.write("hello,again")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> 
```

**Open the file using with keyword and write something inside with block.**
```bash
>>> with open("test.text","w") as f :
...     f.write("Hello, Python\n")
... 
14
>>> f
<_io.TextIOWrapper name='test.text' mode='w' encoding='UTF-8'>
>>> f.write("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> 
```

***Program : webpage.py***
```python
import requests

url = "http://dimikcomputing.com"

response = requests.get(url);

if response.ok :
    with open("dimik.html","w") as f :
        f.write(response.text);
        print("File write successfully.");
else :
    print("Request Can not ok.");
    
```

***Output : webpage.py***
```bash
File write successfully.
```

***dimik.html file open by browser.***

![dimik.html](./../../asset/web/dimik.html.png)

***Program : google.py***
```python
```

***Output : google.py***
```bash
$python3 google.py 
>> File was write successfully!! <<
>> FILE LOCATION IS : 
/home/tazri/Documents/work-place/python/learn-programming-with-python/part_2/chapter_4/dimik.html
$Opening in existing browser session.
```

***Program : download_img.py***
```python
import requests

url = "https://wallpaperaccess.com/full/7885293.jpg";
res = requests.get(url);

if res.ok :
    # open the file wb mean write binary mode for writing img not w mean write mode
    with open("spiderman.jpg","wb") as file :
        # file.write(res.text); don't do it. text contain string 
        file.write(res.content); # content contain binary
        print(">> File was write successfully! <<");

else :
    print(">> Request was bed :( <<");
```

***Output : download_img.py***
```bash
>> File was write successfully! <<
```

***Program : add.py***
```python
import sys

# sys.argv return the list of command line argument
print(sys.argv);
print(type(sys.argv));

# get arguments
arg = sys.argv

a = arg[1];
b = arg[2];

print(int(a) + int(b));
```

***Output : add.py***
```bash
['add.py', '10', '30']
<class 'list'>
40
```

***Program : imgdownloader.py***
```python
import requests,sys

url = sys.argv[1];
filname = sys.argv[2];

res = requests.get(url);


if res.ok :
    with open(filname,"wb") as file :
        file.write(res.content);
        print(">> IMAGE WAS DOWNLOAD SUCCESSFULLY <<");

else :
    print(">> URL PROBLEM <<");
```

***Output : imgdownloader.py***
```bash
$python3 imgdownlaoder.py https://cdn.wallpapersafari.com/37/50/yh3wT8.jpg spiderman_dark_and_red.jpg
>> IMAGE WAS DOWNLOAD SUCCESSFULLY <<
```

***Program : cpbook_downloader.py***
```python
import sys,requests

base_url = "http://subeen.com/download/";

info_data = {
    "name" : "Subeen",
    "email" : "book@subeen.com",
    "country" : "Bangladesh"
}

url = base_url + "process.php";

# send the request
res = requests.get(url);

if not res.ok :
    sys.exit(">> Error downloading the file. :( <<");


with open("book.pdf","wb") as file :
    file.write(res.content);

print(">> Book Download Successfully :) <<");
```

***Output : cpbook_downloader.py***
```bash
$python3 cpbook_downloader.py 
>> Book Download Successfully :) <<
```

[< Go Back](./../part_2.md)
---------------------------