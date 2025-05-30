
# OFFER++ Project - Backend API for Client Management

## Project -- Feature Development Backend: Create CRUD API's for Client

### User Story

As a user of the backend API's, I want to call API's that can retrieve, update, and delete information of clients who have already registered with the CaseManagment service so that I more efficiently help previous clients make better decisions on how to be gainfully employed.

### Acceptance Criteria

- Provide REST API endpoints so that the Frontend can use them to get information on an existing client.
- Document how to use the REST API
- Choose and create a database to hold client information
- Add tests

---

## Project Overview

This project contains the model used for the project that based on the input information will give the social workers the clients baseline level of success and what their success will be after certain interventions.

The model works off of dummy data of several combinations of clients alongside the interventions chosen for them as well as their success rate at finding a job afterward. The model will be updated by the case workers by inputting new data for clients with their updated outcome information, and it can be updated on a daily, weekly, or monthly basis.

This also has an API file to interact with the front end, and logic in order to process the interventions coming from the front end. This includes functions to clean data, create a matrix of all possible combinations in order to get the ones with the highest increase of success, and output the results in a way the front end can interact with.

---

## How to Use

1. In the virtual environment you've created for this project, install all dependencies in requirements.txt

```bash
pip install -r requirements.txt
```

2. Run the app

```bash
uvicorn app.main:app --reload
```

3. Load data into database

```bash
python initialize_data.py
```

4. Go to SwaggerUI

```
http://127.0.0.1:8080/docs
```

5. Log in as admin

| Username | Password |
|----------|----------|
| admin    | admin123 |

6. Click on each endpoint to use

- Create User
- Get Clients
- Get Client by ID
- Update Client
- Delete Client
- Get Clients by Criteria
- Get Clients by Services
- Get Clients Services
- Get Clients by Success Rate
- Get Clients by Case Worker
- Update Client Services
- Create Case Assignment

---

## How to run the application with Docker

### Prerequisites

- Docker installed on your machine. Visit [Docker's website](https://www.docker.com/get-started) for installation instructions.

1. Build the Docker image:

```bash
docker build -t common-assessment-tool-app .
```

2. Run the application:

```bash
docker run -p 8080:8080 common-assessment-tool-app
```

3. Go to SwaggerUI

```
http://127.0.0.1:8080/docs
```

---

## How to run the application with Docker Compose

To start the service using Docker Compose, run:

```bash
docker compose up
```

To stop the service, run:

```bash
docker compose down
```

---

## CI/CD Pipeline Implementation

This repository implements a Continuous Integration (CI) pipeline using GitHub Workflows. The pipeline automates the process of code validation, testing, and Docker container verification to ensure high code quality and reliable deployment.

### CI Pipeline Features

The CI pipeline performs the following operations:

- Automatically runs on push or pull request events to main/master branches
- Executes code linting with Pylint to maintain code quality
- Runs automated tests with pytest
- Validates Dockerfile syntax
- Builds the Docker image
- Runs the container to verify it functions as expected

### Triggering the CI Pipeline

The CI pipeline is automatically triggered when:

- Code is pushed to the main/master branch
- A pull request is opened against the main/master branch

### Viewing CI Results

Go to the "Actions" tab in the GitHub repository, select the workflow run you want to examine, and view the results of each job and step.

### Pipeline Configuration

The CI pipeline is defined in `.github/workflows/ci.yml` and consists of the following jobs:

#### Test Job

- Sets up Python 3.11
- Installs project dependencies
- Runs Pylint for code linting
- Executes pytest tests

#### Docker Job

- Verifies Dockerfile syntax
- Builds the Docker image
- Runs the container and tests connectivity
- Verifies the application is accessible

### Development Notes

The pipeline enforces code quality standards using Pylint. Test failures or Docker verification issues will cause the workflow to fail. The CI pipeline will generate test reports for review.

### Modifying the CI Pipeline

To modify the CI pipeline:

1. Edit the `.github/workflows/ci.yml` file.
2. Commit and push your changes.
3. The updated workflow will be used for subsequent runs.

By using this CI pipeline, we ensure that code changes meet quality standards and the application can be reliably containerized before deployment.

---

## How to access the public address

Visit:

```
https://commen-accessment-tool-app-v43vvietaq-uc.a.run.app/docs
```

---

## Automatic Deployment Pipeline

### Overview
This repository implements a Continuous Deployment (CD) pipeline that automatically deploys our backend application to a public cloud endpoint whenever a new release is created. This automation ensures our team can quickly and reliably make new releases without manual deployment steps.


### How the CD Pipeline Works
Our deployment pipeline uses GitHub Workflows to automate the deployment process:

When a release is created from the master branch, the CD workflow is automatically triggered
The workflow builds a Docker container with the latest code
The container is then deployed to our cloud infrastructure
The application is automatically restarted with the new version

### Creating a New Release
To deploy a new version of the application:
Ensure all changes are merged to the master branch
Go to the "Releases" section in the GitHub repository
Click "Draft a new release"
Create a new tag (e.g., v1.0.1)
Add a title and description for the release
Click "Publish release"

The CD pipeline will automatically start and deploy the latest version to the public endpoint.
Monitoring Deployments
You can monitor the status of deployments:

Go to the "Actions" tab in the repository
Look for the most recent "CD Pipeline" workflow run
Check the logs for detailed information about the deployment process

If a deployment fails, the workflow logs will provide error information for troubleshooting.

### Local Development
For local development, see the main README for instructions on running the application using Docker or directly with Python.