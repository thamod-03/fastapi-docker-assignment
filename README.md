# FastAPI Docker REST API

A simple REST API application developed using **FastAPI** and containerized using **Docker Compose**.

This project demonstrates the process of building a Python web application, creating a Docker image, managing environment variables, running the application inside a Docker container, and exposing REST API endpoints.

---

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- python-dotenv

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
├── .dockerignore
├── .env.example
├── .gitignore
├── compose.yaml
├── Dockerfile
├── README.md
├── reflection.md
└── requirements.txt
```

---

# Running the Application

## Prerequisites

Make sure the following are installed:

- Docker Desktop
- Docker Compose

---

## Environment Configuration

This project uses environment variables to store application configuration.

Create a `.env` file in the project root directory.

Example:

```env
STUDENT_ID=your_student_id
STUDENT_NAME=your_name
```

A template file is provided:

```
.env.example
```

The `.env` file is ignored by Git to prevent exposing local configuration values.

Docker Compose automatically loads these variables into the container using:

```yaml
env_file:
  - .env
```

---

# Build and Start the Application

Clone the repository:

```bash
git clone https://github.com/thamod-03/fastapi-docker-assignment.git
```

Navigate into the project folder:

```bash
cd fastapi-docker-assignment
```

Create your `.env` file:

```bash
copy .env.example .env
```

Update the values according to your environment.

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

Returns application information loaded from environment variables.

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

Response:

```json
{
    "status": "ok"
}
```

---

# Docker Implementation

The application uses Docker to package the FastAPI service with all required dependencies.

## Docker Features Used

- Lightweight Python base image (`python:3.12-slim`)
- Dockerfile for image creation
- Docker Compose for container orchestration
- Environment variable management using `.env`
- Port mapping between host machine and container
- Uvicorn server for running the FastAPI application

---

# Docker Commands

## Build and Run

```bash
docker compose up --build
```

## Run in Background Mode

```bash
docker compose up -d
```

## View Running Containers

```bash
docker ps
```

## View Container Logs

```bash
docker compose logs
```

## Stop the Application

```bash
docker compose down
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

# Environment Security

Sensitive configuration values should not be committed to public repositories.

This project follows the practice:

```
.env              → Local configuration (Not committed)
.env.example      → Template shared publicly
```

The `.gitignore` file prevents accidental upload of private environment files.

---

# Limitations

- No database integration
- No authentication mechanism
- Designed as a simple REST API demonstration project
