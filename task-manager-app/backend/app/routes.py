"""API routes for task management.

This module defines all CRUD endpoints for the Task resource:
- GET /tasks - List all tasks
- POST /tasks - Create a new task
- PUT /tasks/{id} - Update a task's status
- DELETE /tasks/{id} - Delete a task
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import logging

from app.models import Task as TaskModel, TaskCreate, TaskUpdate, TaskResponse
from app.db import get_db

logger = logging.getLogger(__name__)

router = APIRouter()


# ============================================================================
# GET Endpoints
# ============================================================================


@router.get("/tasks", response_model=List[TaskResponse], summary="List all tasks")
async def get_tasks(db: Session = Depends(get_db)):
    """Retrieve all tasks from the database.
    
    Args:
        db (Session): Database session (injected by FastAPI)
    
    Returns:
        List[TaskResponse]: List of all tasks
    
    Raises:
        HTTPException: 500 if database query fails
    """
    try:
        tasks = db.query(TaskModel).all()
        logger.info(f"Retrieved {len(tasks)} tasks")
        return tasks
    except Exception as e:
        logger.error(f"Error fetching tasks: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch tasks",
        )


@router.get(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    summary="Get a single task by ID",
)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific task by its ID.
    
    Args:
        task_id (int): The task ID to retrieve
        db (Session): Database session (injected by FastAPI)
    
    Returns:
        TaskResponse: The requested task
    
    Raises:
        HTTPException: 404 if task not found
        HTTPException: 500 if database query fails
    """
    try:
        task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not task:
            logger.warning(f"Task {task_id} not found")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        return task
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching task {task_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch task",
        )


# ============================================================================
# POST Endpoint
# ============================================================================


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
)
async def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    """Create a new task in the database.
    
    Args:
        task_data (TaskCreate): Task data from request body
        db (Session): Database session (injected by FastAPI)
    
    Returns:
        TaskResponse: The created task with its ID
    
    Raises:
        HTTPException: 400 if validation fails
        HTTPException: 500 if database operation fails
    """
    try:
        new_task = TaskModel(
            title=task_data.title,
            description=task_data.description,
            completed=task_data.completed,
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        logger.info(f"Task created with ID: {new_task.id}")
        return new_task
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating task: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create task",
        )


# ============================================================================
# PUT Endpoint
# ============================================================================


@router.put(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    summary="Update a task",
)
async def update_task(
    task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)
):
    """Update an existing task.
    
    Can update title, description, and/or completed status.
    Only provided fields will be updated (partial update support).
    
    Args:
        task_id (int): The task ID to update
        task_update (TaskUpdate): Fields to update
        db (Session): Database session (injected by FastAPI)
    
    Returns:
        TaskResponse: The updated task
    
    Raises:
        HTTPException: 404 if task not found
        HTTPException: 500 if database operation fails
    """
    try:
        db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not db_task:
            logger.warning(f"Task {task_id} not found for update")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        
        update_data = task_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)
        
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        logger.info(f"Task {task_id} updated")
        return db_task
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating task {task_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update task",
        )


# ============================================================================
# DELETE Endpoint
# ============================================================================


@router.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task from the database.
    
    Args:
        task_id (int): The task ID to delete
        db (Session): Database session (injected by FastAPI)
    
    Returns:
        None (204 No Content response)
    
    Raises:
        HTTPException: 404 if task not found
        HTTPException: 500 if database operation fails
    """
    try:
        db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not db_task:
            logger.warning(f"Task {task_id} not found for deletion")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with id {task_id} not found",
            )
        
        db.delete(db_task)
        db.commit()
        logger.info(f"Task {task_id} deleted")
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting task {task_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete task",
        )

