from pydantic import BaseModel

class AreaRect(BaseModel):
    x1: float
    x2: float
    y1: float
    y2: float