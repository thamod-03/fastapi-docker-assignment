# Docker FastAPI Assignment

## Student Details

Student ID: xxxxx
Name: xxxxx


## Project Description

A small REST API built using FastAPI and containerized using Docker.


## Docker Run Command

Build and start:

docker compose up --build


## API Endpoints

### GET /

URL:
http://localhost:5000/

Response:

{
 "student_id":"SE20260001",
 "name":"John Doe",
 "message":"Hello Docker! My FastAPI application is running inside a container."
}


### GET /health

URL:
http://localhost:5000/health

Response:

{
 "status":"ok"
}


## Stop Container

docker compose down


## Limitations

- No database integration
- Simple demonstration API only
- Designed for Docker containerization practice
