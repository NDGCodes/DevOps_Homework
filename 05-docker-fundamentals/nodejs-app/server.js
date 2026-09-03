const http = require("http");

const page = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Node.js Hello World</title>
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #f2f6f3; color: #17231b; font-family: Arial, sans-serif; }
    main { width: min(560px, 90vw); padding: 40px; background: white; border: 1px solid #cdd8d0; border-radius: 8px; }
    span { color: #176b3a; font-weight: 700; }
    h1 { margin: 12px 0; font-size: 42px; letter-spacing: 0; }
    p { margin: 0; color: #526158; font-size: 18px; }
  </style>
</head>
<body><main><span>NODE.JS</span><h1>Hello World</h1><p>Running in a Docker container.</p></main></body>
</html>`;

http.createServer((request, response) => {
  response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  response.end(page);
}).listen(3000, "0.0.0.0", () => console.log("Node.js app on port 3000"));
