import React from 'react';

const NotesTable = ({ notes }) => {
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
              <td scope="row" className="text-nowrap">
                <a href="#" type="button" data-mdb-ripple-init className="btn btn-outline-dark-green btn-sm p-1 m-0 waves-effect">
                  <span className="value">0</span>
                  <i className="fas fa-thumbs-up ml-1"></i>
                </a>
                <a href="#" type="button" data-mdb-ripple-init className="btn btn-outline-danger btn-sm p-1 m-0 waves-effect">
                  <span className="value">0</span>
                  <i className="fas fa-thumbs-down ml-1"></i>
                </a>
              </td>
              <td className="text-start">
                <a href="#" className="font-weight-bold blue-text">
                  {note.title}
                </a>
                <div className="my-2">
                  <a href="#" className="blue-text">
                    <strong>{note.author}</strong>
                  </a>
                  <span className="badge bg-secondary mx-1">staff</span>
                  <span className="badge bg-primary mx-1">pro</span>
                  <span className="badge bg-warning mx-1">premium</span>
                  <span>{note.created_at}</span>
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

        <div className="d-flex justify-content-center">
          <nav className="my-2 pt-2">
            <ul className="pagination pagination-circle pg-info mb-0">
              <li className="page-item clearfix d-none d-md-block">
                <a href="#" className="page-link waves-effect">First</a>
              </li>
              <li className="page-item">
                <a href="#" className="page-link waves-effect" aria-label="Previous">
                  <span aria-hidden="true">«</span>
                  <span className="sr-only">Previous</span>
                </a>
              </li>
              <li className="page-item">
                <a href="#" className="page-link waves-effect">11</a>
              </li>
              <li className="page-item">
                <a href="#" className="page-link waves-effect">12</a>
              </li>
              <li className="page-item active">
                <a href="#" className="page-link waves-effect">13</a>
              </li>
              <li className="page-item">
                <a href="#" className="page-link waves-effect">14</a>
              </li>
              <li className="page-item">
                <a href="#" className="page-link waves-effect">15</a>
              </li>
              <li className="page-item">
                <a href="#" className="page-link waves-effect" aria-label="Next">
                  <span aria-hidden="true">»</span>
                  <span className="sr-only">Next</span>
                </a>
              </li>
              <li className="page-item clearfix d-none d-md-block">
                <a href="#" className="page-link waves-effect">Last</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  );
}

export default NotesTable;