const http = require("http");

const page = `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Multi-Stage Build</title><style>
*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:#f2f4f7;color:#18212b;font-family:Arial,sans-serif}
main{width:min(640px,90vw);padding:40px;background:white;border:1px solid #cbd3dc;border-radius:8px}
span{color:#1769aa;font-weight:700}h1{margin:12px 0;font-size:38px;letter-spacing:0}p{margin:0;color:#586574;font-size:18px}
</style></head><body><main><span>DOCKER</span><h1>Hello World from Docker multi-stage build</h1><p>Builder and runtime stages are separate.</p></main></body></html>`;

http.createServer((request, response) => {
  response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  response.end(page);
}).listen(3000, "0.0.0.0", () => console.log("Multi-stage app on port 3000"));
