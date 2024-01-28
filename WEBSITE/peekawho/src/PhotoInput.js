import React, { useState, useEffect } from 'react';
import './PhotoInput.css';

const ImageUpload = () => {
  // State to keep track of selected images
  const [selectedFiles, setSelectedFiles] = useState([]);

  // State to keep track of uploaded images
  const [uploadedFiles, setUploadedFiles] = useState([]);

  // Handles file selection through file input
  const handleFileChange = (event) => {
    const files = event.target.files;
    handleFiles(files);
  };

  // Handles dropped files
  const handleFiles = (files) => {
    const newFiles = Array.from(files);
    // Set the selected images to the state
    setSelectedFiles((prevFiles) => [...prevFiles, ...newFiles]);
    // You can also perform additional actions here, such as uploading the images to a server.
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const files = event.dataTransfer.files;
    handleFiles(files);
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  // SENDING MESSAGE TO THE API/SERVER
  const handleUpload = () => {
    setUploadedFiles(selectedFiles);
  };

  const handleRemove = (index) => {
    const updatedFiles = [...selectedFiles];
    updatedFiles.splice(index, 1);
    setSelectedFiles(updatedFiles);
  };

  useEffect(() => {
    // Add event listeners for drag-and-drop
    const dropZone = document.getElementById('drop-zone');

    dropZone.addEventListener('drop', handleDrop);
    dropZone.addEventListener('dragover', handleDragOver);

    // Remove event listeners when the component unmounts
    return () => {
      dropZone.removeEventListener('drop', handleDrop);
      dropZone.removeEventListener('dragover', handleDragOver);
    };
  }, []); // Ensure this effect runs only once on component mount

  // Drop zone for selecting files
  return (
    <div className="file-drop-box">
      <input type="file" accept="image/*" onChange={handleFileChange} multiple />
      
      <div
        id="drop-zone"
        style={{
          border: '2px dashed #ccc',
          height: '250px',
          width: '350px',
          padding: '20px',
          marginTop: '20px',
          textAlign: 'center',
          display: 'inline-block',
          boxSizing: 'border-box',
        }}
      >
        <p>Drag and drop files here</p>
        {/* Display selected files */}
        {selectedFiles.length > 0 && (
          <div>
            <p>Selected Files:</p>
            {selectedFiles.map((file, index) => (
              <div key={index} style={{ margin: '5px' }}>
                {file.name}
                <button onClick={() => handleRemove(index)}>Remove</button>
              </div>
            ))}
            {/* Button to trigger the upload process */}
            <button onClick={handleUpload}>Upload Files</button>
          </div>
        )}
      </div>
      {/* Display uploaded files */}
      {uploadedFiles.length > 0 && (
        <div>
          <p>Uploaded Files:</p>
          {uploadedFiles.map((file, index) => (
            <div key={index} style={{ margin: '5px' }}>
              {file.name}
            </div>
          ))}
        </div>
      )}
      <button className = 'generate-btn' onClick={handleUpload}> Generate Board!</button>
    </div>
  );
};

export default ImageUpload;
