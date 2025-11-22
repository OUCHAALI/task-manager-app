"""FastAPI application entry point.

This module initializes the FastAPI application, sets up middleware,
initializes the database, and includes API routes.

Run with: uvicorn app.main:app --reload --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.db import init_db
from app.routes import router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app with metadata
app = FastAPI(
    title="Task Manager API",
    description="REST API for managing tasks with FastAPI and SQLite",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
)

# Initialize database tables on startup
init_db()
logger.info("Database initialized")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (modify for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("CORS middleware added")

# Include task routes with /api prefix
app.include_router(router, prefix="/api", tags=["tasks"])


# ============================================================================
# Root and Health Check Endpoints
# ============================================================================


@app.get("/", tags=["info"])
async def root():
    """Root endpoint - API information."""
    return {
        "message": "Task Manager API",
        "version": "1.0.0",
        "docs": "/docs",
        "api": "/api",
    }


@app.get("/health", tags=["info"])
async def health_check():
    """Health check endpoint.
    
    Returns:
        dict: Status information
    """
    return {"status": "healthy", "message": "Task Manager API is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
