from app.models.bookings.models import Bookings
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings


    @classmethod
    async def add(cls):
        pass

