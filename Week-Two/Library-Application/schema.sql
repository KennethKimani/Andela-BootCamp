drop table if exists users;
create table users (
    id integer primary key autoincrement,
    firstname text not null,
    lastname text not null,
    username text not null,
    password text not null,
    password_hash text not null,
    unique_user_id text not null,
    email text not null,
    member_since datetime not null,
    last_login datetime default current_timestamp,
    charges integer not null,
    rights text not null

);




drop table if exists books;

create table books (
    id integer primary key autoincrement,
    book_name text not null,
    unique_book_id text not null,
    quantity integer not null,
    borrowed integer not null default 'No',
    category text not null,
    borrow_period text not null,
    availability text not null default 'Yes',
    description text not null,
    added_by text not null,
    FOREIGN KEY(added_by) REFERENCES users(username)


);





drop table if exists activities;
    create table activities (
        id integer primary key autoincrement,
        book text not null,
        unique_book_id text not null,
        borrowed_by text not null,
        available text not null,
        date_borrowed datetime null,
        return_by_date datetime null,
        date_returned datetime null,
        surcharge integer null,
        FOREIGN KEY(book) REFERENCES books(book_name),
        FOREIGN KEY(borrowed_by) REFERENCES users(username)

    );








