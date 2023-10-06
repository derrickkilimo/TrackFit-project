from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import User, Workout  # Import your models from your database.py

# Create a SQLAlchemy engine and session
DATABASE_URL = "sqlite:///./test.db"  # Adjust the database URL as needed
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Example usage: Query the user table
session = SessionLocal()

def get_user_by_username(username: str):
    return session.query(User).filter(User.username == username).first()


