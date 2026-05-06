# Application Tracker System

A FastAPI backend project to track job applications with CRUD operations and SQL database integration.

## Project Overview

Application Tracker System helps users manage their job applications. Users can add company details, job role, application status, applied date, and notes. This project is useful for students and job seekers to track their placement and recruitment process.

## Features

- Add new job applications
- View all applications
- View application by ID
- Update application status
- Delete application records
- Store data using SQLite database
- Test APIs using Swagger UI

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home route |
| POST | /applications/ | Add new application |
| GET | /applications/ | Get all applications |
| GET | /applications/{id} | Get application by ID |
| PUT | /applications/{id} | Update application |
| DELETE | /applications/{id} | Delete application |

## Screenshots

### Swagger API Documentation

![Swagger UI](screenshots/swagger-ui.png)

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/mdfaiyaz001/application-tracker-system.git
### 2. Open project folder

```bash
cd application-tracker-system
This project is designed to run locally as a FastAPI-based backend application. Users can clone the repository, install the required dependencies from requirements.txt, and start the development server using Uvicorn. Once the server is running, the automatically generated Swagger UI can be accessed at http://127.0.0.1:8000/docs, allowing users to interact with and test all available REST API endpoints for creating, retrieving, updating, and deleting job application records.
