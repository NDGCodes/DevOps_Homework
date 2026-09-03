# Bind Mount

## Run

```bash
chmod +x reset-page.sh update-page.sh
./reset-page.sh
docker compose up -d
```

Open http://localhost:8301. It shows `Hello students`.

Change the file:

```bash
./update-page.sh
```

Refresh the same page. It changes without a restart.

Stop Nginx:

```bash
docker compose down
```
