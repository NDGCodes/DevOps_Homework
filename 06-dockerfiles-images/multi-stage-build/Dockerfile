FROM node:22-alpine AS build

WORKDIR /build
COPY package.json server.js ./
RUN node --check server.js

FROM node:22-alpine AS runtime

WORKDIR /app
COPY --from=build /build/package.json /build/server.js ./

EXPOSE 3000
CMD ["npm", "start"]
