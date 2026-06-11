from pydantic import BaseModel

class QuestionPair(BaseModel):
    question1 : str
    question2 : str

class PredictionResponse(BaseModel):
    prediction : str
    confidence : float