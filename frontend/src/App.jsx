import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PublicNotes from "./components/public-notes/PublicNotes.jsx";
import PrivateNotes from "./components/private-notes/PrivateNotes.jsx";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/public-notes" element={<PublicNotes />} />
        <Route path="/private-notes/:private_id" element={<PrivateNotes />} />
      </Routes>
    </Router>
  );
}

export default App;
