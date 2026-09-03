import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return (
    <main>
      <span>REACT</span>
      <h1>Hello World</h1>
      <p>Built with Vite and served by Nginx in Docker.</p>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
