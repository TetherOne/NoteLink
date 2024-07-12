import React, { useEffect } from 'react';
import axios from 'axios';

const App = () => {
  useEffect(() => {
    axios.get("http://127.0.0.1:8005/api/v1/notes/public/").then(
      (response) => {
      console.log(response.data);
    });
  }, []);

  return (
    <div>
    </div>
  );
}

export default App;