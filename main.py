from fastapi import FastAPI
import api1  # Import your API module

app = FastAPI()

# Include the router with a prefix
app.include_router(api1.router, prefix="/module1")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}