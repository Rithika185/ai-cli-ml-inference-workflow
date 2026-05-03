from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    # Input validation: hours_studied must be non-negative
    hours_studied: float = Field(..., ge=0, description="The number of hours studied.")

class PredictionResponse(BaseModel):
    # The predicted exam score
    predicted_score: float = Field(..., description="The predicted exam score.")

class HealthResponse(BaseModel):
    # Simple status for health check
    status: str = Field(..., description="The status of the API.")
