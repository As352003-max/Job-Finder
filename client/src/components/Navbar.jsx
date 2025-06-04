import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-black text-white px-6 py-4 flex justify-between">
      <h1 className="text-xl font-bold">Job Portal</h1>
      <div className="space-x-4">
        <Link to="/">Home</Link>
        <Link to="/jobs">Jobs</Link>
        <Link to="/login">Login</Link>
        <Link to="/register">Register</Link>
        <Link to="/upload">Upload</Link>
      </div>
    </nav>
  );
};

export default Navbar;
