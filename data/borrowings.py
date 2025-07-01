import sqlite3

def get_db():
    conn = sqlite3.connect("mydb.db")
    conn.row_factory = sqlite3.Row
    return conn

def insert_book(title, author):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()
    return True

def select_books():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT title, author FROM books")
    rows = cur.fetchall()
    conn.close()
    return [{"title": r[0], "author": r[1]} for r in rows]

def delete_book(book_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    return deleted > 0

def get_book_by_title(title):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT author FROM books WHERE title = ?", (title,))
    row = cur.fetchone()
    conn.close()
    return {"author": row[0]} if row else None

def delete_book_by_title(title):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE title = ?", (title,))
    conn.commit()
    conn.close()

def insert_borrowing(borrower, title, author, borrow_month):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO borrowings (borrower, title, author, borrow_month) VALUES (?, ?, ?, ?)",
                (borrower, title, author, borrow_month))
    conn.commit()
    conn.close()

def select_borrowings_by_month(borrow_month):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT borrower, title, author FROM borrowings WHERE borrow_month = ?", (borrow_month,))
    rows = cur.fetchall()
    conn.close()
    return [{"borrower": r[0], "title": r[1], "author": r[2]} for r in rows]

def get_borrowing_record(borrower, title):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT author FROM borrowings WHERE title = ? AND borrower = ?", (title, borrower))
    row = cur.fetchone()
    conn.close()
    return {"author": row[0]} if row else None

def delete_borrowing_record(borrower, title):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM borrowings WHERE title = ? AND borrower = ?", (title, borrower))
    conn.commit()
    conn.close()
