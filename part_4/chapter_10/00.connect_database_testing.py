import sqlite3;


con = sqlite3.connect("./data/dimik.db"); # pass path to database file
cur = con.cursor(); # create cursor object

# create table
# execute sql language
cur.execute("CREATE TABLE IF NOT EXISTS book (name text, author text, price real)");

# insert a single row
cur.execute( # cursor object for run query language
    "INSERT INTO book VALUES ('Computer Programming Part 1', 'Tamim Shahriar',260)"
);

book_list = [
    ("Computer programming part 2", "Tamim Shariar",344),
    ("Computer Programming Part 3", "Tamim Shariar",322),
    ("Programming Exercise", "Tamim Rafi",140)
];

cur.executemany("INSERT INTO book VALUES (?, ?, ?)",book_list);

cur.close(); # first close cursor
con.commit(); # commit before close connection
con.close(); # close connection