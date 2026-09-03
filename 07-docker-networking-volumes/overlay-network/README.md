# Overlay Network

An overlay network joins containers on many Docker hosts.

It is used with Docker Swarm. Docker adds a virtual network over the real
host network. Services can use names to find each other.

## Main Commands

```bash
docker swarm init
docker network create --driver overlay app-overlay
docker network ls
docker network inspect app-overlay
```

Use cases:

- Apps on many servers
- Swarm services
- Private service traffic
- Easy service discovery

One computer can show the commands, but a true multi-host test needs two or
more Docker hosts.
