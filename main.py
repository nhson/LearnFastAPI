from enum import Enum

from fastapi import FastAPI
app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexNet"
    resnet = "resNet"
    lenet = "leNet"

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if(model_name == ModelName.alexnet): 
        return {"model_name":model_name, "message":"Deep Learning"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
    