import { randomUUID } from 'crypto';
import { prisma } from '../app';
import { Preview } from './previews';

/**
 * The parameters required to creating a preview. This includes `authorID` and `content`.
 */
export interface PreviewCreationParams extends Pick<Preview, 'authorID' | 'content'> {}

export class PreviewService {
    /**
     * A function that creates a preview in the database.
     * @param data The creation data to add.
     * @returns {Promise<Preview>} The new preview.
     */
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

    /**
     * A function that deletes a preview in the database.
     * @param id The ID of the preview.
     * @param authorID The author of the preview's user ID.
     * @returns {null} null
     */
    public async delete(id: string, authorID: string): Promise<null> {
        return await prisma.preview.delete({
            where: {
                id: id,
                authorID: authorID
            },
        }) as null
    }

    /**
     *
     * @param authorID The ID of the user of which's previews to get.
     * @returns {Array<Preview>} The list of previews, if any. Returns an empty array if empty.
     */
    public async getAll(authorID: string): Promise<Array<Preview>> {
        return await prisma.preview.findMany({
            where: {
                authorID: authorID
            }
        }) as Array<Preview>
    }
}
