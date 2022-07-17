import requests

url = "http://dimikcomputing.com"

response = requests.get(url);

if response.ok :
    with open("dimik.html","w") as f :
        f.write(response.text);
        print("File write successfully.");
else :
    print("Request Can not ok.");
    