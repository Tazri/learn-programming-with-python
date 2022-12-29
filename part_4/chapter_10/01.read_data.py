import sqlite3;

# connect database
con = sqlite3.connect('./data/dimik.db');
cur = con.cursor();

# execute sql 
cur.execute("SELECT * FROM book");

row = cur.fetchone();
while(row):
    print(f"row -> {row}");
    row = cur.fetchone();


# close cursor then connection
cur.close();
con.commit();
con.close();