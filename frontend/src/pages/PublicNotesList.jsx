import React from 'react';

const PublicNotesList = ({ notes }) => {
  return (
    <div>
      <h1>Public Notes</h1>
      <ul>
        {notes.map(note => (
          <li key={note.id}>{note.content}</li>
        ))}
      </ul>
    </div>
  );
}

export default PublicNotesList;
