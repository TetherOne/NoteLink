import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PublicNotesList from "../pages/PublicNotesList.jsx";

const PublicNote = () => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8005/api/v1/notes/public/")
      .then(response => {
        setNotes(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the notes!", error);
      });
  }, []);

  return <PublicNotesList notes={notes} />;
}

export default PublicNote;
