"""The main file for the bot's commands."""

from logging import getLogger

from crescent import Context, Group, Plugin, command, option
from hikari import Message, TextInputStyle

from src.impl.bot import Bot

plugin = Plugin[Bot, None]()
LOG = getLogger(__name__)
NO_CONTENT_STATUS = 204

TAGS_PREVIEW = """
<meta name="title" content="name of the site">
<meta name="description" content="the site!">
"""

previews = Group("previews")

@plugin.include
@command(description="Preview what your Meta/OpenGraph tags will look like on Discord.")
async def preview(ctx: Context) -> None:
    """Preview what your Meta/OpenGraph tags will look like on Discord."""
    modal = plugin.app.rest.build_modal_action_row()

    modal.add_text_input(
        f"preview_modal_content:{ctx.user.id}",  # custom_id, positional for some reason
        "Tags",  # label
        style=TextInputStyle.PARAGRAPH,
        placeholder=TAGS_PREVIEW,
    )

    return await ctx.interaction.create_modal_response(
        title="Tags Preview",
        custom_id=f"preview_modal:{ctx.user.id}",
        component=modal,
    )

@plugin.include
@previews.child
@command(name="delete", description="Delete a preview.")
class PreviewsDelete:
    """Delete a preview."""

    preview_id = option(
        option_type=str,
    )

    async def callback(self, ctx: Context) -> Message | None:
        """Control callback for `/previews delete`."""
        req = await self.delete_preview(preview_id=self.preview_id, user_id=ctx.user.id)

        if not req:
            return await ctx.respond(
                f"`{self.preview_id}` is an invalid ID. Make use of the autocomplete.",
                ephemeral=True,
            )
        return await ctx.respond(f"`{self.preview_id}` deleted", ephemeral=True)

    async def delete_preview(self, *, preview_id: str, user_id: int) -> bool:
        """Delete and check if preview is deleted.

        This is its own function to avoid lots of indentation.
        """
        async with plugin.app.http_session.delete(  # type: ignore[reportOptionalMemberAccess]
            url=f"/previews/{user_id}?id={preview_id}",
        ) as res:
            # DELETE /previews returns 204, so this function won't return any response.
            return res.status == NO_CONTENT_STATUS


@plugin.load_hook
def load() -> None:
    """Control what the plugin does when being loaded."""
    LOG.info("Loaded %s", __name__)


@plugin.unload_hook
def unload() -> None:
    """Control what the plugin does when being unloaded."""
    LOG.warning("Unloaded %s", __name__)
