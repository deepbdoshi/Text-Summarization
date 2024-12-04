import uvicorn
import sys
import os

from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

from starlette.responses import RedirectResponse
from text_summarization.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/model-train")
async def training_route():
    try:
        os.system("python main.py")
        return Response("Training successful!")

    except Exception as e:
        return Response(f"Error Occurred in Training Stage! {e}")


@app.post("/summary-generation")
async def prediction_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        return Response(f"Error Occurred in Summary Generation Stage! {e}")
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)