from sqlalchemy import Column, Integer, String, JSON, Date, ForeignKey, Computed, VARCHAR
from app.database.datebase import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)