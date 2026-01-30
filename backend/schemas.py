from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    name: str
    address: str
    state: str
    gstin: str | None = None

class Item(BaseModel):
    name: str
    hsn: str
    qty: int
    rate: float
    gst: float

class PurchaseOrder(BaseModel):
    delivery_date: str
    order_date: str
    bill_from: Address
    bill_to: Address
    ship_to: Address
    items: List[Item]
