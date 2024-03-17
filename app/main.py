from fastapi import FastAPI
from app.models.bookings.router import booking
from app.models.users.router import user_router


app = FastAPI()

app.include_router(user_router)
app.include_router(booking)


