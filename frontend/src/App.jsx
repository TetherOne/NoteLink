import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ListNotes from "./components/notes/public/ListNotes.jsx";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/notes/public" element={<ListNotes />} />
      </Routes>
    </Router>
  );
}

export default App;
