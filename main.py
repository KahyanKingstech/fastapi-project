from fastapi import FastAPI
import course, student # Import your API module

app = FastAPI()

# Include the router with a prefix
app.include_router(course.router)
app.include_router(student.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}