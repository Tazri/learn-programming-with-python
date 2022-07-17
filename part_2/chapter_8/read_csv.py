import csv

with open('./text/books.csv','r',newline='') as file :
    csv_reader = csv.reader(file);
    for row in csv_reader :
        print(row);