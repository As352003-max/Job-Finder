const Home = () => {
  return (
    <div
      className="min-h-screen bg-cover bg-center relative text-white"
      style={{
        backgroundImage:
          "url('https://images.unsplash.com/photo-1508385082359-f38ae991e8f2?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNvcnBvcmF0ZXxlbnwwfHwwfHx8MA%3D%3D')",
      }}
    >
      {/* Dark semi-transparent overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-black via-black/70 to-black/90"></div>

      {/* Content */}
      <div className="relative z-10 max-w-5xl mx-auto px-6 py-20 text-center">
        <h1 className="text-5xl md:text-6xl font-extrabold mb-8 text-white drop-shadow-lg animate-bounce">
          Welcome to the Job Portal
        </h1>

        <p className="max-w-3xl mx-auto text-lg md:text-xl text-gray-200 mb-6 animate-fadeIn animation-delay-500 drop-shadow-md">
          Your gateway to exciting career opportunities — whether you’re a job seeker or a recruiter looking for top talent. We simplify the hiring process to save your time and energy.
        </p>

        <p className="max-w-3xl mx-auto text-md md:text-lg text-gray-300 mb-12 animate-fadeIn animation-delay-700 drop-shadow-md">
          Explore curated job listings, upload your resume with ease, and manage your applications effortlessly. Recruiters can post jobs, review resumes, and track applicants through a powerful admin dashboard.
        </p>

        <button
          className="bg-emerald-600 text-white px-8 py-3 rounded-full shadow-xl hover:bg-emerald-700 transition duration-300 transform hover:scale-105"
          onClick={() => alert('Let’s get started!')}
        >
          Get Started
        </button>

        {/* Features */}
        <section className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8 text-white">
          <Feature
            icon={
              <svg className="w-10 h-10 mx-auto mb-3" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m2 0a2 2 0 11-4 0 2 2 0 014 0zM5 12h.01M7 21h10a2 2 0 002-2v-7H5v7a2 2 0 002 2z" />
              </svg>
            }
            title="Smart Job Search"
            desc="Find your ideal job with filters for location, salary, experience, and more."
          />
          <Feature
            icon={
              <svg className="w-10 h-10 mx-auto mb-3" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" d="M8 16l-4-4m0 0l4-4m-4 4h16" />
              </svg>
            }
            title="Resume Upload"
            desc="Upload your resume and we’ll parse it to create your job-seeker profile instantly."
          />
          <Feature
            icon={
              <svg className="w-10 h-10 mx-auto mb-3" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" d="M3 7h18M3 12h18M3 17h18" />
              </svg>
            }
            title="Admin Dashboard"
            desc="Recruiters can easily post jobs, track applicants, and manage interviews."
          />
        </section>
      </div>

      {/* Animations */}
      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-fadeIn {
          animation: fadeIn 1s ease forwards;
        }
        .animation-delay-500 {
          animation-delay: 0.5s;
        }
        .animation-delay-700 {
          animation-delay: 0.7s;
        }
      `}</style>
    </div>
  );
};

const Feature = ({ icon, title, desc }) => (
  <div className="bg-white/10 backdrop-blur-md rounded-lg p-6 shadow-lg hover:bg-white/20 transition duration-300">
    {icon}
    <h3 className="text-xl font-semibold mb-2">{title}</h3>
    <p className="text-gray-200">{desc}</p>
  </div>
);

export default Home;
