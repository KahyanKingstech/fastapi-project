from fastapi import APIRouter

router = APIRouter()

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