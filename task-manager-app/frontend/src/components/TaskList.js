import React from 'react';
import TaskItem from './TaskItem';
import '../styles/TaskList.css';

function TaskList({ tasks, onDeleteTask, onCompleteTask }) {
    if (tasks.length === 0) {
        return <p className="no-tasks">No tasks yet. Create one to get started!</p>;
    }

    return (
        <ul className="task-list">
            {tasks.map(task => (
                <TaskItem
                    key={task.id}
                    task={task}
                    onDelete={onDeleteTask}
                    onComplete={onCompleteTask}
                />
            ))}
        </ul>
    );
}

export default TaskList;
