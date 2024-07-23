import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import PublicNotesList from "../pages/PublicNotesList.jsx";
import NoteDetail from './NoteDetail';
import API_ROUTES from "../config.js";

const PublicNote = () => {
  const { publicId } = useParams();
  const [notes, setNotes] = useState([]);
  const [note, setNote] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (publicId) {
      axios.get(`${API_ROUTES.PUBLIC_NOTES}${publicId}`)
        .then(response => {
          setNote(response.data);
        })
        .catch(error => {
          setError("There was an error fetching the note!");
          console.error("There was an error fetching the note!", error);
        });
    } else {
      axios.get(API_ROUTES.PUBLIC_NOTES)
        .then(response => {
          setNotes(response.data);
        })
        .catch(error => {
          setError("There was an error fetching the notes!");
          console.error("There was an error fetching the notes!", error);
        });
    }
  }, [publicId]);

  if (error) return <p>{error}</p>;
  if (publicId && !note) return <p>Loading...</p>;
  if (!publicId && notes.length === 0) return <p>Loading...</p>;

  return publicId ? <NoteDetail note={note} /> : <PublicNotesList notes={notes} />;
}

export default PublicNote;
