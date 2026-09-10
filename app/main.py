from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


student_id = os.getenv("STUDENT_ID")
student_name = os.getenv("STUDENT_NAME")


@app.get("/")
def home():
    return {
        "student_id": student_id,
        "name": student_name,
        "message": "Hello Docker! My FastAPI application is running inside a container."
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
