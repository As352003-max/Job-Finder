import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [form, setForm] = useState({ email: '', password: '' });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('/api/auth/login', form);
      localStorage.setItem('token', res.data.token);
      navigate('/jobs');
    } catch (err) {
      alert('Login failed. Please check credentials.');
    }
  };

  return (
    <div
      className="min-h-screen bg-cover bg-center flex items-center justify-center relative"
      style={{
        backgroundImage:
          "url('https://images.unsplash.com/photo-1508385082359-f38ae991e8f2?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNvcnBvcmF0ZXxlbnwwfHwwfHx8MA%3D%3D')",
      }}
    >
      <div className="absolute inset-0 "></div>

      <div className="relative z-10 max-w-md w-full mx-4 p-8 bg-white bg-opacity-90 rounded-2xl shadow-2xl animate-slideUp">
        <h2 className="text-3xl font-bold text-center text-indigo-700 mb-6 drop-shadow">
          🔐 Login to Your Account
        </h2>
        <form onSubmit={handleSubmit} className="space-y-5">
          <input
            type="email"
            placeholder="Email"
            className="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
            value={form.email}
            onChange={(e) => setForm({ ...form, email: e.target.value })}
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
            value={form.password}
            onChange={(e) => setForm({ ...form, password: e.target.value })}
            required
          />
          <button
            type="submit"
            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 rounded-lg shadow-md transition duration-300 transform hover:scale-105"
          >
            Log In
          </button>
        </form>
        <p className="mt-4 text-sm text-center text-gray-600">
          Don't have an account? <span className="text-indigo-500 hover:underline cursor-pointer">Sign up</span>
        </p>
      </div>

      {/* Animations */}
      <style>{`
        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(40px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-slideUp {
          animation: slideUp 1s ease-out forwards;
        }
      `}</style>
    </div>
  );
};

export default Login;

