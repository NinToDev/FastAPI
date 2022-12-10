from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    date_creation: str