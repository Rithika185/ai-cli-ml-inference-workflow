from fastapi import FastAPI
from app.schemas import PredictionRequest, PredictionResponse, HealthResponse
from app.model import exam_model

app = FastAPI(title="ML Inference API", description="A simple API for predicting exam scores.")

@app.get("/", response_model=HealthResponse)
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """
    Predict exam score based on hours studied.
    """
    prediction = exam_model.predict(request.hours_studied)
    return {"predicted_score": prediction}
