from typing import Union
from fastapi import FastAPI
import time
import random
import string

app = FastAPI()

@app.get("/")
def read_root(u: str):
    epoch_time = int(time.time())

    return {"Hello": unique_url(int(u))}


@app.get("/{id}")
def read_item(id: str):
    return {"item_id": id}

def is_unique_string(random_string):
    return True

def unique_url(n):
    alphanumeric_characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(alphanumeric_characters) for _ in range(n))

    if is_unique_string(random_string):
        return random_string
    
    unique_url(n)
