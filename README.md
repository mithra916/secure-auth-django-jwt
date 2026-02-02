🔒 Project Overview

This project implements a secure user authentication system using Django REST Framework and JWT (JSON Web Tokens). It features:

Registration with strong password validation

Login using JWT access and refresh tokens

Secure password storage using bcrypt hashing

Logout with token blacklisting

Full RESTful API design for easy integration with frontend applications

This setup is designed for resume-ready projects, demonstrating advanced backend skills and security best practices.

📦 Features
Feature	Description
Secure Passwords	All passwords are hashed using BCryptSHA256 before storing in the database.
Strong Password Policy	Enforces minimum 8 characters, combination of letters, numbers, and special characters.
JWT Authentication	Uses access and refresh tokens for secure session management.
Logout & Token Blacklist	Implements token revocation for immediate logout security.
REST API Endpoints	Fully functional endpoints for login, registration, refresh, and logout.
⚡ Tech Stack

Backend: Python 3.13, Django 6.0.1, Django REST Framework

Authentication: JWT via djangorestframework-simplejwt

Database: SQLite (default, can be replaced with PostgreSQL/MySQL)

Password Hashing: bcrypt (BCryptSHA256PasswordHasher)

🚀 Installation & Setup
# Clone the repository
git clone <YOUR_REPO_URL>
cd JWT-Auth-for-Flask  # or your project folder

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
pip install bcrypt djangorestframework-simplejwt

# Migrate database
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver

🔗 API Endpoints
Endpoint	Method	Description
/api/register/	POST	Register a new user
/api/login/	POST	Obtain JWT access & refresh tokens
/api/refresh/	POST	Refresh access token using refresh token
/api/logout/	POST	Blacklist the refresh token (logout)

Example Request (Login):

POST /api/login/
{
  "username": "testuser",
  "password": "Test@123"
}


Example Response:

{
  "access": "<JWT_ACCESS_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>"
}

🧩 How to Test

Use Postman or Insomnia to test API endpoints.

Do not try GET requests on JWT endpoints; they only accept POST.

/api/register/ → register user first

/api/login/ → get access & refresh tokens

/api/refresh/ → refresh access token

/api/logout/ → blacklist refresh token

🔧 Future Improvements

Integrate Django Allauth for social logins (Google, Facebook).

Add email verification for registration.

Switch database to PostgreSQL for production.

Implement rate limiting for brute-force attack prevention.

📌 Notes

This project is API-only, no frontend.

/ or /api/ alone will return 404 — normal behaviour.

Passwords are never stored in plain text.

🏆 Why This Project is Resume-worthy

Shows secure authentication implementation

Demonstrates JWT + token management

Demonstrates backend API development skills

Perfect to integrate with React/Next.js frontend for full-stack demo
