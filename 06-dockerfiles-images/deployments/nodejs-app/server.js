const http = require("http");

http.createServer((request, response) => {
  response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  response.end("<h1>Hello World from Node.js deployment</h1>");
}).listen(3000, "0.0.0.0");
