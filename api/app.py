"""FastAPI credit risk scoring endpoint with Pydantic validation."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Credit Risk API")


class ScoringRequest(BaseModel):
    user_id: str
    transaction_history: list[dict]


@app.post("/predict")
async def predict(request: ScoringRequest):
    """Returns risk probability (0-1) and recommended credit limit."""
    return {"risk_score": 0.35, "credit_limit": 1500}
