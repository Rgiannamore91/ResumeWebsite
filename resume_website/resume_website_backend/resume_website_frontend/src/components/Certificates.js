import axios from 'axios';
import React, { useEffect, useState } from 'react';

function Certificates() {
    const [certificates, setCertificates] = useState([]);

    useEffect(()=>{
        axios.get('http://localhost:8000/certificates/')
        .then(res => setCertificates(res.data))
        .catch(err => console.error(err));
    }, []);
    return (
        <div>
            <h3>Certificates</h3>
            <table>
                <tr>
                    <th>School/Institution</th>
                    <th>Certificate</th>
                    <th>Date Obtained</th>
                </tr>
                {certificates.map(certificate => (
                    <tr>
                        <td>{certificate.school}</td>
                        <td><a href={certificate.link}>{certificate.name}</a></td>
                        <td>{certificate.date}</td>
                    </tr>
                ))}
            </table>
        </div>
    );
}
export default Certificates;