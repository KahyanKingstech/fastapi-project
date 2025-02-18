from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI()

# Create a router for your endpoints
router = APIRouter()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (you can restrict this to specific domains if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Dummy data for courses
courses = [
    {"course_id": "CRS1090", "course_name": "Introduction to Python", "description": "Learn the basics of Python programming."},
    {"course_id": "CRS1091", "course_name": "Data Structures and Algorithms", "description": "Study fundamental data structures and algorithms."},
    {"course_id": "CRS1092", "course_name": "Web Development with FastAPI", "description": "Learn to build web applications using FastAPI."},
    {"course_id": "CRS1093", "course_name": "Database Management Systems", "description": "Explore relational and non-relational databases."},
    {"course_id": "CRS1094", "course_name": "Machine Learning Basics", "description": "Understand the basics of machine learning algorithms."}
]

# Define the GET endpoint for courses
@router.get("/courses")
def get_courses():
    return courses

# Include the router in the app
app.include_router(router)

