from app.database.datebase import async_session_maker
from app.database.bookings.models import Bookings
from sqlalchemy import select
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings
