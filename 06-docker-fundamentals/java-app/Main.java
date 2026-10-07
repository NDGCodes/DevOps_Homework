import com.sun.net.httpserver.HttpServer;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) throws Exception {
        String page = """
            <!doctype html><html lang="en"><head><meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Java Hello World</title><style>
            *{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:#f7f2f1;color:#291d1b;font-family:Arial,sans-serif}
            main{width:min(560px,90vw);padding:40px;background:white;border:1px solid #dbcac6;border-radius:8px}
            span{color:#a13d2d;font-weight:700}h1{margin:12px 0;font-size:42px;letter-spacing:0}p{margin:0;color:#675956;font-size:18px}
            </style></head><body><main><span>JAVA</span><h1>Hello World</h1><p>Running in a Docker container.</p></main></body></html>
            """;
        byte[] body = page.getBytes(StandardCharsets.UTF_8);
        HttpServer server = HttpServer.create(new InetSocketAddress("0.0.0.0", 8080), 0);
        server.createContext("/", exchange -> {
            exchange.getResponseHeaders().add("Content-Type", "text/html; charset=utf-8");
            exchange.sendResponseHeaders(200, body.length);
            exchange.getResponseBody().write(body);
            exchange.close();
        });
        server.start();
        System.out.println("Java app on port 8080");
    }
}
