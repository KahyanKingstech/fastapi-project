from fastapi import APIRouter

router = APIRouter()

# Dummy data for users
students = [
    {"student_id": "STU001", "student_name": "Merlion", "gender": "Female", "email": "merlion@gmail.com", "phone": "0178907890", "course": "Introduction to Python"},
    {"student_id": "STU002", "student_name": "Alice", "gender": "Female", "email": "alice@gmail.com", "phone": "0123456789", "course": "Data Structures and Algorithms"},
    {"student_id": "STU003", "student_name": "Bob", "gender": "Male", "email": "bob@gmail.com", "phone": "0198765432", "course": "Web Development with FastAPI"},
    {"student_id": "STU004", "student_name": "Charlie", "gender": "Male", "email": "charlie@gmail.com", "phone": "0167890123", "course": "Database Management Systems"},
    {"student_id": "STU005", "student_name": "Diana", "gender": "Female", "email": "diana@gmail.com", "phone": "0187654321", "course": "Machine Learning Basics"},
    {"student_id": "STU006", "student_name": "Eva", "gender": "Female", "email": "eva@gmail.com", "phone": "0141234567", "course": "Mobile App Development"},
    {"student_id": "STU007", "student_name": "Frank", "gender": "Male", "email": "frank@gmail.com", "phone": "0192233445", "course": "Introduction to AI"},
    {"student_id": "STU008", "student_name": "Grace", "gender": "Female", "email": "grace@gmail.com", "phone": "0177766554", "course": "Cloud Computing Fundamentals"},
    {"student_id": "STU009", "student_name": "Hannah", "gender": "Female", "email": "hannah@gmail.com", "phone": "0134455667", "course": "JavaScript for Beginners"},
    {"student_id": "STU010", "student_name": "Irene", "gender": "Female", "email": "irene@gmail.com", "phone": "0162333445", "course": "Cybersecurity Basics"},
    {"student_id": "STU011", "student_name": "Jack", "gender": "Male", "email": "jack@gmail.com", "phone": "0145566778", "course": "Data Science with Python"},
    {"student_id": "STU012", "student_name": "Kevin", "gender": "Male", "email": "kevin@gmail.com", "phone": "0156677889", "course": "Networking Fundamentals"},
    {"student_id": "STU013", "student_name": "Lily", "gender": "Female", "email": "lily@gmail.com", "phone": "0174455668", "course": "Blockchain and Cryptocurrencies"},
    {"student_id": "STU014", "student_name": "Mike", "gender": "Male", "email": "mike@gmail.com", "phone": "0185566779", "course": "Introduction to Algorithms"},
    {"student_id": "STU015", "student_name": "Nina", "gender": "Female", "email": "nina@gmail.com", "phone": "0196677880", "course": "Advanced Python Programming"},
    {"student_id": "STU016", "student_name": "Oscar", "gender": "Male", "email": "oscar@gmail.com", "phone": "0167894321", "course": "Full-Stack Web Development"},
    {"student_id": "STU017", "student_name": "Paul", "gender": "Male", "email": "paul@gmail.com", "phone": "0189988776", "course": "Data Visualization with Python"},
    {"student_id": "STU018", "student_name": "Quinn", "gender": "Female", "email": "quinn@gmail.com", "phone": "0191122334", "course": "Artificial Intelligence Concepts"},
    {"student_id": "STU019", "student_name": "Rita", "gender": "Female", "email": "rita@gmail.com", "phone": "0172244665", "course": "Digital Marketing Fundamentals"},
    {"student_id": "STU020", "student_name": "Sam", "gender": "Male", "email": "sam@gmail.com", "phone": "0143344556", "course": "Game Development with Unity"}
]

# Define the GET endpoint for students
@router.get("/students")
def get_students():
    return students