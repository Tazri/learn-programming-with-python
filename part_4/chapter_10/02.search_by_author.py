import sqlite3

database_path = './data/dimik.db';

def show_by_author(cur,author):
    # below query is danger for use because injection
    q = "SELECT * FROM book WHERE author=";
    
    
    
    print(f"-> query : {q} <-");
    # cur.execute(query);

    # use one of below querys for read data from database
    # cur.execute("SELECT * FROM book WHERE author=?",(author,));
    cur.execute("SELECT * FROM book Where author=:auth",{"auth": author});
    rows = cur.fetchall();
    for row in rows:
        print(row);


# create connection and cursor object
con = sqlite3.connect(database_path);
cur = con.cursor();

show_by_author(cur,"Tamim Rafi");


# close cursor and connection
cur.close();
con.commit();
con.close();


'''
ouptut ; 
->query : SELECT * FROM book WHERE author='Tamim Rafi' <-
('Programming Exercise', 'Tamim Rafi', 140.0)
('Programming Exercise', 'Tamim Rafi', 140.0)
'''