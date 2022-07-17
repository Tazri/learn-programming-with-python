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