# Student-Subject Management API

A FastAPI-based REST API for managing students and subjects with encrypted student names for enhanced security.

## Features

- **Student Management**: Add, retrieve, update students with encrypted names
- **Subject Management**: Create and manage subjects
- **Security**: RSA encryption for student names
- **PostgreSQL**: Database with stored procedures
- **FastAPI**: Modern, fast web framework with automatic API documentation

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aashirzubair999/Fast_RSA_StudentSubject.git
   cd fastapi_studentsubject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=flask_student_subject_db
   DB_USER=postgres
   DB_PASSWORD=1234
   ```

5. **Set up the database**
   ```sql
   CREATE DATABASE flask_student_subject_db;
   ```
   Run the provided SQL scripts to create tables and stored procedures.

## Database Schema

### Subjects Table
```sql
CREATE TABLE subject (
    subjectid BIGINT PRIMARY KEY,
    subjectname VARCHAR(50) NOT NULL,
    subjectinfo TEXT
);
```

### Students Table
```sql
CREATE TABLE student (
    studentid BIGINT PRIMARY KEY,
    studentname BYTEA,  -- Encrypted student name
    fk_subjectid BIGINT,
    FOREIGN KEY (fk_subjectid) REFERENCES subject(subjectid) ON DELETE CASCADE
);
```

## Running the Application

### Development
```bash
uvicorn application:application --reload
```

### Production
```bash
uvicorn application:application 
```

The API will be available at: `http://localhost:8000`

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Home
- `GET /` - Welcome message

### Subjects
- `POST /subject/addsubject` - Add a new subject
  ```json
  {
    "subjectname": "Mathematics",
    "subjectinfo": "Advanced calculus and algebra"
  }
  ```

### Students
- `POST /student/addstudent` - Add a new student
  ```json
  {
    "studentname": "John Doe",
    "subjectid": 12345678
  }
  ```

- `GET /student/all/{subjectid}` - Get all students by subject ID
- `GET /student/{studentid}` - Get student by student ID
- `PUT /student/update/{studentid}` - Update student information

## Security Features

- **RSA Encryption**: Student names are encrypted using RSA-2048 before storage
- **Automatic Key Management**: RSA keys are automatically generated and managed
- **Secure Storage**: Encrypted data stored as BYTEA in PostgreSQL

## Project Structure

```
fastapi_studentsubject/
├── application.py          # Main FastAPI application
├── config.py              # Environment configuration
├── db.py                  # Database connection
├── models.py              # Pydantic models
├── rsa_utils.py           # RSA encryption utilities
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── routers/
    ├── home_router.py     # Home routes
    ├── student_router.py  # Student management routes
    └── subject_router.py  # Subject management routes
```

## Dependencies

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM
- **Psycopg2** - PostgreSQL adapter
- **Cryptography** - RSA encryption
- **Python-dotenv** - Environment management
- **Pydantic** - Data validation

## Stored Procedures

The project uses PostgreSQL stored procedures for all database operations:

- `sp_setsubjects()` - Add new subject
- `sp_setstudentbysubjectid()` - Add new student
- `sp_getstudentbysubjectid()` - Get students by subject
- `sp_getstudentbystudentid()` - Get student by ID
- `sp_updatestudentbystudentid()` - Update student

## Testing the API

### Using curl:

1. **Add a subject:**
   ```bash
   curl -X POST "http://localhost:8000/subject/addsubject" \
   -H "Content-Type: application/json" \
   -d '{"subjectname": "Computer Science", "subjectinfo": "Programming and algorithms"}'
   ```

2. **Add a student:**
   ```bash
   curl -X POST "http://localhost:8000/student/addstudent" \
   -H "Content-Type: application/json" \
   -d '{"studentname": "Alice Smith", "subjectid": 12345678}'
   ```

3. **Get students by subject:**
   ```bash
   curl "http://localhost:8000/student/all/12345678"
   ```

## Configuration

### Environment Variables
- `DB_HOST` - Database host
- `DB_PORT` - Database port
- `DB_NAME` - Database name
- `DB_USER` - Database user
- `DB_PASSWORD` - Database password

### RSA Keys
- RSA keys are automatically generated in `rsa_private_key.pem` and `rsa_public_key.pem`
- Keys are created on first run if they don't exist

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check PostgreSQL is running
   - Verify database credentials in `.env`
   - Ensure database exists

2. **404 Not Found**
   - Check if the server is running
   - Verify endpoint URLs
   - Check router registration in `application.py`

3. **Encryption Errors**
   - Delete `.pem` files to regenerate keys
   - Check file permissions

## License

This project is for educational purposes.

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For support, please check the API documentation at `/docs` or create an issue in the repository.