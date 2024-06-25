from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{num}")
def read_item(num: int):
    return {"num": num, "flag": isPrime(num)}


def isPrime(n):
    if n <= 1:
        return "F"
    for i in range(2, n):
        if n % i == 0:
            return "F"
    return "T"
