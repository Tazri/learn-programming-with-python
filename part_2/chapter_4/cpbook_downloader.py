import sys,requests

base_url = "http://subeen.com/download/";

info_data = {
    "name" : "Subeen",
    "email" : "book@subeen.com",
    "country" : "Bangladesh"
}

url = base_url + "process.php";

# send the request
res = requests.post(url,info_data);

if not res.ok :
    sys.exit(">> Error downloading the file. :( <<");


with open("book.pdf","wb") as file :
    file.write(res.content);

print(">> Book Download Successfully :) <<");

