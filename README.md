# FastAPI Docker REST API

A simple REST API application developed using **FastAPI** and containerized using **Docker Compose**.

This project demonstrates the process of building a Python web application, creating a Docker image, running the application inside a container, and exposing REST API endpoints.

---

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Docker
- Docker Compose

---

## Project Structure

```
fastapi-docker-assignment
│
├── app
│   └── main.py
│
├── evidence
│   ├── compose-up.png
│   ├── container-running.png
│   ├── health-api.png
│   └── home-api.png
│
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── README.md
└── reflection.md
```

---

# Running the Application

## Prerequisites

Make sure the following are installed:

- Docker Desktop
- Docker Compose

---

## Build and Start the Application

Clone the repository:

```bash
git clone https://github.com/thamod-03/fastapi-docker-assignment.git
```

Navigate into the project folder:

```bash
cd fastapi-docker-assignment
```

Build and run the application:

```bash
docker compose up --build
```

The API will be available at:

```
http://localhost:5000
```

---

# API Endpoints

## Home Endpoint

### GET /

Returns application information.

URL:

```
http://localhost:5000/
```

Example response:

```json
{
    "student_id": "XXXXXXXX",
    "name": "Example Name",
    "message": "Hello Docker! My FastAPI application is running inside a container."
}
```

---

## Health Check Endpoint

### GET /health

Used to verify that the API service is running correctly.

URL:

```
http://localhost:5000/health
```

Example response:

```json
{
    "status": "ok"
}
```

---

# Docker Implementation

The application uses Docker to package the FastAPI service with all required dependencies.

## Docker Features Used

- Python lightweight base image (`python:3.12-slim`)
- Dockerfile for image creation
- Docker Compose for container management
- Port mapping between host machine and container
- Uvicorn server for running the FastAPI application

---

# Docker Commands

## Build and Run

```bash
docker compose up --build
```

## View Running Containers

```bash
docker ps
```

## Stop the Application

```bash
docker compose down
```

## View Container Logs

```bash
docker compose logs
```

---

# Testing

The API was tested using:

- Browser requests
- FastAPI endpoints
- Docker container execution

Evidence screenshots are available in the `evidence` directory.

Included evidence:

- Docker Compose build and startup
- Running container status
- Home endpoint response
- Health endpoint response

---

# Environment Configuration

For future improvements, sensitive configuration values can be managed using environment variables.

Example:

```
.env
```

```
STUDENT_ID=your_student_id
STUDENT_NAME=your_name
```

Environment files containing private values should not be uploaded to public repositories.

---

# Limitations

- No database integration
- No authentication mechanism
- Designed as a simple REST API demonstration project

