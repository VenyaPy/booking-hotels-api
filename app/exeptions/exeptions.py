from fastapi import HTTPException, status


class Exceptions(HTTPException):
    status_code = 401
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(Exceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class IncorrectUsernameOrPasswordException(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"


class TokenExpiredException(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истёк"


class TokenAbsentException(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Некорректный формат токена"


class UserIsNotPresent(Exceptions):
    status_code = status.HTTP_401_UNAUTHORIZED




