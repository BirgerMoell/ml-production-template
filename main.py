from typing import Optional

from fastapi import FastAPI

from model import Classifier
from pydantic import BaseModel

class PredictModel(BaseModel):
    image_url: str
    label: str

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def predict(predictmodel: PredictModel):
    predictmodel = predictmodel.dict()
    print(type(predictmodel))
    #print(predictmodel)
    my_classifier = Classifier()
    prediction = my_classifier.evaluate([predictmodel["image_url"], predictmodel["label"]])
    #print(f"type(prediction): {type(prediction)}")
    #print(f"prediction: {prediction}")
    return {"prediction": prediction}
    #return {"Hello": "World"}
