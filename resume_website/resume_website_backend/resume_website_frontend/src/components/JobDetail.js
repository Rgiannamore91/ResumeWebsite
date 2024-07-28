import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function JobDetail() {
    const { id } = useParams();
    const [job, setJob] = useState(null);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/jobs/${id}/`)
        .then(res => setJob(res.data))
        .catch(err => console.error(err));
    }, [id]);

    if (!job) return <div>Loading...</div>;

    return (
        <div>
            <p><strong>{job.company}</strong> - {job.job_title}</p>
            <p>{job.from_date} to {job.to_date} | {job.duraration_str}</p>
            <p>{job.description}</p>
        </div>
    );
}
export default JobDetail;