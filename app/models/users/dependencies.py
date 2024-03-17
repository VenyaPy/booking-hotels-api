from datetime import datetime
from app.models.users.dao import UsersDAO
from fastapi import Request, Depends
from jose import jwt, JWTError
from app.exeptions.exeptions import (TokenExpiredException,
                                     TokenAbsentException,
                                     IncorrectTokenFormatException,
                                     UserIsNotPresent)


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, "asdlajsdasASDASD", "HS256"
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresent
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresent
    return user



