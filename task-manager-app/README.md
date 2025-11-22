# Task Manager App

A full-stack task management application built with React frontend, FastAPI backend, and PostgreSQL database, containerized with Docker and orchestrated with Docker Compose.

## 📋 Project Structure

```
task-manager-app/
├── frontend/                # React frontend application
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   ├── pages/           # Page components
│   │   ├── styles/          # CSS files
│   │   ├── App.js           # Main app component
│   │   └── index.js         # React entry point
│   ├── package.json         # Frontend dependencies
│   └── Dockerfile           # Frontend container image
│
├── backend/                 # FastAPI backend application
│   ├── app/
│   │   ├── main.py          # FastAPI entry point
│   │   ├── models.py        # Pydantic models
│   │   ├── routes.py        # API endpoints
│   │   └── db.py            # Database connection
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile           # Backend container image
│
├── docker-compose.yml       # Docker Compose orchestration
├── Jenkinsfile              # CI/CD pipeline definition
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git

### Installation and Running

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd task-manager-app
   ```

2. **Start the application with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

4. **Stop the application**
   ```bash
   docker-compose down
   ```

## 🏗️ Architecture

### Frontend (React)
- **Framework**: React 18
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Styling**: CSS modules

### Backend (FastAPI)
- **Framework**: FastAPI
- **Database ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Validation**: Pydantic

### Infrastructure
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **CI/CD**: Jenkins

## 📡 API Endpoints

### Tasks

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/{task_id}` - Get a specific task
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/{task_id}` - Update a task
- `DELETE /api/tasks/{task_id}` - Delete a task

### Health Check

- `GET /health` - Health check endpoint

## 📦 Environment Variables

### Backend
- `DATABASE_URL` - PostgreSQL connection string
  - Default: `postgresql://postgres:postgres@db:5432/taskdb`
- `PYTHONUNBUFFERED` - Set to 1 to disable Python buffering

### Frontend
- `REACT_APP_API_URL` - Backend API URL
  - Default: `http://localhost:8000`

## 🛠️ Development

### Local Development without Docker

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

### Docker Build

**Build all services:**
```bash
docker-compose build
```

**Build specific service:**
```bash
docker-compose build frontend
docker-compose build backend
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🚀 CI/CD Pipeline

The project includes a Jenkinsfile that defines a complete CI/CD pipeline with the following stages:

1. **Checkout** - Clone the repository
2. **Build Backend** - Build backend Docker image
3. **Build Frontend** - Build frontend Docker image
4. **Test Backend** - Run backend tests
5. **Test Frontend** - Run frontend tests
6. **Security Scan** - Scan images for vulnerabilities
7. **Push Images** - Push to Docker registry
8. **Deploy to Dev** - Deploy to dev environment (on develop branch)
9. **Deploy to Production** - Deploy to production (on main branch)
10. **Health Check** - Verify service health

## 📝 Database Schema

### Tasks Table

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

## 🔒 Security Features

- CORS middleware configured
- Trusted host middleware for request validation
- Database connection pooling with health checks
- Input validation with Pydantic models
- Error handling and logging
- Health check endpoint for monitoring

## 📊 Logging

Both frontend and backend include logging for debugging and monitoring:

- **Backend**: Python logging configuration in `app/main.py`
- **Frontend**: Browser console and error boundaries

## 🤝 Contributing

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Commit your changes (`git commit -m 'Add amazing feature'`)
3. Push to the branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Database connection errors
- Ensure PostgreSQL container is running: `docker-compose logs db`
- Check DATABASE_URL environment variable

### Frontend can't connect to backend
- Verify backend is running: `docker-compose logs backend`
- Check REACT_APP_API_URL environment variable
- Ensure CORS is enabled in backend

### Docker issues
- Clear Docker cache: `docker system prune`
- Rebuild images: `docker-compose build --no-cache`

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 👨‍💻 Author

Task Manager App - DevOps Project

## ⭐ Show your support

Give a ⭐ if this project helped you!
