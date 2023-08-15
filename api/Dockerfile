FROM node:18-bullseye-slim

WORKDIR /api

COPY package.json yarn.lock ./

RUN --mount=type=cache,target=/root/.cache/yarn,sharing=locked \
    yarn install --production --non-interactive

COPY . .

CMD [ "sh", "./entrypoint.sh" ]