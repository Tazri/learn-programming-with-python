import os,csv

try :
    os.mkdir("text");
except FileExistsError :
    print(">>> The Directory already exsit. <<<");

# book details
field_names = ["Name","Author","Publisher","Price","Category"];
book1 = {
    "Name" :"Computer Programming, Part 1",
    "Author" : "Tamim Shahrier Subeen",
    "Publisher" : "Onnorokom Prokashoni",
    "Price" : "240.00",
    "Category" : "Programming"
};
book2 = {
    "Name" : "Computer Programming, Part 2",
    "Author" : "Tamim Shahrier Subeen",
    "Publisher" : "Dimik Prokashoni",
    "Price" : "250.00",
    "Category" : "Programming"
};
book3 = {
    "Name" : "Learn Programming with Python",
    "Author" : "Tamim Sharier Subeen",
    "Publisher" : "Dimik Prokashoni",
    "Price" : "200.00",
    "Category" : "Programming"
}

book_list = [book1,book2,book3];


file_name = './text/books_list.csv';

with open(file_name,'w') as csv_file :
    csv_writer = csv.DictWriter(csv_file,fieldnames=field_names);
    csv_writer.writeheader();
    csv_writer.writerows(book_list);
    print(">>> File was successfully created. <<<");