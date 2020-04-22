import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    members = cur.fetchall()
    conn.close()
    return members

def search(title= "", author= "", year= "", isbn= ""):
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM book WHERE title= ? OR author=? OR year= ? OR isbn= ?",(title, author, year, isbn))
    members = cur.fetchall()
    conn.close()
    return members

connect()

insert("The sea", "John Smith", 1918, 913123132)
print(view())
print(search(author= "John Smith"))
