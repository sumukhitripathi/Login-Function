# Flask Login App

This project is a simple Flask-based login application with a styled frontend and basic session-based authentication.

## Features

- Flask backend with login, dashboard, and logout routes
- Session-based authentication
- Frontend integrated with HTML, CSS, and JavaScript
- Credentials stored in a local `.env` file
- Static assets served through Flask

## Project Structure

```text
Login_page/
|-- app.py
|-- index.html
|-- .env
|-- .gitignore
|-- static/
|   |-- styles.css
|   |-- script.js
```

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone or download the project.
2. Open the project folder in your terminal.
3. Install Flask if needed:

```bash
pip install flask
```

## Environment Variables

Create a `.env` file in the project root with the login credentials.


## Running the App

Start the Flask server with:

```bash
python app.py
```

## Routes

- `/` - Login page
- `/dashboard` - Protected dashboard page
- `/logout` - Logs the user out and redirects to login

## How Login Works

- The user enters a username and password on the login page.
- Flask checks the values against `LOGIN_USERNAME` and `LOGIN_PASSWORD` from `.env`.
- If the credentials are valid, the app stores the username in the session and redirects to the dashboard.
- If the credentials are invalid, the app shows an error message.

## Notes

- This project is intended as a basic learning/demo app.
- For production use, store hashed passwords and use a stronger secret key.