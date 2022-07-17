import re

file_url = "./text/book.html"

with open(file_url,'r') as file :
    text = file.read();


regex = r'<div class="book-cover">.*<a href="(.*?)">[\.\s]*<img src="(.*?)">.*?<h2 class="sd-title">.*<a .*?>(.*?)<';

compiler = re.compile(regex,re.S);

text = compiler.findall(text);

print(text);