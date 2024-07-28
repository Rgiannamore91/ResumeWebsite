// import logo from './logo.svg';
// import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Index from './components/Index.js'
import JobDetail from './components/JobDetail.js'
import ProjectDetail from './components/ProjectDetail.js'
import Certificates from './components/Certificates.js'


function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Index />}/>
          <Route path="/jobs/:id" element={<JobDetail/>}/>
          <Route path="/projects/:id" element={<ProjectDetail/>}/>
          <Route path="/certificates" element={<Certificates/>}/>
        </Routes>
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      </div>
    </Router>

  );
}

export default App;
