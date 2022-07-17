import csv
import os

# create directory
try :
    os.mkdir("text");
except FileExistsError:
    print("May be directory already exist.");


# book details
field_names = ["Name","Author","Publisher","Price","Category"];
book1 = [
    "Computer Programming Part 1",
    "Tamim Shahrier Subeen",
    "Onnorokom Prokashoni",
    "240.00",
    "Programming"
];
book2 = [
    "Computer Programming Part 2",
    "Tamim Shahrier Subeen",
    "Dimik Prokashoni",
    "250.00",
    "Programming"
];
book3 = [
    "Learn Programming with Python",
    "Tamim Sharier Subeen",
    "Dimik Prokashoni",
    "200.00",
    "Programming"
]

book_list = [book1,book2,book3];


# create csv file
with open("./text/books.csv",'w') as file :
    csv_writer = csv.writer(file,delimiter=',',quotechar='\"',quoting=csv.QUOTE_MINIMAL);
    csv_writer.writerow(field_names);

    for book in book_list :
        csv_writer.writerow(book);

    print(">>> CSV FILE WRITE SUCCESSFULLY <<<");
    # csv_writer.writerows(book_list); # escape for loop to write row