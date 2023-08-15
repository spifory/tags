import { randomUUID } from 'crypto';
import { prisma } from '../app';
import { Preview } from './previews';

export type PreviewCreationParams = Pick<Preview, 'authorID' | 'content'>

export class PreviewService {
    public async create(data: PreviewCreationParams): Promise<Preview> {
        return await prisma.preview.create({
            data: {
                id: randomUUID(),
                // it will error when a BigInt is not a BigInt and then turn it into a string again
                // just so that it can go in to the database correctly
                // I have no idea why I'm doing it like this
                authorID: String(BigInt(data.authorID)),
                content: data.content
            }
        }) as Preview
    }

    public async delete(id: string, authorID: string): Promise<null> {
        return await prisma.preview.delete({
            where: {
                id: id,
                authorID: authorID
            },
        }) as null
    }

    public async getAll(authorID: string): Promise<Array<Preview>> {
        return await prisma.preview.findMany({
            where: {
                authorID: authorID
            }
        }) as Array<Preview>
    }
}
