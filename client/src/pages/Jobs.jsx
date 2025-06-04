import { useEffect, useState } from 'react';
import axios from 'axios';
import JobCard from '../components/JobCard';

const Jobs = () => {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get('/api/jobs')
      .then(res => {
        if (Array.isArray(res.data)) {
          setJobs(res.data);
        } else if (res.data.jobs && Array.isArray(res.data.jobs)) {
          setJobs(res.data.jobs);
        } else {
          setJobs(fallbackJobs);
        }
      })
      .catch(() => setJobs(fallbackJobs));
  }, []);

  return (
    <div
      className="min-h-screen bg-cover bg-center relative text-white"
      style={{
        backgroundImage: "url('https://images.unsplash.com/photo-1508385082359-f38ae991e8f2?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNvcnBvcmF0ZXxlbnwwfHwwfHx8MA%3D%3D')"
      }}
    >
      <div className="absolute inset-0 "></div>

      <div className="relative z-10 px-6 py-16 max-w-7xl mx-auto">
        <h1 className="text-4xl md:text-5xl font-extrabold mb-10 text-center text-white drop-shadow-lg">
          🔍 Explore Career Opportunities
        </h1>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {jobs.length > 0 ? (
            jobs.map(job => <JobCard key={job.id} job={job} />)
          ) : (
            <p className="text-center col-span-full text-lg text-gray-300">No jobs available right now.</p>
          )}
        </div>
      </div>
    </div>
  );
};

const fallbackJobs = [
  {
    id: 1,
    title: 'Frontend Developer',
    company: 'SoftTech Solutions',
    location: 'Remote',
    salary: '₹8–12 LPA',
    description: 'Build UI components with React and Tailwind CSS.'
  },
  {
    id: 2,
    title: 'Backend Engineer',
    company: 'CodeCraft Ltd',
    location: 'Bangalore, India',
    salary: '₹10–15 LPA',
    description: 'Develop REST APIs with Node.js and Express.'
  },
  {
    id: 3,
    title: 'UI/UX Designer',
    company: 'PixelPerfection',
    location: 'Mumbai, India',
    salary: '₹6–10 LPA',
    description: 'Design modern web and mobile interfaces.'
  },
  {
    id: 4,
    title: 'DevOps Engineer',
    company: 'CloudBridge',
    location: 'Remote',
    salary: '₹14–20 LPA',
    description: 'Automate infrastructure and CI/CD pipelines with AWS.'
  },
  {
    id: 5,
    title: 'Data Analyst',
    company: 'Insight Lab',
    location: 'Hyderabad, India',
    salary: '₹9–13 LPA',
    description: 'Analyze data trends using SQL, Power BI, and Python.'
  },
  {
    id: 6,
    title: 'Mobile App Developer',
    company: 'Appify Tech',
    location: 'Pune, India',
    salary: '₹10–16 LPA',
    description: 'Develop apps using Flutter or React Native.'
  }
];

export default Jobs;


