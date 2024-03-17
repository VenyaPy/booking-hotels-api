from app.dao.base import BaseDAO
from app.models.users.models import Users


class UsersDAO(BaseDAO):
    model = Users