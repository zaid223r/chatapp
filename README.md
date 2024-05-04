
Chat Application
===
This real-time chat application harnesses the power of Django's Model-View-Template architecture and JavaScript WebSockets to create a seamless and interactive chatting experience. With Django handling the backend logic and data management through its robust MVT framework, and WebSockets facilitating instant communication between users in real-time.

## Table of Contents

[TOC]

## Beginners Guide

If you are a total beginner to this, start here!

1. Clone the repository:
    ```bash
    git clone https://github.com/zaid223r/djangochat.git
    ```
2. Navigate to the project directory:
    ```bash
    cd djangochat
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```
The application should now be accessible at http://localhost:8000.

Usage
---
1. Register a new account or log in with existing credentials.
2. Once logged in, you can:
    * Choose the chat room.
    * Write messages in the chat room and communicate with others.
    * See messages from others in the same chat room. 
    * logout any time.

Features
---
* User authentication: Users can register, log in, and log out.
* User authintication with Google.
* Real-time chat.
* More than one room to chat in.

Project Structure
---
```bash
.
├── chatapp/
│   ├── asgi.py            # ASGI config for chatapp
│   ├── settings.py        # Django settings for chatapp
│   ├── urls.py            # URL routing for chatapp
│   └── wsgi.py            # WSGI config for chatapp
├── main/
│   ├── migrations/        # Database migrations for main app
│   ├── templates/         # HTML templates for main app
│   ├── admin.py           # Admin configuration for main app
│   ├── apps.py            # Configuration for main app
│   ├── forms.py           # Forms for main app
│   ├── models.py          # Database models for main app
│   ├── urls.py            # URL routing for main app
│   └── views.py           # View functions for main app
├── room/
│   ├── migrations/        # Database migrations for room app
│   ├── templates/         # HTML templates for room app
│   ├── admin.py           # Admin configuration for room app
│   ├── apps.py            # Configuration for room app
│   ├── consumers.py       # WebSocket consumers for room app
│   ├── models.py          # Database models for room app
│   ├── routing.py         # WebSocket routing for room app
│   ├── urls.py            # URL routing for room app
│   └── views.py           # View functions for room app
├── manage.py              # Django's command-line utility for administrative tasks
├── requirements.txt       # List of Python dependencies
└── README.md              # README file for the project

```
NOTES
---
* User authintication with Google won't work until you do some configurations in Google Cloud. [Read this](https://medium.com/@infowithkiiru/django-user-registration-with-google-67524cce5ab7)
* Make Super user and make a room in the admin page before using the web application.
```bash
python manage.py createsuperuser
```
* Sign in with that user at http://localhost:8000/admin
