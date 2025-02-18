from fastapi import APIRouter

router = APIRouter()

# Dummy data for users
students = [
    {"student_id": "STU001", "student_name": "Merlion", "Gender": "Female", "Email": "merlion@gmail.com", "phone": "0178907890", "course": "Introduction to Python"},
    {"student_id": "STU002", "student_name": "Alice", "Gender": "Female", "Email": "alice@gmail.com", "phone": "0123456789", "course": "Data Structures and Algorithms"},
    {"student_id": "STU003", "student_name": "Bob", "Gender": "Male", "Email": "bob@gmail.com", "phone": "0198765432", "course": "Web Development with FastAPI"},
    {"student_id": "STU004", "student_name": "Charlie", "Gender": "Male", "Email": "charlie@gmail.com", "phone": "0167890123", "course": "Database Management Systems"},
    {"student_id": "STU005", "student_name": "Diana", "Gender": "Female", "Email": "diana@gmail.com", "phone": "0187654321", "course": "Machine Learning Basics"},
    {"student_id": "STU006", "student_name": "Eva", "Gender": "Female", "Email": "eva@gmail.com", "phone": "0141234567", "course": "Mobile App Development"},
    {"student_id": "STU007", "student_name": "Frank", "Gender": "Male", "Email": "frank@gmail.com", "phone": "0192233445", "course": "Introduction to AI"},
    {"student_id": "STU008", "student_name": "Grace", "Gender": "Female", "Email": "grace@gmail.com", "phone": "0177766554", "course": "Cloud Computing Fundamentals"},
    {"student_id": "STU009", "student_name": "Hannah", "Gender": "Female", "Email": "hannah@gmail.com", "phone": "0134455667", "course": "JavaScript for Beginners"},
    {"student_id": "STU010", "student_name": "Irene", "Gender": "Female", "Email": "irene@gmail.com", "phone": "0162333445", "course": "Cybersecurity Basics"},
    {"student_id": "STU011", "student_name": "Jack", "Gender": "Male", "Email": "jack@gmail.com", "phone": "0145566778", "course": "Data Science with Python"},
    {"student_id": "STU012", "student_name": "Kevin", "Gender": "Male", "Email": "kevin@gmail.com", "phone": "0156677889", "course": "Networking Fundamentals"},
    {"student_id": "STU013", "student_name": "Lily", "Gender": "Female", "Email": "lily@gmail.com", "phone": "0174455668", "course": "Blockchain and Cryptocurrencies"},
    {"student_id": "STU014", "student_name": "Mike", "Gender": "Male", "Email": "mike@gmail.com", "phone": "0185566779", "course": "Introduction to Algorithms"},
    {"student_id": "STU015", "student_name": "Nina", "Gender": "Female", "Email": "nina@gmail.com", "phone": "0196677880", "course": "Advanced Python Programming"},
    {"student_id": "STU016", "student_name": "Oscar", "Gender": "Male", "Email": "oscar@gmail.com", "phone": "0167894321", "course": "Full-Stack Web Development"},
    {"student_id": "STU017", "student_name": "Paul", "Gender": "Male", "Email": "paul@gmail.com", "phone": "0189988776", "course": "Data Visualization with Python"},
    {"student_id": "STU018", "student_name": "Quinn", "Gender": "Female", "Email": "quinn@gmail.com", "phone": "0191122334", "course": "Artificial Intelligence Concepts"},
    {"student_id": "STU019", "student_name": "Rita", "Gender": "Female", "Email": "rita@gmail.com", "phone": "0172244665", "course": "Digital Marketing Fundamentals"},
    {"student_id": "STU020", "student_name": "Sam", "Gender": "Male", "Email": "sam@gmail.com", "phone": "0143344556", "course": "Game Development with Unity"}
]

# Define the GET endpoint for students
@router.get("/students")
def get_students():
    return students