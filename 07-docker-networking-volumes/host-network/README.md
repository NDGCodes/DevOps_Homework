# Host Network

## Run

```bash
docker compose pull
docker compose up -d
docker compose ps
```

Open http://localhost:80.

Stop Apache:

```bash
docker compose down
```

Docker Desktop must have host networking enabled:

1. Sign in to Docker Desktop.
2. Open **Settings**.
3. Open **Resources**, then **Network**.
4. Turn on **Enable host networking**.
5. Select **Apply and restart**.
