from pydantic import BaseModel, Field
from datetime import date


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class SHotel(BaseModel):
    address: str
    name: str
    stars: int