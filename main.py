#  ___________________
#  Import LIBRARIES
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


# def main():
#     print("Hello from bookly!")


# if __name__ == "__main__":
#     main()
