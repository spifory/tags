/**
 * The preview model/object containing all the data in a preview.
 */
export interface Preview {
    /** The ID of the preview. This cannot be modified/added by the user. */
    id: string;
    /** The author of this preview. */
    authorID: string;
    /**
     * The preview's content. This contains the Meta/OG tags.
     */
    content: string;
}
