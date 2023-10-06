import os
import click
from datetime import date
from database import SessionLocal
from models import User, Workout

@click.command()
@click.option("--username", prompt="Enter your username:", help="Your username to associate with the workout.")
@click.option("--exercise", prompt="Enter the exercise name:", help="Name of the exercise.")
@click.option("--duration", prompt="Enter the duration in minutes:", type=int, help="Duration of the exercise in minutes.")
def log_workout(username, exercise, duration):
    """Log a workout and store it in the database."""
    
    # Calculate calories burned (a basic formula for demonstration purposes)
    calories_burned = duration * 5.0
    
    # Store workout information in the database
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
    
    workout = Workout(
        date=date.today(),
        exercise=exercise,
        duration_minutes=duration,
        calories_burned=calories_burned,
        user=user,
    )
    db.add(workout)
    db.commit()
    
    click.echo(f"Workout logged successfully for user {username}.")

if __name__ == "__main__":
    log_workout()
