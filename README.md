# Flask Authentication System

A secure authentication system built using Flask, Flask-Login, and SQLAlchemy.

This project demonstrates user authentication features such as registration, login, password hashing, session management, protected routes, and secure file downloading.

---

## Features

- User Registration
- User Login
- Password Hashing using Werkzeug
- Flask-Login Session Management
- Protected Routes with `@login_required`
- Logout Functionality
- Flash Messages for Errors & Notifications
- Secure PDF Download Route
- SQLite Database Integration
- Dynamic Navbar using `current_user`

---

## Technologies Used

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Werkzeug Security
- HTML5
- CSS3
- SQLite

---

## Project Structure

```bash
003 Starting-Files-flask-auth-start/
│
├── static/
│   ├── css/
│   └── files/
│       └── cheat_sheet.pdf
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── secrets.html
│
├── main.py
├── users.db
└── README.md