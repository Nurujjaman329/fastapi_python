from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    vendor_id: int   # add this

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    vendor_id: int   # add this

    class Config:
        orm_mode = True
