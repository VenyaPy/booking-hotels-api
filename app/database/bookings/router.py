from fastapi import APIRouter
from app.database.datebase import async_session_maker
from app.database.bookings.models import Bookings
from sqlalchemy import select
from app.database.bookings.dao import BookingDAO
from app.database.bookings.schemas import SBooking


booking = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
    )


@booking.get("")
async def get_booking() -> SBooking:
    return await BookingDAO.find_all()


































