#  ___________________
#  Import LIBRARIES
from typing import Any
from fastapi import FastAPI
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


# def main():
#     print("Hello from bookly!")


# if __name__ == "__main__":
#     main()
