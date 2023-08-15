# tags-api

The API for the tags Discord bot.

This is backend for the actual bot. It's where the data is stored, the sites are generated, and so on.

## Self-Hosting

You can start of with filling in the variables in the [.env](./.env) file. All you need to do is fill in the following variable:

```sh
# The authentication key used to access the API. This will default to nothing, meaning there will be no authentication.
AUTH_KEY=...
```

After that is done, you can then run `docker-compose up` and watch it become alive!
You will of course need [docker-compose](https://docs.docker.com/compose/) as well as [docker](https://docs.docker.com) to do this.

## Tools Used

- [PostgreSQL](https://postgresql.org/) & [Prisma](https://prisma.io/) for database-related functions
- [tsoa](https://tsoa-community.github.io/docs/) & [Express](https://expressjs.com/) for routing in the API
- [Docker](https://docs.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) for creating containers and starting up the project easily
- [tsup](https://tsup.egoist.dev/) for code bundling
- [Pino](https://getpino.io/) & [pino-pretty](https://github.com/pinojs/pino-pretty/) for better logging