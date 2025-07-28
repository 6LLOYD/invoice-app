import React from "react";
import Navbar from "./components/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";
import Tabs from "./components/Tabs";
import "./css/App.css";

const App: React.FC = () => {
  return (
    <div className="container mt-5">
      <Navbar />
      <h1>fzefezf</h1>
      <Tabs />
    </div>
  );
};

export default App;
