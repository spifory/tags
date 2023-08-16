"""The main file for the bot's commands."""

from logging import getLogger

from crescent import Context, Plugin, command
from hikari import RESTBot, TextInputStyle

plugin = Plugin[RESTBot, None]()
LOG = getLogger(__name__)

TAGS_PREVIEW = """
<meta name="title" content="name of the site" />
<meta name="description" content="the site!" />
"""


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


@plugin.load_hook
def load() -> None:
    """Control what the plugin does when being loaded."""
    LOG.info("Loaded %s", __name__)


@plugin.unload_hook
def unload() -> None:
    """Control what the plugin does when being unloaded."""
    LOG.warning("Unloaded %s", __name__)
