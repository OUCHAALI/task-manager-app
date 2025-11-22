import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TaskList from '../components/TaskList';
import TaskForm from '../components/TaskForm';
import '../styles/Tasks.css';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function Tasks() {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        try {
            setLoading(true);
            const response = await axios.get(`${API_BASE_URL}/api/tasks`);
            setTasks(response.data);
            setError(null);
        } catch (err) {
            setError('Failed to fetch tasks');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleAddTask = async (taskData) => {
        try {
            const response = await axios.post(`${API_BASE_URL}/api/tasks`, taskData);
            setTasks([...tasks, response.data]);
        } catch (err) {
            setError('Failed to add task');
            console.error(err);
        }
    };

    const handleDeleteTask = async (taskId) => {
        try {
            await axios.delete(`${API_BASE_URL}/api/tasks/${taskId}`);
            setTasks(tasks.filter(task => task.id !== taskId));
        } catch (err) {
            setError('Failed to delete task');
            console.error(err);
        }
    };

    const handleCompleteTask = async (taskId) => {
        try {
            const response = await axios.put(`${API_BASE_URL}/api/tasks/${taskId}`, {
                completed: true
            });
            setTasks(tasks.map(task => task.id === taskId ? response.data : task));
        } catch (err) {
            setError('Failed to update task');
            console.error(err);
        }
    };

    return (
        <div className="container tasks-container">
            <h2>My Tasks</h2>
            {error && <div className="error-message">{error}</div>}
            <TaskForm onAddTask={handleAddTask} />
            {loading ? (
                <p>Loading tasks...</p>
            ) : (
                <TaskList
                    tasks={tasks}
                    onDeleteTask={handleDeleteTask}
                    onCompleteTask={handleCompleteTask}
                />
            )}
        </div>
    );
}

export default Tasks;
