import React from 'react';
import '../styles/TaskItem.css';

function TaskItem({ task, onDelete, onComplete }) {
    return (
        <li className={`task-item ${task.completed ? 'completed' : ''}`}>
            <div className="task-content">
                <input
                    type="checkbox"
                    checked={task.completed}
                    onChange={() => onComplete(task.id)}
                    className="task-checkbox"
                />
                <div className="task-info">
                    <h3 className="task-title">{task.title}</h3>
                    {task.description && <p className="task-description">{task.description}</p>}
                </div>
            </div>
            <button
                onClick={() => onDelete(task.id)}
                className="btn btn-delete"
            >
                Delete
            </button>
        </li>
    );
}

export default TaskItem;
