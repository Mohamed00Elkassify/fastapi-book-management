from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import random


app = FastAPI()
# list of books
books = []

# pydantic model for Book
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

# create a new book
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book)
    return book

# get all books
@app.get("/books/", response_model=List[Book])
def get_books():
    return books

# get a book by id
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# update a book by id
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# search books by title case-insensitive
@app.get("/books/title/{title}", response_model=Book)
def get_book_by_title(title: str):
    for book in books:
        if book.title.lower() == title.lower():
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# delete a book by ID
@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# delete all books
@app.delete("/books/", response_model=List[Book])
def delete_all_books():
    books.clear()
    return books

# filter books by author case-insensititve
@app.get("/books/author/{author}", response_model=List[Book])
def filter_books_by_author(author: str):
    author_books = []
    for book in books:
        if book.author.lower() == author.lower():
            author_books.append(book)
    if not author_books:
        raise HTTPException(status_code=404, detail="Author not found")
    return author_books

# get a random book
@app.get("/books/random/", response_model=Book)
def get_random_book():
    if not books:
        raise HTTPException(status_code=404, detail="No books available")
    return random.choice(books)

# count the total number of books
@app.get("/books/count/", response_model=int)
def count_books():
    return len(books)