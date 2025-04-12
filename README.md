
# OFFER++ Project - Backend API for Client Management

This project implements a Case Management System backend with RESTful APIs to help social workers manage clients and track their success rates based on different interventions.

---


### User Story

As a user of the backend API's, I want to call API's that can retrieve, update, and delete information of clients who have already registered with the CaseManagment service so that I more efficiently help previous clients make better decisions on how to be gainfully employed.

### 

- Provide REST API endpoints so that the Frontend can use them to get information on an existing client.
- Document how to use the REST API.
- Choose and create a database to hold client information.
- Add tests.

---

## How to Use

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application Locally

```bash
uvicorn app.main:app --reload
```

### 3. Load Initial Data

```bash
python initialize_data.py
```

### 4. Access API Documentation

Visit Swagger UI at:

```
http://127.0.0.1:8080/docs
```

### 5. Login Information

| Username | Password |
|----------|----------|
| admin    | admin123 |

---

## API Endpoints

> These are the Sprint 3 newly added endpoints for Client Management.

- Create User
- Get All Clients
- Get Client by ID
- Update Client
- Delete Client
- Get Clients by Criteria
- Get Clients by Services
- Get Client's Services
- Get Clients by Success Rate
- Get Clients by Case Worker
- Update Client Services
- Create Case Assignment

Details of request parameters and response schemas are available in Swagger UI.

---

## Run the Application with Docker

### 1. Build Docker Image

```bash
docker build -t common-assessment-tool-app .
```

### 2. Run Docker Container

```bash
docker run -p 8080:8080 common-assessment-tool-app
```

### 3. Access API

```
http://127.0.0.1:8080/docs
```

---

## Run with Docker Compose

```bash
docker compose up
```

Stop the service:

```bash
docker compose down
```

---

## CI/CD Pipeline

We use GitHub Actions for Continuous Integration (CI).

### Features

- Auto runs on push/pull request
- Code linting with pylint
- Automated testing with pytest
- Dockerfile validation
- Docker image build & run verification

Configuration file: `.github/workflows/ci.yml`

---

## Access the Public Deployment

> Sprint 3 Update: The application is now deployed and accessible via the following public URL:

Visit:

```
https://commen-accessment-tool-app-v43vvietaq-uc.a.run.app/docs
```

---
