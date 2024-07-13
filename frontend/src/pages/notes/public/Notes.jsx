import React from 'react';
import { Link } from 'react-router-dom';

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const year = date.getFullYear();
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');
  return `${hours}:${minutes}:${seconds} ${day}.${month}.${year}`;
};

const Notes = ({ notes }) => {
  return (
    <div className="card d-flex" style={{ width: '48rem' }}>
      <div className="card-body">
        <table className="table table-hover table-forum text-center">
          <thead>
          <tr>
            <th></th>
            <th className="text-left">Topic</th>
          </tr>
          </thead>
          <tbody>
          {notes.map((note, index) => (
            <tr key={index}>
              <td scope="row" className="text-nowrap"></td>
              <td className="text-start">
                <Link to={`/notes/public/${note.id}`} className="font-weight-bold blue-text">
                  {note.title}
                </Link>
                <div className="my-2">
                  <a href="#" className="blue-text">
                    <strong>{note.text}</strong>
                  </a>
                  <span>{formatDate(note.created_at)}</span>
                  <div></div>
                </div>
              </td>
              <td>
                <a href="#" className="text-dark">
                  <span>{note.comments_count}</span>
                  <i className="fas fa-comments ml-1"></i>
                </a>
              </td>
            </tr>
          ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Notes;
