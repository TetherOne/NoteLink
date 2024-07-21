import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PublicNotesList from "../pages/PublicNotesList.jsx";
import API_ROUTES from "../config.js";

const PublicNote = () => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios.get(API_ROUTES.PUBLIC_NOTES)
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
