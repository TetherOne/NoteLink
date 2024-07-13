import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PublicNotes from "./components/PublicNotes.jsx";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/public-notes" element={<PublicNotes />} />
      </Routes>
    </Router>
  );
}

export default App;
