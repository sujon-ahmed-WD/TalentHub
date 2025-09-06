# Job Portal Project

## Overview
A Job Portal application with two types of users: **Employers** and **Job Seekers**.  
Users can register, login, and perform actions based on their roles. Features include job listings, applications, dashboards, resume management, and email notifications.

---

## Features

### 1. User Authentication (10 Marks)
- Roles: Employer, Job Seeker
- User registration, login, and logout
- Email verification after registration
- Only verified users can log in

### 2. Job Listings (5 Marks)
- Employers can create job listings
- Display key information: job title, company name, date posted
- Filter jobs by category

### 3. Job Details (5 Marks)
- View detailed job information
- Job Seekers can apply with resume and other details

### 4. User Dashboard (20 Marks)
- **Employer Dashboard:**
  - Manage posted jobs
  - View applications received
  - Update job details
- **Job Seeker Dashboard:**
  - Track job applications
  - Update resumes and profile

### 5. Job Categories (5 Marks)
- Categorize jobs by industries (e.g., IT, Healthcare, Finance)
- Filter job listings by category

### 6. Email Notifications (5 Marks)
- Notify Job Seekers on successful application
- Notify Employers on new application

### 7. Resume Management (10 Marks)
- Upload, update, and delete resumes
- Resumes stored securely

### 8. Application Status Tracking (10 Marks)
- Track application status (Pending, Reviewed, Rejected, Accepted)
- Employers can update application status

### 9. Employer Reviews (5 Marks)
- Job Seekers can leave reviews
- Reviews include ratings and comments

### 10. Deployment and Submission (5 Marks)
- Deployed on secure hosting platform
- Proper documentation included

### 11. Future Payment Gateway Integration (Placeholder)
- Potential support for premium features:
  - Featured Job Listings
  - Advanced recruitment tools
  - Payment history and invoices

---

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/register/` | Register a new user |
| POST   | `/api/login/` | Login user |
| POST   | `/api/logout/` | Logout user |
| GET    | `/api/verify-email/<token>/` | Verify user email |

### Jobs
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/jobs/` | List all jobs |
| POST   | `/api/jobs/` | Create a job (Employer only) |
| GET    | `/api/jobs/<id>/` | Job details |
| PUT    | `/api/jobs/<id>/` | Update job details (Employer only) |
| DELETE | `/api/jobs/<id>/` | Delete job (Employer only) |

### Applications
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/jobs/<id>/apply/` | Apply for a job |
| GET    | `/api/applications/` | View user applications |
| PUT    | `/api/applications/<id>/status/` | Update application status (Employer only) |

### Resumes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/resumes/` | Upload resume |
| GET    | `/api/resumes/` | List resumes |
| PUT    | `/api/resumes/<id>/` | Update resume |
| DELETE | `/api/resumes/<id>/` | Delete resume |

### Reviews
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/employers/<id>/reviews/` | Leave a review for an employer |
| GET    | `/api/employers/<id>/reviews/` | List all reviews for an employer |

---

## Installation

```bash
git clone <repository-url>
cd job-portal
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
