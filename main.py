from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import course, student  # Import your routers

# Create FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include multiple routers
app.include_router(course.router, prefix="/api")
app.include_router(student.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}