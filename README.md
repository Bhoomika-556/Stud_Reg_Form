# Student Registration - Flask CRUD Example

A simple Flask application demonstrating CRUD (Create, Read, Update, Delete)
operations for student registration, using SQLite as the database.

## Project Structure

├── app.py
├── templates/
│ └── index.html
└── instance/
└── example.db (auto-generated on first run)


## Features

- **Create**: Register a new student with name, email, course, and age.
- **Read**: View all registered students in a table.
- **Update**: Edit an existing student's details.
- **Delete**: Remove a student record.

## Requirements

- Python 3.8+
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone or download the project files.
2. Install dependencies:

```bash
   pip install flask flask-sqlalchemy
```

## Running the App

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000/`.
On first run, Flask-SQLAlchemy will automatically create `instance/example.db`
with the required `student` table.

## Usage

1. Fill out the registration form on the homepage and click **Register Student**.
2. All registered students appear in the table below the form.
3. Click **Edit** next to a student to update their details, then click **Update Student**.
4. Click **Delete** next to a student to remove their record (confirmation required).

## Notes

- Email addresses must be unique; attempting to register a duplicate email will show an error.
- Change `app.secret_key` in `app.py` to a secure random value before deploying.
- Debug mode is enabled by default (`debug=True`); disable it in production.
