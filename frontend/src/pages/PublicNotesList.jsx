import React from 'react';

const PublicNotePage = ({ notes }) => {
  return (
    <div>
      <h1>Недавние записи</h1>
      <ul>
        {notes.map(note => (
          <li key={note.id} style={{ marginBottom: '20px', padding: '10px', border: '1px solid #ddd' }}>
            <h2>{note.title}</h2>
            <p>{note.text}</p>
            <p><strong>Дата публикации:</strong> {new Date(note.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PublicNotePage;
