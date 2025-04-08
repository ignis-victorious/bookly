#  ___________________
#  Import LIBRARIES
from typing import Any
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
import books_db
import schema
from schema import Book_Update
#  Import FILES
#  ___________________


app = FastAPI()


@app.get("/books", response_model=list[schema.Book] | None)
# @app.get("/books", response_model=List[books_db.Book])
async def get_all_books() -> list[schema.Book] | None:
    # async def get_all_books() -> list[dict[str, Any]]:
    return books_db.books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: schema.Book) -> schema.Book:
    new_book: schema.Book = book_data.model_dump()
    books_db.books.append(new_book)
    return new_book
    # pass


@app.get("/book/{book_id}")
async def get_book(book_id: int) -> schema.Book | None:
    # if book: schema.Book == None:
    #     return {"message": "Please insert a valid id for a book"}
    print("Hello")
    for book in books_db.books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")
    # pass


@app.patch("/book/{book_id}", response_model=Book_Update)
async def update_book(
    book_id: int, book_update_data: schema.Book_Update
) -> schema.Book:
    for book in books_db.books:
        print(f"book: {book}")
        print(f"book['title']: {book['title']}")
        # print(f"book.title: {book.title}")  ERROR
        print("-1")

        if book["id"] == book_id:
            print("0")
            # print(f"Book_Update: {schema.Book_Update.title}")  ERROR!!!
            # print(f"Book_Update: {schema.Book_Update['title']}")
            print("1")
            book["title"] = "Elle"  # schema.Book_Update["title"]
            print(f"book['title'] (elle): {book['title']}")
            print("2")
            book["title"] = schema.Book_Update["title"]
            print(f"book['title'](title): {book['title']}")
            print("2Bis")
            # book["title"] = schema.Book_Update.title
            # print("2Tris")

            book["author"] = schema.Book_Update["author"]
            print("3")
            book["publisher"] = schema.Book_Update["publisher"]
            book["page_count"] = schema.Book_Update["page_count"]
            book["language"] = schema.Book_Update["language"]
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")

    # pass


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:  # -> list[schema.Book] | None:
    for book in books_db.books:
        # print(f"book: {book}")
        if book["id"] == book_id:
            print(f"book: {book}, id: {id}")
            books_db.books.remove(book)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")

    # pass


# def main():
#     print("Hello from bookly!")


# if __name__ == "__main__":
#     main()
