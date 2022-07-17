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