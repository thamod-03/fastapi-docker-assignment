from fastapi import FastAPI

app = FastAPI(
    title="Docker FastAPI Assignment",
    description="Containerized API using FastAPI",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "student_id": "244078P",
        "name": "G.T. Idusara",
        "message": "Hello Docker! My FastAPI application is running inside a container."
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
