import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Notes from "../../../pages/notes/public/Notes.jsx";

const ListNotes = () => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8005/api/v1/notes/public/")
      .then(response => {
        setNotes(response.data);
      });
  }, []);

  return (
    <Notes notes={notes} />
  );
}

export default ListNotes;