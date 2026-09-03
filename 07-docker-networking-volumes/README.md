# Docker Networking and Volumes

Name: Nishant Dasgupta  
Roll number: **24bcs10451**

## Container Networking

The frontend, backend, and database use three Docker networks. The backend can
connect to both the frontend and database.

![Container networking](container-networking/container-networking_24bcs10451.png)

## Host Network

Apache uses the host network and is available on port `80`.

![Host-network container](host-network/host-network-started_24bcs10451.png)

![Apache on port 80](host-network/host-network-page_24bcs10451.png)

## Bind Mount

The page changes after editing the mounted `index.html` file. The container is
not restarted.

![Bind mount before update](bind-mount/bind-mount-before_24bcs10451.png)

![Bind mount after update](bind-mount/bind-mount-after_24bcs10451.png)

## Overlay Network

The overlay-network explanation and commands are in
[overlay-network/README.md](overlay-network/README.md).
