from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    birth_date = Column(Date, nullable=True)
    created_at = Column('created_at', DateTime, default=func.now())
