from inputModel import InputData
import pandas as pd
from fastapi.encoders import jsonable_encoder
from services import DataPreprocessor
from fastapi import FastAPI

app = FastAPI()

@app.post("/predict")
def predict_data(input_data: InputData):
    df = pd.DataFrame.from_records([jsonable_encoder(input_data)])
    df = DataPreprocessor.data_cleansing(df)
    print(df.info())
    print(df.head())

    return {"data": input_data}

@app.get("/")
def read_root():
    return {"Hello": "World"}
