import React from 'react';
import { Link } from 'react-router-dom';
import API_ROUTES from "../config.js";

const PublicNotePage = ({ notes }) => {
  return (
    <div>
      <h1>Недавние записи</h1>
      <ul>
        {notes.map(note => (
          <li key={note.id} style={{ marginBottom: '20px', padding: '10px', border: '1px solid #ddd' }}>
            <h2>
              <Link to={`${API_ROUTES.PUBLIC_NOTES_PATH}/${note.public_id}`}>
                {note.title}
              </Link>
            </h2>
            <p>{note.text}</p>
            <p><strong>Дата публикации:</strong> {new Date(note.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PublicNotePage;
