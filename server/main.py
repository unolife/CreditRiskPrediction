from typing import Optional
from inputModel import InputData

from fastapi import FastAPI

app = FastAPI()

@app.post("/predict")
def predict_data(input_data: InputData):
    return {"data": input_data}

@app.get("/")
def read_root():
    return {"Hello": "World"}


