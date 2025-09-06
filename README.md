
# Job Portal Django Project

## Overview

This project is a **Job Portal** built with Django and Django REST Framework (DRF) that allows **Employers** to post jobs and **Job Seekers** to browse and apply for jobs. The platform supports user authentication, email verification, role-based access, and job management.

![Job Portal Overview]
*Diagram: High-level workflow of the job portal*

---

## Features

1. **User Authentication**

   * Two roles: **Employer** and **Job Seeker**
   * Registration, login, logout
   * Email verification after registration
   * Only verified users can log in

![Authentication Flow] 
*Diagram: How user authentication and verification work*

2. **Job Listings**

   * Employers can create, update, and delete job postings
   * Job Seekers can view job listings
   * Filter and search jobs by title, category, location, etc.

![Job Management] 
*Diagram: Job CRUD operations*

3. **Job Applications**

   * Job Seekers can apply for jobs
   * Employers can view applications for their posted jobs

![Application Flow]
*Diagram: Job application workflow*

4. **Categories**

   * Jobs can be categorized
   * CRUD operations for categories (for admin/employer)

5. **Permissions**

   * Role-based access:

     * Only Employers can create jobs
     * Only Job Seekers can apply
     * Admin can manage everything

---

## API Endpoints

> Base URL: `/api/`

### 1. Authentication

| Method | Endpoint                        | Description         |
| ------ | ------------------------------- | ------------------- |
| POST   | `/auth/register/`               | Register a new user |
| POST   | `/auth/login/`                  | User login          |
| POST   | `/auth/logout/`                 | User logout         |
| GET    | `/auth/verify-email/?token=...` | Verify user email   |

### 2. Job Management

| Method | Endpoint                 | Description                      |
| ------ | ------------------------ | -------------------------------- |
| GET    | `/jobs/`                 | List all jobs                    |
| POST   | `/jobs/create/`          | Create a new job (Employer only) |
| GET    | `/jobs/<job_id>/`        | Retrieve job details             |
| PUT    | `/jobs/<job_id>/update/` | Update job (Employer only)       |
| DELETE | `/jobs/<job_id>/delete/` | Delete job (Employer only)       |

### 3. Job Applications

| Method | Endpoint                       | Description                                 |
| ------ | ------------------------------ | ------------------------------------------- |
| POST   | `/jobs/<job_id>/apply/`        | Apply for a job (Job Seeker only)           |
| GET    | `/jobs/<job_id>/applications/` | List applications for a job (Employer only) |

### 4. Categories

| Method | Endpoint                   | Description                          |
| ------ | -------------------------- | ------------------------------------ |
| GET    | `/categories/`             | List all categories                  |
| POST   | `/categories/create/`      | Create new category (Admin/Employer) |
| PUT    | `/categories/<id>/update/` | Update category (Admin/Employer)     |
| DELETE | `/categories/<id>/delete/` | Delete category (Admin/Employer)     |

---

## Example Requests

### Register User

```bash
POST /api/auth/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",
  "role": "job_seeker"
}
```

### Create Job

```bash
POST /api/jobs/create/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Python Developer",
  "description": "We are looking for a Python Developer...",
  "category": 1,
  "location": "Dhaka",
  "salary": "50000"
}
```

### Apply for Job

```bash
POST /api/jobs/5/apply/
Authorization: Bearer <token>
Content-Type: application/json

{
  "resume": "resume.pdf",
  "cover_letter": "I am interested in this position..."
}
```

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd job-portal
```

2. Create virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create superuser:

```bash
python manage.py createsuperuser
```

6. Run server:

```bash
python manage.py runserver
```

---

## Notes

* Make sure email backend is configured for email verification.
* Use DRF's browsable API or Postman to test endpoints.
* Pagination, search, and filters can be added via query parameters.

---


