from fastapi import FastAPI
from src.functional import calculate


app = FastAPI()


@app.get("/calculate/{a}/{b}")
def calculate_endpoint(a: int, b: int) -> dict[str, int]:
    return {"result": calculate(a, b)}
