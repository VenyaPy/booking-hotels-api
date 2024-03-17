from app.dao.base import BaseDAO
from app.database.users.models import Users


class UsersDAO(BaseDAO):
    model = Users