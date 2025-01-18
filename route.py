from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
import schemas, service, auth

router = APIRouter()
db = get_db()

@router.post("/login", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Logs a user in and returns a JWT access token."""
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = auth.create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, current_user: schemas.User = Depends(auth.get_current_user)):
    """Creates a new book after validating the logged-in user."""
    return service.create_book(db, book)

@router.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, current_user: schemas.User = Depends(auth.get_current_user)):
    """Reads books in the db after validating the logged-in user."""
    return service.get_books(db, skip, limit)

@router.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, current_user: schemas.User = Depends(auth.get_current_user)):
    """Reads a single book by id in the db after validating the logged-in user."""
    return service.get_book(db, book_id)

@router.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, current_user: schemas.User = Depends(auth.get_current_user)):
    """Updates a book by id in the db after validating the logged-in user."""
    return service.update_book(db, book_id, book)

@router.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int, current_user: schemas.User = Depends(auth.get_current_user)):
    """Deletes a book by id in the db after validating the logged-in user."""
    return service.delete_book(db, book_id)
