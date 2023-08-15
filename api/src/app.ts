import 'dotenv/config';

import pino from 'pino';
import express, { Request, Response, json, urlencoded } from 'express';
import swaggerUi from 'swagger-ui-express'

import { RegisterRoutes } from '../build/routes'
import { PrismaClient } from '@prisma/client';

export const app = express()
export const log = pino({
    transport: {
        target: 'pino-pretty'
    }
})
export const prisma = new PrismaClient()

app.listen(3000, () => {
    log.info("API listening at http://localhost:3000")
})

app.use("/docs", swaggerUi.serve, async (_req: Request, res: Response) => {
    return res.send(
        swaggerUi.generateHTML(await import("../build/swagger.json"))
    )
})

app.get("/", (_req: Request, res: Response) => {
    res.redirect("/docs")
})
app.use(urlencoded({ extended: true }))
app.use(json())

RegisterRoutes(app)

async function main() {
    for (const preview of await prisma.preview.findMany()) {
        app.use(`/${preview.id}`, (_req: Request, res: Response) => {
            res.send(preview.content)
        })
    }
    await prisma.$connect()
}
main().then(async () => {
    await prisma.$disconnect()
}).catch(async (reason) => {
    log.error(reason)
    await prisma.$disconnect()
    log.warn("Exiting...")
    process.exit(1)
})
