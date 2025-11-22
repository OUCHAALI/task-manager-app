import React, { useState } from 'react';
import '../styles/TaskForm.css';

function TaskForm({ onAddTask }) {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (title.trim()) {
            onAddTask({
                title: title.trim(),
                description: description.trim(),
                completed: false
            });
            setTitle('');
            setDescription('');
        }
    };

    return (
        <form className="task-form" onSubmit={handleSubmit}>
            <div className="form-group">
                <input
                    type="text"
                    placeholder="Task title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    className="form-input"
                    required
                />
            </div>
            <div className="form-group">
                <textarea
                    placeholder="Task description (optional)"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    className="form-textarea"
                    rows="3"
                />
            </div>
            <button type="submit" className="btn btn-primary">
                Add Task
            </button>
        </form>
    );
}

export default TaskForm;
