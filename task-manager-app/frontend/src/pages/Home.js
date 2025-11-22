import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Home.css';

function Home() {
    return (
        <div className="container home-container">
            <h2>Welcome to Task Manager</h2>
            <p>Manage your tasks efficiently and stay organized.</p>
            <Link to="/tasks" className="btn btn-primary">
                View Tasks
            </Link>
        </div>
    );
}

export default Home;
