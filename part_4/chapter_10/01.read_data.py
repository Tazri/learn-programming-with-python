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

'''
output : 
row -> ('Computer Programming Part 1', 'Tamim Shahriar', 260.0)
row -> ('Computer programming part 2', 'Tamim Shariar', 344.0)
row -> ('Computer Programming Part 3', 'Tamim Shariar', 322.0)
row -> ('Programming Exercise', 'Tamim Rafi', 140.0)
row -> ('Computer Programming Part 1', 'Tamim Shahriar', 260.0)
row -> ('Computer programming part 2', 'Tamim Shariar', 344.0)
row -> ('Computer Programming Part 3', 'Tamim Shariar', 322.0)
row -> ('Programming Exercise', 'Tamim Rafi', 140.0)
'''