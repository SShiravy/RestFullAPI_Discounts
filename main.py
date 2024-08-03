from fastapi import FastAPI
from read_data import read_all_data

app = FastAPI()


@app.get("/all_discounts")
async def all_discounts():
    return read_all_data()

