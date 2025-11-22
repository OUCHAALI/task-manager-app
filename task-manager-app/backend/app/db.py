"""Database configuration module.

This module sets up SQLAlchemy with SQLite database,
defines the database engine, session factory, and Base class
for all SQLAlchemy models.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

logger = logging.getLogger(__name__)

# SQLite database configuration
# Using SQLite with file-based storage: tasks.db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")

# Create SQLAlchemy engine
# connect_args={"check_same_thread": False} is needed for SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    echo=False,  # Set to True for SQL query logging
)

logger.info(f"Database engine created: {DATABASE_URL}")

# Create session factory
# SessionLocal is used to create new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for all SQLAlchemy models
Base = declarative_base()


def init_db():
    """Initialize all database tables.
    
    Creates all tables defined in SQLAlchemy models
    by calling Base.metadata.create_all().
    This should be called once at application startup.
    """
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables initialized")


def get_db():
    """Dependency injection function for database sessions.
    
    Yields a database session for each request and ensures
    the session is closed after the request is completed.
    
    Yields:
        Session: SQLAlchemy session instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
