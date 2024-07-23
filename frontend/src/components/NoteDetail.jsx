import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import API_ROUTES from '../config.js';

const NoteDetail = () => {
  const { publicId } = useParams();
  const [note, setNote] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get(`${API_ROUTES.PUBLIC_NOTES}${publicId}`)
      .then(response => {
        setNote(response.data);
      })
      .catch(error => {
        setError("There was an error fetching the note!");
        console.error("There was an error fetching the note!", error);
      });
  }, [publicId]);

  if (error) return <p>{error}</p>;
  if (!note) return <p>Loading...</p>;

  return (
    <div>
      <h1>{note.title}</h1>
      <p>{note.text}</p>
      <p><strong>Дата публикации:</strong> {new Date(note.created_at).toLocaleString()}</p>
    </div>
  );
};

export default NoteDetail;
