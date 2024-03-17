from fastapi import APIRouter, Depends
from app.models.users.models import Users
from app.models.users.dependencies import get_current_user
from app.models.bookings.schemas import SBooking
from app.models.bookings.dao import BookingDAO

booking = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
    )


@booking.get("")
async def get_booking(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@booking.post("")
async def add_booking(
        user: Users = Depends(get_current_user)
):
    await BookingDAO.add(user_id=user.id)
































