from flask import Flask, flash, redirect, render_template, request, session, abort, json, current_app, url_for
import os
import sqlite3 as sql
from datetime import datetime,date,timedelta
from dateutil.relativedelta import relativedelta
from werkzeug import generate_password_hash, check_password_hash
import random
import string
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#db configurations
conn = sql.connect('andela_library.db')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/')
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def logginin():
    error = None
    msg = None
    if request.method == 'POST':
        if request.form['useremail'] != '' or request.form['password'] != '':
            con = sql.connect('andela_library.db')
            try:
                _email = request.form['useremail']
                _password = request.form['password']
                _hashed_password = generate_password_hash(_password)
                check_password_hash(_hashed_password, _password)

                remember_me = False
                if 'remember_me' in request.form:
                    remember_me = True

                cur = con.cursor()
                cur.execute('SELECT * from users WHERE email="%s" AND password="%s"' % (_email, _password))
                exist = cur.fetchone()
                if exist is None:
                    session['logged_in'] = False
                    flash('Invalid credentials', 'error')
                    return render_template("login.html", msg=msg, error=error)
                else:
                    print(exist[9])  # Print the first column retrieved(user's name)
                    session['logged_in'] = True
                    session['user'] = _email
                    session['status'] = exist[11]
                    flash('You were successfully logged in', 'success')
                    return redirect(url_for('index'))
            except con.OperationalError as er:
                print 'er:', er.message
                con.rollback()
                flash('Error in insert operation', 'error')
                return render_template("login.html", msg=msg, error=error)
            finally:
                con.close()

        else:
            flash('Both Username and Password Blank. Please try again.', 'error')
            return render_template('login.html', error=error)
    return render_template('login.html', error=error)


# route for handling the login page logic
@app.route('/userlogin', methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('loginx.html', error=error)

@app.route('/admin_login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signup',  methods=['GET', 'POST'])
def signup():
    error = None
    msg = None
    if request.method == 'POST':
        if request.form['firstname'] != '' or request.form['lastname'] != '' or request.form['inputEmail'] != '' or request.form['password'] != '' or request.form['inputComPassword'] != '' or request.form['username'] != '':

            try:
                con = sql.connect('andela_library.db')
                try:
                    _username = request.form['username']
                    _useremail = request.form['inputEmail']
                    _userpassword = request.form['password']
                    _userpassword2 = request.form['inputComPassword']
                    _userhashed_password = generate_password_hash(_userpassword)
                    _firstname = request.form['firstname']
                    _lastname = request.form['lastname']
                    unique_user = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

                    if _userpassword != _userpassword2:
                        flash('Passwords do not match. Please try again.', 'error')
                        return render_template("signup.html", msg=msg, error=error)
                    else:
                        expires = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        cur = con.cursor()
                        cur.execute(
                            "INSERT INTO users (firstname, lastname, email,username,unique_user_id,password,password_hash, member_since, charges, rights) VALUES (?,?,?,?,?,?,?,?,?,?)",
                            (_firstname, _lastname, _useremail, _username, unique_user, _userpassword, _userhashed_password, expires, 0, "User"))

                        rowInserted = cur.lastrowid
                        if rowInserted == -1:
                            session['logged_in'] = False
                            flash('User not inserted!. Please try again', 'error')
                            return render_template("signup.html", msg=msg, error=error)
                        else:
                            con.commit()
                            flash('User registered successfully, Please log in', 'success')
                            return redirect(url_for('index'))

                except con.OperationalError as er:
                    print 'er:', er.message
                    con.rollback()
                    flash('Euser not added. Error in insert operation, Please try again', 'error')
                    return render_template("signup.html", msg=msg, error=error)
                finally:
                    con.close()

            except sql.Error as e:
                print(e)
                flash('Error opening database: '+e, 'error')
                return render_template('signup.html', error=error)
        else:
            flash('Some Input Values are Blank. Please try again.', 'error')
            return render_template('signup.html', error=error)

    return render_template('signup.html', error=error)


# logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session['user'] = ''
    flash('You have been logged out')
    return redirect(url_for('index'))



@app.route('/index')
def index():
    con = sql.connect("andela_library.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from books")

    rows = cur.fetchall()
    return render_template("list_books.html", rows=rows)




@app.route('/list_books')
def list_books():
    con = sql.connect("andela_library.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from books")

    rows = cur.fetchall()
    return render_template("list_books.html", rows=rows)


@app.route('/list_users')
def list_users():
    con = sql.connect("andela_library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    rows = cur.fetchall()
    return render_template("list_users.html", rows=rows)


@app.route('/list_activities')
def list_activities():
    con = sql.connect("andela_library.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from activities")
    rows = cur.fetchall()
    return render_template("list_activities.html", rows=rows)


# Admin add users
@app.route('/admin_insert', methods=['GET', 'POST'])
def insert():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        address = request.form['address']
        table = request.form['table']
        if not name or not email:
            error = "Please check your entires"
            if not phone_number.isdigit():
                error = "Please enter a valid User Name"
        user_reg = User(name, phone_number, email, address, table)
        db.session.add(user_reg)
        db.session.commit()
        flash('Registration Successfull.')
    return render_template('admin_insert.html', error=error)


# Admin add books
@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    error = None
    msg = None
    if request.method == 'POST':
        if request.form['book_name'] != '' or request.form['category'] != '' or request.form['quantity'] != '' or request.form['description'] != '':

            try:
                con = sql.connect('andela_library.db')

                try:
                    _book_name = request.form['book_name']
                    _category = request.form['category']
                    _quantity = request.form['quantity']
                    _period = request.form['period']
                    _description = request.form['description']
                    added_by = session['user']
                    _unique_book_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
                    if session['user'] =='':
                        msg = "Please login to add a Book!!"
                        error = 'Please login to add a Book!.'
                        return render_template("login.html", msg=msg, error=error)

                    else:

                        expires = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        cur = con.cursor()
                        cur.execute(
                            "INSERT INTO books (book_name, unique_book_id, quantity, borrowed, category, borrow_period, availability, description, added_by) VALUES (?,?,?,?,?,?,?,?,?)",
                            (_book_name, _unique_book_id, _quantity, 0, _category, _period, "Yes", _description, added_by))

                        rowInserted = cur.lastrowid
                        if rowInserted == -1:
                            msg = "Book not inserted!!"
                            error = 'Book not inserted!. Please try again.'
                            return render_template("add_book.html", msg=msg, error=error)
                        else:

                            msg = "Book Inserted successfully. Insert another book?"
                            error = "Book Inserted successfully. Insert another book?"
                            con.commit()
                            return redirect(url_for('add_book'))

                except con.OperationalError as er:
                    print 'er:', er.message
                    con.rollback()
                    msg = "error in insert operation"
                    error = "book not added. Please try again"
                    return render_template("add_book.html", msg=msg, error=error)
                finally:
                    con.close()

            except sql.Error as err:
                print(err.message)
                error = "Error opening database: "+err.message
                return render_template('add_book.html', error=error)

        else:
            error = 'Some Input Values are Blank. Please try again.'
            return render_template('add_book.html', error=error)

    return render_template('add_book.html', error=error)




# Delete
@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):

    error = None
    msg = None
    if request.method == 'POST':
        if user != '':
            try:
                con = sql.connect('andela_library.db')

                try:
                    book_id = request.form['entry_id']
                    cur = con.cursor()
                    cur.execute("DELETE FROM books WHERE id= ?", (book_id))
                    rowInserted = cur.lastrowid
                    if rowInserted == -1:
                        msg = "Book not deleted!!"
                        error = 'Book not deleted!. Please try again.'
                        return render_template("list_books.html", msg=msg, error=error)
                    else:

                        msg = "Book deleted successfully. Delete another book?"
                        error = "Book deleted successfully. Delete another book?"
                        con.commit()
                        return redirect(url_for('list_books'))

                except con.OperationalError as er:
                    print 'er:', er.message
                    con.rollback()
                    msg = "error in insert operation"
                    error = "book not deleted. Please try again"
                    return render_template("list_books.html", msg=msg, error=error)
                finally:
                    con.close()

            except sql.Error as e:
                print(e)
                error = "Error opening database: " + e
                return render_template('list_books.html', error=error)

        else:
            error = 'Some Input Values are Blank. Please try again.'
            return render_template('list_books.html', error=error)

    return render_template('list_books.html', error=error)





# Borrow
@app.route('/borrow/<id>', methods=['POST', 'GET'])
def borrow(id):
    error = None
    msg = None
    if request.method == 'POST':
        if user != '':

            try:
                con = sql.connect('andela_library.db')

                try:
                    book_id = request.form['activity_id']
                    cur = con.cursor()
                    cur.execute('SELECT * from books WHERE id="%s" AND availability="%s"' % (book_id, "Yes"))
                    exist = cur.fetchone()
                    if exist is None:
                        print "All books currently borrowed"
                        error = "This book is currently borrowed. Try another book."
                        return render_template("list_books.html", msg=msg, error=error)

                    else:

                        bookname = exist[1]  # Print the first column retrieved(user's name)
                        _unique_book_id = exist[3]
                        quantity_now = exist[2]

                        if session['user'] != '':
                            username = session['user']
                        else:
                            return redirect(url_for('login'))

                        borrow_period = exist[5]

                        datex = datetime.now()
                        if borrow_period =="Short Term":
                            returnDate = datex + relativedelta(days=3)

                        elif borrow_period == "Long Term":
                            returnDate = datex + relativedelta(days=14)
                        else:
                            returnDate = datex + relativedelta(days=7)

                        formattedReturnDate = returnDate.strftime('%Y-%m-%d %H:%M:%S')
                        today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        if quantity_now > 0 :
                            cur.execute(
                                "INSERT INTO activities (book,unique_book_id, borrowed_by,available,date_borrowed, return_by_date, surcharge) VALUES (?,?,?,?,?,?,?)",
                                (bookname, _unique_book_id, username, "No", today, formattedReturnDate, "0"))
                            rowInserted = cur.lastrowid
                            if rowInserted == -1:
                                msg = "Book not borrowed!!"
                                error = 'Error borrowing book!!!. Please try again.'
                                return render_template("list_books.html", msg=msg, error=error)
                            else:

                                cur.execute("UPDATE books SET quantity =  quantity-1 WHERE book_name= ? AND id=? AND quantity>0",
                                            (bookname, book_id))

                                con.commit()
                                return redirect(url_for('list_books'))
                        else:
                            error = 'Error borrowing book!!!. All available books already borrowed!!.'
                            return redirect(url_for('list_books'))

                except con.OperationalError as er:
                    print 'er:', er.message
                    con.rollback()
                    msg = "error in insert operation"
                    error = "book not borrowed. Please try again"
                    return render_template("list_books.html", msg=msg, error=error)
                finally:
                    con.close()

            except sql.Error as e:
                print(e)
                error = "Error opening database: " + e
                return render_template('list_books.html', error=error)

        else:
            error = 'Some Input Values are Blank. Please try again.'
            # flash(error)
            return render_template('list_books.html', error=error)

    return render_template('list_books.html', error=error)







# Edit
@app.route('/editbook/<id>', methods=['GET', 'POST'])
def editbook(id):

    error = None
    msg = None
    if request.method == 'POST':
        if request.form['editBookTitle'] != '' or request.form['editBookQuantity'] != '' or request.form['editBookCategory'] != '' or request.form['editBookAvailable'] != ''or request.form['editBookDescription'] != '' or request.form['editBookDuration'] != '':

            try:
                con = sql.connect('andela_library.db')

                try:
                    book_id = request.form['edit_id']
                    book_title = request.form['editBookTitle']
                    book_quantity = request.form['editBookQuantity']
                    book_category = request.form['editBookCategory']
                    book_available = request.form['editBookAvailable']
                    book_description = request.form['editBookDescription']
                    book_duration = request.form['editBookDuration']
                    print book_description
                    print book_id
                    cur = con.cursor()
                    cur.execute("UPDATE books SET book_name = ?, quantity = ?, borrowed = ?, category = ?, borrow_period = ?, availability = ?, description = ? WHERE id= ?",
                                (book_title, book_quantity, "", book_category, book_duration, book_available, book_description, book_id))
                    if cur.rowcount == 1:
                        print "Book Details updated Successfully"
                        flash('Book Details updated Successfully', 'success')
                        con.commit()

                        return redirect(url_for('list_books'))

                    else:
                        print "Book not updated"
                        flash('This book is not found. Try another book.', 'error')
                        return redirect(url_for('list_books'))

                except con.OperationalError as er:
                    print 'er:', er.message
                    con.rollback()
                    flash('Error in insert operation. Book not updated. Please try again.', 'error')
                    return render_template("list_books.html", msg=msg, error=error)
                finally:
                    con.close()

            except sql.Error as e:
                print(e)
                error = "Error opening database: " + e
                flash('Error opening database: ' + e, 'error')
                return render_template('list_books.html', error=error)

        else:
            flash('Some Input Values are Blank. Please try again.', 'error')
            return render_template('list_books.html', error=error)

    return render_template('list_books.html', error=error)




# Return
@app.route('/returnbook/<id>', methods=['POST', 'GET'])
def returnbook(id):

    error = None
    msg = None
    if request.method == 'POST':
        if request.form['return_id'] != '':

            try:
                con = sql.connect('andela_library.db')

                try:
                    book_id = request.form['return_id']
                    print  book_id
                    #unique_book_id = request.form['unique_book_id']
                    datey = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cur = con.cursor()
                    cur.execute("UPDATE activities SET date_returned = ? AND available = ? WHERE unique_book_id= ?", (datey, "Yes", book_id))
                    if cur.rowcount == 1:
                        updter = cur.fetchone()
                        #unique_book_id = updter[2]
                        cur.execute("UPDATE books SET quantity = quantity+1 WHERE unique_book_id=?", (book_id))
                    else:
                        flash('Error updating', 'error')
                    cur.execute('SELECT * from books WHERE unique_book_id="%s" AND availability="%s"' % (book_id, "Yes"))
                    exist = cur.fetchone()
                    if exist is None:
                        print "All books currently borrowed"
                        flash('This book is currently borrowed. Try another book', 'error')
                        return render_template("list_books.html", msg=msg, error=error)

                    else:
                        bookname = exist[1]
                        category = exist[5]
                        dated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        rowy = cur.execute(
                            "INSERT INTO activities (book,borrowed_by,available,date_borrowed, return_by_date, surcharge) VALUES (?,?,?,?)",
                            (bookname, username, "No", dated, formattedReturnDate, "0"))
                        if rowy:
                            cur.execute("UPDATE books SET quantity =  quantity-1 WHERE book= ? AND borrowed_by=?",
                                        (bookname, user))
                            con.commit()
                            return redirect(url_for('list_books'))
                        else:
                            flash('Error updating books!!', 'error')


                        return redirect(url_for('list_books'))

                except con.OperationalError as er:
                    print 'er:', er.message
                    con.rollback()
                    flash('Book not returned. Please try again!', 'error')
                    return render_template("list_books.html", msg=msg, error=error)
                finally:
                    con.close()

            except sql.Error as e:
                print(e)
                flash('Error opening database: ' + e, 'error')
                return render_template('list_books.html', error=error)

        else:
            flash('Some Input Values are Blank. Please try again', 'error')
            return render_template('list_books.html', error=error)

    return render_template('list_books.html', error=error)


# Surcharge
@app.route('/surchage/<id>', methods=['POST', 'GET'])
def surchage(id):

    error = None
    msg = None
    if request.method == 'POST':
        if user != '':
            try:
                con = sql.connect('andela_library.db')

                try:

                    cur = con.cursor()
                    cur.execute("UPDATE activities SET surcharge = ? WHERE book= ? AND borrowed_by=?",
                                (charge, bookname, user))
                    exist = cur.fetchone()
                    if exist is None:
                        print "All books currently borrowed"
                        flash('This book is currently borrowed. Try another book.', 'error')
                        return render_template("list_books.html", msg=msg, error=error)

                    else:
                        bookname = exist.book
                        borrowed_by = exist.borrowed_by
                        available = exist.available
                        datee = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        rowy = cur.execute(
                            "INSERT INTO activities (book,borrowed_by,available,date_borrowed, return_by_date, surcharge) VALUES (?,?,?,?)",
                            (bookname, username, "No", datee, formattedReturnDate, "0"))
                        if rowy:
                            cur.execute("UPDATE books SET quantity =  quantity-1 WHERE book= ? AND borrowed_by=?",
                                        (bookname, user))
                            con.commit()

                        else:
                            flash('Error updating books!', 'error')

                        return redirect(url_for('list_books'))
                except con.OperationalError as er:
                    print 'er:', er.message
                    con.rollback()
                    flash('Error in insert operation!', 'error')
                    return render_template("list_books.html", msg=msg, error=error)
                finally:
                    con.close()

            except sql.Error as e:
                print(e)
                flash('Error opening database: ' + e, 'error')
                return render_template('list_books.html', error=error)

        else:
            flash('Some Input Values are Blank. Please try again. ', 'error')
            return render_template('list_books.html', error=error)

    return render_template('list_books.html', error=error)



# Error Handeling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='127.0.0.1', port=5000)






@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember=remember_me)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['text']:
            flash('Text is required', 'error')
        else:
            todo = Todo(request.form['title'], request.form['text'])
            todo.user = g.user
            db.session.add(todo)
            db.session.commit()
            flash('Todo item was successfully created')
            return redirect(url_for('index'))
    return render_template('new.html')





