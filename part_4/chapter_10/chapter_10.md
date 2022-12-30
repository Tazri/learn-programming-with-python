Chapter 10 : Database Programming 
====================

Python has a **sqlite3** package for work with sqlite database.  Here the table of content of chapter 10 : 

- [Connect Database](#connect-database)


<hr />

## Connect Database

Here syntax to connect sqlite3 database : 

```py
import sqlite3

con = sqlite3.connect(path_to_sqlite_database_file);

con.close() # close the database
```

If databse file is dose not exist then ***sqlite3.connect()*** method create the database file. When database connection successfully then create **cursor** object by using **.cursor()** method. Here simple example : 

```py
cur = con.cursor();
```

Run query language by cursor object. When work is done with database then close cursor object first then commit the connection and at the last close the connection. Here simple syntax : 

```py
cur.close(); # close the cursor object
con.commit(); # coomit the connection object
con.close(); # close the connection object
```

Here example : 
***Program : connect_databse_testing.py***
```py
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
```


Here some method to use for run query on database by cursor object : 

| Method Name        | Description                                                  |
|--------------------|--------------------------------------------------------------|
| cur.execute()      | execute single line of query by string                       |
| cur.executemany()  | execute multiline of query by string and tuple or list       |

<hr />

## Read the data from Database

Use below method for read data from database : 

| Method Name     | Description                                                   |
|-----------------|---------------------------------------------------------------|
| cur.fetchone()  | cur.fetchone() is iterator which return single tuple if data is exist every calling otherwise return none |
| cur.fetchall()  | return list of tuple where every tuple is contain row |

Here example of read the from database : 

***Program : 01.read_data.py***
```py
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
```

Another Example of read data from database : 
```py
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
```

## Example of save password in database
**Program : 03.password_encription_example.py**
```py
# register the password with user
def register(user, password):
    ecrypted_password = encrypt_password(password);
    save_user(user, ecrypted_password);

# login logic
def login(user,password):
    stored_password = get_password_from_db(user);
    encrypted_password = encrypt_password(password);

    if stored_password != encrypted_password:
        return "Incorrect Password!";

def get_password_from_db():
    pass;

def save_user():
    pass;

# logic of encrypt password
import hashlib

# encrypt logic
def encrypt_password(password):
    m = hashlib.sha256();
    m.update(password.encode());
    return m.hexdigest();
```

> 🟢 **hashlib** package use for hashing thing in python.

Example of use hashlib : 
```bash
>>> import hashlib
>>> password = 'secret';
>>> salt = 'a1b2c3';
>>> dk = hashlib.pbkdf2_hmac('sha256',password.encode(),salt.encode(),100000);
>>> dk.hex()
'af169a74b0edf2bcb22d63c797457be655d8699423fb8fc86e74094ee906f0cb'
>>> 
```

Here structure of ***hashlib.pbkdf2_hmac()*** structure : 
```py
hashlib.pbkdf2_hmac(encription_algorithm,passowrd.encode(),salt.encode(),how_many_time_encrypt);
```

<hr />
<br />

[< Go Back](./../part_4.md)
--------------------------