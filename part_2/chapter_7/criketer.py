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