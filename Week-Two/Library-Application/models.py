import sqlite3 as sql
import datetime


def user_login(user, passcode):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute('SELECT * from users WHERE username="%s" AND password_hash="%s"' % (user, passcode))
    exist = cur.fetchone()
    if exist is None:
        print "All books currently borrowed"
    else:
        print "yes"
    con.commit()
    con.close()



def insert_user(email,username,phone,password,member_since, last_login, charges, rights):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,username,phone,password, member_since, last_login, charges, rights) VALUES (?,?,?,?)",
                (email,username,phone,password,member_since, last_login, charges, rights))
    con.commit()
    con.close()


def update_book_as_unavailable(bookname):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute("UPDATE books SET availability = ? WHERE book_name= ?", ("unavailable", bookname))
    con.commit()
    con.close()


def delete_book_from_library(bookname):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE book_name= ?", (bookname))
    #cur.execute("delete from books where book_name = '%s' " % bookname)
    con.commit()
    con.close()

def surcharge_user(bookname,user, charge):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute("UPDATE activities SET surcharge = ? WHERE book= ? AND borrowed_by=?", (charge, bookname, user))
    con.commit()
    con.close()



def book_returned(bookname,user):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    returner =  cur.execute("UPDATE activities SET date_returned = ? WHERE book= ? AND borrowed_by=?", (DateTime('now'), bookname, user))
    if returner:
        cur.execute("UPDATE books SET quantity = quantity+1 WHERE book= ? AND borrowed_by=?",
                    (bookname, user))
    else:
        print "Error updating"
    con.commit()
    con.close()



def borrow_available_book(book, bookname,user):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    returnDate = datetime.now()+relativedelta(days=14)
    formattedReturnDate = returnDate.strftime('%Y-%m-%d %H:%M:%S')
    cur.execute('SELECT * from books WHERE book="%s" AND availability="%s"' % (book, "Yes"))
    exist = cur.fetchone()
    if exist is None:
        print "All books currently borrowed"
    else:
        rowy = cur.execute("INSERT INTO activities (book,borrowed_by,available,date_borrowed, return_by_date, surcharge) VALUES (?,?,?,?)",
                    (bookname, username,"No", DateTime('now'),formattedReturnDate, "0"))
        if rowy:
            cur.execute("UPDATE books SET quantity =  quantity-1 WHERE book= ? AND borrowed_by=?",
                        (bookname, user))
        else:
            print "error updating books!!"
    con.commit()
    con.close()



def insert_book(book_name,quantity,borrowed, added_by):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books (book_name,quantity,borrowed, added_by) VALUES (?,?,?,?)", (book_name,quantity,borrowed, added_by))
    con.commit()
    con.close()

def categorize_all_books(book, cat):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute('SELECT * from books WHERE book="%s" AND category="%s"' % (book, cat))
    if cur.fetchone() is not None:
        print "Welcome"
    else:
        print "Login failed"

def categorize_books(book, cat):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute('SELECT * from books WHERE book="%s" AND category="%s"' % (book, cat))
    if cur.fetchone() is not None:
        print "Welcome"
    else:
        print "Login failed"

def login_user(user, pswd):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    cur.execute('SELECT * from users WHERE name="%s" AND password="%s"' % (user, pswd))
    if cur.fetchone() is not None:
        print "Welcome"
    else:
        print "Login failed"



def select_account_holder(params=()):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    if params==():
        cur.execute("select * from account_holder")
    else:
        string = "select"
        for i in xrange(len(params)-1):
            string += "%s,"
        string += "%s"
        string += " from account_holder"

        result = cur.execute(string)
        con.close()
        return result.fetchall()

def select_contact(params=()):
    con = sql.connect("andela_library.db")
    cur = con.cursor()
    if params==():
        cur.execute("select * from contact")
    else:
        string = "select"
        for i in xrange(len(params)-1):
            string += "%s,"
        string += "%s"
        string += " from contact"

        result = cur.execute(string)
        con.close()
        return result.fetchall()



