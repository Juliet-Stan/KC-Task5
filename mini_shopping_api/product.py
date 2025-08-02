from pydantic import BaseModel, ValidationError, field_validator, model_validator

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int = 0

    @field_validator('price', 'quantity')
    def value_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError('Value must be non-negative')
        return v