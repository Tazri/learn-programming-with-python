import requests,os
import webbrowser as wb 

url = "http://www.google.com";
res = requests.get(url);

if res.ok :
    with open("google.html","w") as file :
        file.write(res.text);
        print(">> File was write successfully!! <<");
    
    file_path = os.path.realpath("dimik.html");
    print(">> FILE LOCATION IS : ")
    print(file_path);
    wb.open("file://"+file_path);
else :
    print(">> Requst is bad :(");
    