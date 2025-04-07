#  ___________________
#  Import LIBRARIES
from typing import Any
from fastapi import FastAPI, Header
import schema
#  Import FILES
#  ___________________


app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet_name(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}


@app.get("/greetings")
async def greetings_w_name(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}


@app.get("/mix-greet/{name}")
# async def greetings_mix(name: str, age: int) -> dict[str, int]:
async def greetings_mix(name: str, age: int = None) -> dict[str, Any]:
    return {"message": f"Hello {name}", "age: ": age}


@app.get("/optional-greet")
async def greetings_opt(name: str = "User", age: int = None) -> dict[str, Any]:
    return {"message": f"Hello {name}", "age: ": age}


@app.post("/create_book")
async def create_book(book_data: schema.BookCreateModel) -> dict[str, Any]:
    return {"title": book_data.title, "author": book_data.author}


@app.get("/get_headers", status_code=201)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
) -> dict:
    request_headers: dict = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers


# def main():
#     print("Hello from bookly!")


# if __name__ == "__main__":
#     main()
