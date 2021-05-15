from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# run this command in terminal : uvicorn fastapi_test_code:app --reload
# do not run : python fastapi_test_code.py

# please must check fastapi run, it will be very compulsory
# check : http://127.0.0.1:8000/docs
