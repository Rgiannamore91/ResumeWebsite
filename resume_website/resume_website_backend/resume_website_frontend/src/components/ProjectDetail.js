import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function ProjectDetail(){
    const { id } = useParams();
    const [project, setProject] = useState(null);
    useEffect(() => {
        axios.get(`http://localhost:8000/api/projects/${id}/`)
        .then(res => setProject(res.data))
        .catch(err => console.error(err));
    }, [id]);
    if (!project) return <div>Loading...</div>
    return (
        <div>
            <p><strong>{project.org}</strong> - {project.project_name}, {project.role}</p>
            <p><a href={project.github}>GitHub</a></p>
            <p>{project.description}</p>
        </div>
    );
}
export default ProjectDetail;