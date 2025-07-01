from data import borrowings as borrow_data
from cache import borrower as borrower_cache
from datetime import datetime
from fastapi import HTTPException


def add_book(book):
    exists = borrow_data.get_book_by_title(book.title)
    if exists:
        raise HTTPException(status_code=400, detail="Book with same title already exists")
    return borrow_data.insert_book(book.title, book.author)


def list_books():
    return borrow_data.select_books()


def delete_book(book_id):
    success = borrow_data.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return True


def borrow_book(req):
    book = borrow_data.get_book_by_title(req.title)
    if not book:
        raise HTTPException(status_code=404, detail="Book not available")
    borrow_data.delete_book_by_title(req.title)
    borrow_data.insert_borrowing(req.borrower, req.title, book['author'], datetime.now().strftime('%Y-%m'))
    borrower_cache.add_borrowed_book(req.borrower, req.title)
    return True


def get_borrowed_by_month(borrow_month):
    try:
        datetime.strptime(borrow_month, "%Y-%m")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid month format. Use YYYY-MM")
    return borrow_data.select_borrowings_by_month(borrow_month)


def get_borrower_books(borrower):
    books = borrower_cache.get_borrowed_books(borrower)
    return {"borrower": borrower, "books": books}


def return_book(req):
    record = borrow_data.get_borrowing_record(req.borrower, req.title)
    if not record:
        raise HTTPException(status_code=404, detail="No such borrowing record")
    borrow_data.delete_borrowing_record(req.borrower, req.title)
    borrow_data.insert_book(req.title, record['author'])
    borrower_cache.remove_borrowed_book(req.borrower, req.title)
    return True