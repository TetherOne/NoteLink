import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PublicNotes = () => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8005/api/v1/notes/public/").then(
      (response) => {
        setNotes(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Public Notes</h1>
      <ul>
        {notes.map((note, index) => (
          <li key={index}>{note.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default PublicNotes;
