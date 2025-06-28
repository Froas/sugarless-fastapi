from pydantic import BaseModel
from typing import Optional, List
from .enums import Tags, CategoryType
import uuid


class Sugar(BaseModel):
    added: float
    natural: float

class Macros(BaseModel):
    fat: float
    protein: float
    carbs: float


class Product(BaseModel):
    name: str
    sugar: Sugar
    type: Optional[List[Tags]] = [Tags.sugarless]
    calories: float
    category: Optional[CategoryType] = CategoryType.daily
    macros: Macros