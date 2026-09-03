from http.server import BaseHTTPRequestHandler, HTTPServer


PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Python Hello World</title>
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #f7f5ef; color: #20252b; font-family: Arial, sans-serif; }
    main { width: min(560px, 90vw); padding: 40px; background: white; border: 1px solid #d7d1bf; border-radius: 8px; }
    span { color: #8b6508; font-weight: 700; }
    h1 { margin: 12px 0; font-size: 42px; letter-spacing: 0; }
    p { margin: 0; color: #5f625f; font-size: 18px; }
  </style>
</head>
<body><main><span>PYTHON</span><h1>Hello World</h1><p>Running in a Docker container.</p></main></body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGE.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
