import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PublicNote from "./components/PublicNote";
import API_ROUTES from "./config.js";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path={API_ROUTES.PUBLIC_NOTES_PATH} element={<PublicNote />} />
      </Routes>
    </Router>
  );
}

export default App;
