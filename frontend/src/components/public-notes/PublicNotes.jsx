import React, { useEffect, useState } from 'react';
import axios from 'axios';
import NotesTable from "./NotesTable.jsx";

const PublicNotes = () => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8005/api/v1/notes/public/")
      .then(response => {
        setNotes(response.data);
      });
  }, []);

  return (
    <NotesTable notes={notes} />
  );
}

export default PublicNotes;
