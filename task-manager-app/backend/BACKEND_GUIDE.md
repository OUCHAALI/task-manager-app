# Backend Setup & Usage Guide

## 📁 Backend Structure

```
backend/
├── app/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # FastAPI application entry point
│   ├── db.py                # SQLite database configuration
│   ├── models.py            # SQLAlchemy ORM & Pydantic schemas
│   └── routes.py            # CRUD API endpoints
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container configuration
└── .gitignore              # Git ignore rules
```

## 🚀 Running the Backend

### Prerequisites
- Python 3.8+
- Dependencies installed: `pip install -r requirements.txt`

### Start the Development Server

```bash
# Navigate to backend directory
cd backend

# Run with uvicorn (with hot reload)
uvicorn app.main:app --reload --port 8000

# Or run directly with Python
python app/main.py
```

The API will be available at: **http://localhost:8000**

## 📚 API Documentation

### Interactive Docs (Swagger UI)
- URL: `http://localhost:8000/docs`

### ReDoc Documentation
- URL: `http://localhost:8000/redoc`

## 🔌 API Endpoints

### Get All Tasks
```
GET /api/tasks
Response: [TaskResponse]
```

### Get Single Task
```
GET /api/tasks/{task_id}
Response: TaskResponse
```

### Create Task
```
POST /api/tasks
Body: {
  "title": "string",
  "description": "string (optional)",
  "completed": false
}
Response: TaskResponse
```

### Update Task
```
PUT /api/tasks/{task_id}
Body: {
  "title": "string (optional)",
  "description": "string (optional)",
  "completed": boolean (optional)
}
Response: TaskResponse
```

### Delete Task
```
DELETE /api/tasks/{task_id}
Response: 204 No Content
```

### Health Check
```
GET /health
Response: {"status": "healthy", "message": "..."}
```

## 💾 Database

- **Type**: SQLite
- **File**: `tasks.db` (auto-created in backend directory)
- **Tables**: `tasks`

### Task Schema
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(2000),
    completed BOOLEAN DEFAULT FALSE
)
```

## 📋 File Descriptions

### `db.py` - Database Configuration
- SQLite engine initialization
- SessionLocal factory
- Base declarative class
- Database initialization function (`init_db()`)
- Dependency injection helper (`get_db()`)

### `models.py` - Data Models
- **Task**: SQLAlchemy ORM model
- **TaskBase**: Base Pydantic schema with common fields
- **TaskCreate**: Schema for POST requests
- **TaskUpdate**: Schema for PUT requests (all fields optional)
- **TaskResponse**: Schema for responses (includes ID)

### `main.py` - FastAPI Application
- FastAPI app initialization
- CORS middleware configuration
- Database initialization
- Route registration
- Root endpoint (`GET /`)
- Health check endpoint (`GET /health`)

### `routes.py` - API Endpoints
- **GET /tasks**: List all tasks
- **GET /tasks/{id}**: Get single task
- **POST /tasks**: Create task
- **PUT /tasks/{id}**: Update task
- **DELETE /tasks/{id}**: Delete task

All endpoints include:
- Dependency injection for database sessions
- Comprehensive error handling
- Logging
- HTTP status codes
- Pydantic validation

## 🔍 Testing

### List Tasks
```bash
curl http://localhost:8000/api/tasks
```

### Create Task
```bash
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","description":"Study basics","completed":false}'
```

### Update Task
```bash
curl -X PUT http://localhost:8000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'
```

### Delete Task
```bash
curl -X DELETE http://localhost:8000/api/tasks/1
```

## 🔧 Configuration

Set environment variable to use different database:
```bash
export DATABASE_URL="sqlite:///./custom_tasks.db"
uvicorn app.main:app --reload
```

## 📝 Logging

Logs are printed to console with format:
```
2025-11-22 02:33:36,541 - app.db - INFO - Database tables initialized
```

To enable SQL query logging, set `echo=True` in `db.py`'s `create_engine()` call.

## ✅ Verification

Backend is working correctly if:
1. ✓ No import errors
2. ✓ Database file `tasks.db` is created
3. ✓ API is accessible at `http://localhost:8000`
4. ✓ Swagger docs available at `http://localhost:8000/docs`
5. ✓ Health check returns `{"status": "healthy", ...}`
