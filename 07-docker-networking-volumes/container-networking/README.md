# Container Networking

## Layout

- Frontend: `frontend-net`
- Backend: `frontend-net` and `backend-net`
- Database: `backend-net` and `database-net`

## Run

```bash
docker compose up -d
docker compose ps
docker compose exec backend ping -c 2 frontend
docker compose exec backend ping -c 2 database
docker network ls
```

Stop the containers:

```bash
docker compose down
```
