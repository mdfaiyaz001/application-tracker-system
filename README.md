# Application Tracker System

A FastAPI backend project to track job applications with CRUD operations and SQL database integration.

## Project Overview

Application Tracker System is a backend application designed to help users manage and track their job applications. Users can store important details such as company name, job role, application status, applied date, and notes. This project is useful for students, freshers, and job seekers who want to organize their placement or recruitment process in one place.

The project demonstrates backend development concepts such as REST API creation, CRUD operations, database connectivity, request validation, and API testing using Swagger UI.

## Features

- Add new job applications
- View all job applications
- View a specific application by ID
- Update application details
- Delete application records
- Store application data using SQLite database
- Test APIs using Swagger UI
- Simple and beginner-friendly backend structure

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Git
- GitHub
- VS Code

## Requirements

Before running this project, make sure you have the following installed:

- Python 3.x
- pip
- Git
- VS Code or any code editor

## Project Structure

```text
application-tracker-system/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── screenshots/
    └── swagger-ui.png
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home route to check API status |
| POST | `/applications/` | Add a new job application |
| GET | `/applications/` | Get all job applications |
| GET | `/applications/{application_id}` | Get a specific application by ID |
| PUT | `/applications/{application_id}` | Update an application |
| DELETE | `/applications/{application_id}` | Delete an application |

## Screenshots

### Swagger API Documentation

![Swagger UI](screenshots/swagger-ui.png)

## How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/mdfaiyaz001/application-tracker-system.git
```

### 2. Open the Project Folder

```bash
cd application-tracker-system
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

If the above command does not work, use:

```bash
python -m uvicorn main:app --reload
```

### 5. Open the Application

Open the following URL in your browser:

```text
http://127.0.0.1:8000
```

### 6. Open API Documentation

Open the Swagger UI using:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI allows users to test all API endpoints for adding, viewing, updating, and deleting job applications.

## Sample Request Body

Use this sample JSON while testing the POST API:

```json
{
  "company_name": "Infosys",
  "job_role": "Python Developer",
  "status": "Applied",
  "applied_date": "2026-05-06",
  "notes": "Applied through off-campus recruitment portal"
}
```

## Sample Response

```json
{
  "company_name": "Infosys",
  "job_role": "Python Developer",
  "status": "Applied",
  "applied_date": "2026-05-06",
  "notes": "Applied through off-campus recruitment portal",
  "id": 1
}
```

## What I Learned

- Built REST APIs using FastAPI
- Implemented CRUD operations
- Connected FastAPI with SQLite database
- Used SQLAlchemy ORM for database operations
- Used Pydantic for request and response validation
- Tested APIs using Swagger UI
- Managed project files using Git and GitHub

## Future Improvements

- Add user authentication
- Add search by company name
- Add filter by application status
- Add MySQL database support
- Add frontend dashboard
- Add deployment support

## Author

**MD Faiyaz**  
Python Backend Developer | AIML Student
