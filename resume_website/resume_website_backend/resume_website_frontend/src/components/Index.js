import axios from 'axios';
import React, {useEffect, useState } from 'react';
import { Link } from 'react-router-dom'

function Index(){
    const [details, setDetails] = useState([])
    const [jobs, setJobs] = useState([])
    const [educations, setEducations] = useState([])
    const [projects, setProjects] = useState([])
    const [languages, setLanguages] = useState([])
    const [frameworks, setFrameworks] = useState([])
    const [skills, setSkills] = useState([])

    useEffect(()=>{
        axios.get('http://localhost:8000/details/').then(
            res => setDetails(
            res.data
            )
        ).catch(err => console.error(err));
        axios.get('http://localhost:8000/jobs/').then(
            res => setJobs(
                res.data
            )
        ).catch(err => console.error(err));
        axios.get('http://localhost:8000/educations/').then(
            res => setEducations(
                res.data
            )
        ).catch(err => console.error(err));
        axios.get('http://localhost:8000/projects/').then(
            res => setProjects(
                res.data
            )
        ).catch(err => console.error(err));
        axios.get('http://localhost:8000/languages/').then(
            res => setLanguages(
                res.data
            )
        ).catch(err => console.error(err));
        axios.get('http://localhost:8000/frameworks/').then(
            res => setFrameworks(
                res.data
            )
        ).catch(err => console.error(err));
        axios.get('http://localhost:8000/skills/').then(
            res => setSkills(
                res.data
            )
        ).catch(err => console.error(err));
    }, []);

    const skillList = (items) => items.map((item, index)=> (
        <span key={item.id}>
            {item.name}{index < items.length - 1 ? '; ' : ''}
        </span>
    ));

    return (
        <div>
            <section>
                <h3>Details</h3>
                <div>
                    {details.map(detail => 
                    <div key={detail.id}>
                        <p>{detail.first} {detail.last}</p>
                        <p>{detail.email} | {detail.phone} | {detail.city}, {detail.state}</p>
                        <p>{detail.social_link}</p>
                        <h3>Summary</h3>
                        <p>{detail.summary}</p>
                    </div>
                    )}                  
                </div>
            </section>
            <section>
                <h3>Jobs</h3>
                <div>
                    {jobs.map(job => 
                    <div key={job.id}>
                        <p><strong>{job.company}</strong> - <Link to={`/jobs/${job.id}`}>{job.job_title}</Link></p>
                        <p>{job.from_date} to {job.to_date} | {job.duraration_str}</p>
                    </div>                   
                )}
                </div>
            </section>
            <section>
                <h3>Education</h3>
                <div>
                    {educations.map(education => 
                        <div key={education.id}>
                            <p><strong>{education.school}</strong> - {education.degree}, <a href={education.course_structure}>{education.major}</a></p>
                            <p>{education.from_date} to {education.to_date}</p>
                        </div>
                    )}
                </div>
            </section>
            <section>
                <h3>Projects</h3>
                <div>
                    {projects.map(project => 
                        <div key={project.id}>
                            <p><strong>{project.org}</strong> - <Link to={`/projects/${project.id}`}>{project.project_name}</Link>, {project.role}</p>
                            <p><a href={project.github}>GitHub</a></p>
                        </div>
                    )}
                </div>
            </section>
            <section>
                <h3>Skills</h3>
                <div>
                    <p><strong>Languages:</strong> {skillList(languages)}</p>
                </div>
                <div>
                    <p><strong>Frameworks:</strong> {skillList(frameworks)}</p>
                </div>
                <div>
                    <p><strong>Competencies:</strong> {skillList(skills)}</p>
                </div>
            </section>
            <section>
                    <h3><Link to="/certificates">Certificates</Link></h3>
            </section>
        </div>
    );
}
export default Index;
// class App extends React.Component {
//     state = {
//         details: [],
//         jobs: [],
//         educations: [],
//         projects: [],
//         languages: [],
//         frameworks: [],
//         skills: [],
//         certificates: [],
//     }

//     componentDidMount() {
//         let data;
//         axios.get('http://localhost:8000/api/details/').then(res => {
//             data = res.data;
//             this.setState({
//                 details: data
//             });
//         }).catch(err => console)
//     }
    
// }