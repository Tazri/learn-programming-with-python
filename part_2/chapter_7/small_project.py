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
    