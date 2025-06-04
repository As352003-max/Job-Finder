import React, { useState } from 'react';
import axios from 'axios';

export default function Upload() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [preview, setPreview] = useState(null);

  const handleFileChange = (f) => {
    setFile(f);
    if (f && f.type.startsWith('image/')) {
      const reader = new FileReader();
      reader.onload = () => setPreview(reader.result);
      reader.readAsDataURL(f);
    } else {
      setPreview(null);
    }
  };

  const uploadResume = async () => {
    if (!file) {
      alert('Please select a file first.');
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append('resume', file);
    try {
      const res = await axios.post('http://localhost:5000/api/resume/upload', formData);
      setText(res.data.parsed_text);
    } catch (error) {
      alert('Upload failed. Please try again.');
    }
    setLoading(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile) handleFileChange(droppedFile);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  return (
    <div
      className="min-h-screen bg-cover bg-center flex items-center justify-center relative p-4"
      style={{
        backgroundImage:
          "url('https://images.unsplash.com/photo-1508385082359-f38ae991e8f2?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNvcm9wcmF0ZXxlbnwwfHwwfHx8MA%3D%3D')",
      }}
    >
      {/* Overlay */}
      <div className="absolute inset-0 bg-black opacity-60 z-0"></div>

      {/* Upload Box */}
      <div
        className="relative z-10 bg-white bg-opacity-90 rounded-3xl shadow-2xl p-8 w-full max-w-md border-2 border-dashed border-indigo-300"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
      >
        <h2 className="text-center text-2xl font-bold text-indigo-600 mb-4 border-b pb-2 border-indigo-200">
          --- UPLOAD FILES ---
        </h2>

        <div
          className="w-full h-40 bg-indigo-50 border-2 border-dashed border-indigo-300 rounded-xl flex flex-col items-center justify-center cursor-pointer transition hover:bg-indigo-100"
          onClick={() => document.getElementById('fileInput').click()}
        >
          <img
            src="https://img.icons8.com/color/48/000000/upload-to-cloud.png"
            alt="Upload Icon"
            className="mb-2"
          />
          <p className="font-semibold text-gray-700">Drag & Drop</p>
          <p className="text-sm text-gray-500">Or Browse to upload</p>
          <p className="text-xs mt-2 text-indigo-400">
            Only JPEG, PNG, GIF, PDF files, Max 15MB
          </p>
        </div>

        <input
          type="file"
          id="fileInput"
          className="hidden"
          accept=".pdf,.doc,.docx,.png,.jpg,.jpeg,.gif"
          onChange={(e) => handleFileChange(e.target.files[0])}
          disabled={loading}
        />

        {preview && (
          <div className="mt-4 flex justify-center">
            <img src={preview} alt="preview" className="w-16 h-16 rounded-full shadow" />
          </div>
        )}

        <button
          onClick={uploadResume}
          disabled={loading}
          className="mt-6 w-full bg-indigo-600 hover:bg-indigo-700 text-white py-3 rounded-xl font-semibold flex items-center justify-center gap-2 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? (
            <>
              <svg
                className="animate-spin h-5 w-5 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                ></circle>
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
                ></path>
              </svg>
              Uploading...
            </>
          ) : (
            'SAVE FILES'
          )}
        </button>

        {text && (
          <pre className="mt-6 p-4 bg-gray-100 rounded-lg max-h-64 overflow-auto text-gray-800 whitespace-pre-wrap">
            {text}
          </pre>
        )}
      </div>
    </div>
  );
}

