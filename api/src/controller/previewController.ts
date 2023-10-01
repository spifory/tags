import { Body, Controller, Delete, Get, Path, Post, Route, SuccessResponse } from 'tsoa';

import { Preview } from '../previews/previews';
import { PreviewCreationParams, PreviewService } from '../previews/previewService';
import { app, log } from '../app';
import { Request as ExRequest, Response as ExResponse } from 'express';

/**
 * The main control class for the `/previews` route.
 */
@Route('previews')
export class PreviewsController extends Controller {
    /**
     * Create a preview.
     * @param requestBody The body needed to make this request. Specifically the author ID and content.
     */
    @Post()
    @SuccessResponse('201', 'Created')
    public async createPreview(
        @Body() requestBody: PreviewCreationParams
    ): Promise<Preview> {
        this.setStatus(201)
        const created = await new PreviewService().create(requestBody)

        app.use(`/${created.id}`, (_req: ExRequest, res: ExResponse) => {
            return res.send(created.content)
        })
        return created as Preview
    }

    /**
     * Delete a preview.
     * @param id The ID of the preview.
     * @param authorID The author ID of the preview.
     */
    @Delete('{id}')
    @SuccessResponse(204, 'Deleted')
    public async deletePreview(
        @Path() id: string,
        @Body() authorID: string
    ): Promise<null> {
        this.setStatus(204)
        return await new PreviewService().delete(id, authorID)
    }

    /**
     * Gets all the previews for the specific user.
     * @param authorID The specific author to get previews from.
     */
    @Get('{authorID}')
    public async getAll(
        @Path() authorID: string
    ): Promise<Array<Preview>> {
        this.setStatus(200)
        return await new PreviewService().getAll(authorID)
    }
}
