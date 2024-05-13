from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    description: str
    image: str
    price: float


class UpdateProduct(BaseModel):
    id: int
    name: str
    description: str
    image: str
    price: float

