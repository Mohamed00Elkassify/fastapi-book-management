# FastAPI Book Management 📚

This is a simple FastAPI application for managing books. It provides endpoints to create, read, update, delete, search, and filter books.

## Features 🚀
- 📖 Add, update, and delete books  
- 🔍 Search books by title (case-insensitive)  
- 🖊️ Filter books by author (case-insensitive)  
- 🎲 Get a random book  
- 📊 Count total books  

## Installation 🛠️

###1. Clone the repository:  
   ```bash
   git clone https://github.com/Mohamed00Elkassify/fastapi-book-management.git
   cd fastapi-book-management
   ```

###3. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

###4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints 🔗

### 📌 Book Operations
- **`POST /books/`** → Add a new book  
- **`GET /books/`** → Get all books  
- **`GET /books/{book_id}`** → Get a book by ID  
- **`PUT /books/{book_id}`** → Update a book  
- **`DELETE /books/{book_id}`** → Delete a book  
- **`DELETE /books/`** → Delete all books  

### 🔍 Search & Filter
- **`GET /books/title/{title}`** → Search book by title (case-insensitive)  
- **`GET /books/author/{author}`** → Filter books by author (case-insensitive)  

### 🎲 Other Features
- **`GET /books/random/`** → Get a random book  
- **`GET /books/count/`** → Get the total count of books  

## License 📜
This project is licensed under the MIT License.
