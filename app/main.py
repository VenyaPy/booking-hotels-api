from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from app.models.models import SBooking, SHotel
from app.database.bookings.router import booking


app = FastAPI()

app.include_router(booking)

# VARIANT 1 response_model
@app.get("/hotels", response_model=list[SHotel])
def get_hotels(data_from: date,
               data_to: date,
               location: Optional[str] = None,
               stars: Optional[int] = Query(None, ge=1, le=5),
               has_spa: Optional[bool] = None):


    hotels = [
        {
            "address": "Гагарина 156",
            "name": "Sus Hotel",
            "stars": 5
        }
    ]

    return data_from, data_to


class HotelsC:
    def __init__(self,
                 data_from: date,
                 data_to: date,
                 location: Optional[str] = None,
                 stars: Optional[int] = Query(None, ge=1, le=5),
                 has_spa: Optional[bool] = None
                 ):
        self.data_from = data_from
        self.data_to = data_to
        self.location = location
        self.stars = stars
        self.has_spa = has_spa



@app.get("/hotelss")
def get_hotelss(seatch_args: HotelsC = Depends()):

    hotels = [
        {
            "address": "Гагарина 156",
            "name": "Sus Hotel",
            "stars": 5
        }
    ]


    return seatch_args


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass

