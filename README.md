# FastAPI Book Application

A simple CRUD application for managing books using FastAPI (Python 3.9), SQLite, and JWT authentication. This project demonstrates how to create an API that allows users to perform CRUD operations on a book collection, with user authentication secured using JWT tokens.

## Features

- **Create, Read, Update, Delete (CRUD)** operations for books.
- **JWT-based authentication** for securing APIs.
- **SQLite** as the database backend.
- Uses FastAPI's dependency injection for efficient session management.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-book-app.git
   cd fastapi-book-app
   
2. **Create a virtual-environment and install the needed dependencies:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     python3 -r requirements.txt
3. **Run the application**
     ```bash
     python3 main.py
    this will start the application on http://127.0.0.1:8000/docs (Swagger UI)

## Endpoints
Documented with swagger, accesible at http://127.0.0.1:8000/docs
