import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import NotesTable from "./NotesTable.jsx";

const PrivateNotes = () => {
  const [notes, setNotes] = useState([]);
  const { private_id } = useParams();

  useEffect(() => {
    const token = localStorage.getItem('access_token');

    if (token) {
      axios.get(`http://127.0.0.1:8005/api/v1/notes/private/${private_id}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
        .then(response => {
          setNotes(response.data);
        })
        .catch(error => {
          console.error('Error fetching private notes:', error);
        });
    } else {
      console.error('No access token found');
    }
  }, [private_id]);

  return (
    <NotesTable notes={notes} />
  );
}

export default PrivateNotes;
