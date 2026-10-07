# Multi-Stage Build

## Run

```bash
docker build -t homework-multi-stage .
docker run -d --name homework-multi-stage -p 8080:3000 homework-multi-stage
docker ps
```

Open http://localhost:8080.

## Stop

```bash
docker rm -f homework-multi-stage
```
