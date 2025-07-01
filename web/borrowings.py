from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from service import borrowings as borrow_service

router = APIRouter()

class Book(BaseModel):
    title: str
    author: str

class BorrowRequest(BaseModel):
    borrower: str
    title: str

@router.post("/books")
def add_book(book: Book):
    return borrow_service.add_book(book)

@router.get("/books")
def list_books():
    return borrow_service.list_books()

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    return borrow_service.delete_book(book_id)

@router.post("/borrows")
def borrow_book(req: BorrowRequest):
    return borrow_service.borrow_book(req)

@router.get("/borrows/month/{borrow_month}")
def get_borrowed_by_month(borrow_month: str):
    return borrow_service.get_borrowed_by_month(borrow_month)

@router.get("/borrowers/{borrower}/books")
def get_borrower_books(borrower: str):
    return borrow_service.get_borrower_books(borrower)

@router.post("/return")
def return_book(req: BorrowRequest):
    return borrow_service.return_book(req)

