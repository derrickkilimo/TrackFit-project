from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base 

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    workouts = relationship("Workout", back_populates="user")

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    exercise = Column(String)
    duration_minutes = Column(Integer)
    calories_burned = Column(Float)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="Workouts")

