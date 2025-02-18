from fastapi import APIRouter

router = APIRouter()

# Dummy data for users
users = [
    {"id": 1, "name": "John Doe", "username": "johndoe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "username": "janesmith", "email": "jane@example.com"},
    {"id": 3, "name": "Alice Johnson", "username": "alicej", "email": "alice@example.com"},
]

# Define the GET endpoint for users
@router.get("/users")
def get_users():
    return users