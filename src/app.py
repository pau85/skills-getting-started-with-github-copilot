"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
    # Add 2 more sports related activities, 2 more artistic activities, and 2 more intellectual activities
    ,
    "Basketball Team": {
        "description": "Join the basketball team and compete in local tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["ian@mergington", "jon@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various art forms and create your own masterpieces",
        "schedule": "Tuesdays, 3:00 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["kim@mergington", "megan@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["brandon@mergington.edu", "michael@mergington.edu"]
    },
    "Drama Club": {
        "description": "Participate in theater productions and improv sessions",
        "schedule": "Wednesdays, 3:00 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["maude@mergington.edu", "paulette@mergington.edu"]
    },
    "Mathletes": {
        "description": "Compete in math competitions and improve problem-solving skills",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["shelly@mergington.edu", "justin@mergington.edu"]
    },
    "Science Club": {
        "description": "Explore scientific concepts through experiments and projects",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["bob@mergington.edu", "todd@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and participate in photo walks",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 10,
        "participants": ["theresa@mergington.edu", "aaron@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Validate student is not already signed up
    if email in activities[activity_name]["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
