from fastapi import APIRouter
from app.database.datebase import async_session_maker
from app.database.bookings.models import Bookings
from sqlalchemy import select
from app.database.bookings.repo import BookingDAO


booking = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
    )


@booking.get("")
async def get_booking():
    return await BookingDAO.find_all()

