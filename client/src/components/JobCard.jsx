const JobCard = ({ job }) => {
  return (
    <div className="bg-white bg-opacity-90 rounded-xl p-6 shadow-lg hover:shadow-2xl transform transition duration-300 hover:scale-105 text-gray-800">
      <h2 className="text-xl font-bold mb-1">{job.title}</h2>
      <p className="text-sm text-gray-600 mb-2">{job.company} • {job.location}</p>
      <p className="text-sm mb-3">{job.description}</p>
      <p className="font-semibold text-indigo-600">{job.salary}</p>
    </div>
  );
};

export default JobCard;


