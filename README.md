# ZenLTD Backend

A FastAPI backend application with PostgreSQL database and Alembic migrations.

## Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Configuration

Create a `.env` file in the project root with your PostgreSQL configuration:

```env
# Database Configuration
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=zenltd
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password_here

# Application Settings
PROJECT_NAME=ZenLTD Backend
```

### 3. Database Setup

#### Option A: Using the setup script
```bash
python setup_database.py
```

#### Option B: Manual setup
1. Create the database in PostgreSQL:
```sql
CREATE DATABASE zenltd;
```

2. Run the setup script to create tables:
```bash
python setup_database.py
```

### 4. Alembic Migrations

Initialize and run migrations:

```bash
# Create initial migration
alembic revision --autogenerate -m "Initial migration"

# Apply migrations
alembic upgrade head
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## Project Structure

```
zenltd-backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes.py
│   ├── core/
│   │   ├── config.py      # Database and app configuration
│   │   └── database.py    # Database connection and session
│   ├── models/
│   │   ├── __init__.py    # Model imports
│   │   └── user.py        # User model
│   ├── schemas/           # Pydantic schemas
│   └── main.py           # FastAPI application
├── alembic/              # Migration files
├── alembic.ini          # Alembic configuration
├── requirements.txt     # Python dependencies
├── setup_database.py   # Database setup script
└── README.md
```

## Database Models

### User Model
- `id`: Primary key
- `email`: Unique email address
- `username`: Unique username
- `full_name`: Full name (optional)
- `hashed_password`: Hashed password
- `is_active`: Account status
- `is_superuser`: Admin privileges
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## API Endpoints

- `GET /api/v1/`: API information
- `GET /docs`: Interactive API documentation (Swagger UI)
- `GET /redoc`: Alternative API documentation

## Development

### Adding New Models

1. Create a new model file in `app/models/`
2. Import the model in `app/models/__init__.py`
3. Generate and run migrations:
```bash
alembic revision --autogenerate -m "Add new model"
alembic upgrade head
```

### Database Migrations

- **Create migration**: `alembic revision --autogenerate -m "Description"`
- **Apply migrations**: `alembic upgrade head`
- **Rollback migration**: `alembic downgrade -1`
- **Check migration status**: `alembic current`
- **View migration history**: `alembic history`

## Troubleshooting

### Common Issues

1. **Database connection error**: Check your `.env` file and ensure PostgreSQL is running
2. **Import errors**: Make sure you're in the project root directory
3. **Migration errors**: Check that all models are properly imported in `app/models/__init__.py`

### PostgreSQL Setup

If you need to install PostgreSQL:

**Windows:**
- Download from https://www.postgresql.org/download/windows/
- Use the default port 5432

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
``` 
