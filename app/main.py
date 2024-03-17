from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from app.models.models import SBooking, SHotel
from app.database.bookings.router import booking
from app.database.users.router import user_router


app = FastAPI()

app.include_router(user_router)
app.include_router(booking)


