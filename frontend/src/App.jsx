import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PublicNote from "./components/PublicNote";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/notes/public" element={<PublicNote />} />
      </Routes>
    </Router>
  );
}

export default App;
