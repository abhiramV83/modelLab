import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from MlModels import knn,Linear_Regression,Logistic_Regression,Naive_Bayes

app = FastAPI()
origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/train")
def upload_dataset(
    file: UploadFile = File(...),
    model: str = Form(...)
):  
    if(model=="K_Nearest_Neighbours"):
        accuracy=knn(file)
    elif(model=="Linear_Regression"):
        accuracy=Linear_Regression(file)
    elif(model=="Logistic_Regression"):
        accuracy=Logistic_Regression(file)
    elif(model=="Naive_Bayes"):
        accuracy=Naive_Bayes(file)
    else:
        accuracy="Please select a model"
    return {
        "dataset_name": file.filename,
        "model_name": model,
        "result_is": accuracy,
    }