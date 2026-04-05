from pydantic import BaseModel
from typing import Optional


class SoilInput(BaseModel):
    ph: float
    nitrogen: str  # "low", "medium", "high"
    phosphorus: str
    potassium: str
    calcium: Optional[float] = None
    magnesium: Optional[float] = None
    sulfur: Optional[float] = None


class CropInput(BaseModel):
    name: str  # e.g., "corn", "wheat"


class FertilizerRecommendation(BaseModel):
    fertilizer: str
    quantity: str
    instructions: str
