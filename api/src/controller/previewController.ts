import { Body, Controller, Delete, Get, Path, Post, Query, Response, Route, SuccessResponse } from 'tsoa';

import { Preview } from '../previews/previews';
import { PreviewCreationParams, PreviewService } from '../previews/previewService';
import { app, log } from '../app';
import { Request as ExRequest, Response as ExResponse } from 'express';

@Route('previews')
export class PreviewsController extends Controller {
    @Post()
    @SuccessResponse('201', 'Created')
    @Response('500', 'authorID is not a BigInt')
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

    @Delete('{authorID}')
    @SuccessResponse(204, 'Deleted')
    public async deletePreview(
        @Path() authorID: string,
        @Query() id: string,
    ): Promise<null> {
        this.setStatus(204)
        return await new PreviewService().delete(id, authorID)
    }

    @Get('{authorID}')
    public async getAll(
        @Path() authorID: string
    ): Promise<Array<Preview>> {
        this.setStatus(200)
        return await new PreviewService().getAll(authorID)
    }
}
