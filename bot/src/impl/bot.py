"""The file containing all implementation for the `Bot` class used everywhere."""
from os import environ
from typing import Any

from aiohttp import ClientSession
from hikari import ModalInteraction, RESTBot
from hikari.api import InteractionMessageBuilder

__all__ = ("Bot",)


class Bot(RESTBot):
    """The main bot subclass of `RESTBot`.

    This is used primarily to override functions in the original class.
    """

    def __init__(self) -> None:
        """Initiate the `Bot` class."""
        super().__init__(token=environ["BOT_TOKEN"], public_key=environ["PUBLIC_KEY"])
        self.http_session: ClientSession | None = None

    async def start(self, *args: Any, **kwargs: Any) -> None:
        """Control the starting process of the bot."""
        self.http_session = ClientSession(base_url=environ["API_URL"])

        return await super().start(*args, **kwargs)

    async def handle_preview_modal(
        self,
        inter: ModalInteraction,
    ) -> InteractionMessageBuilder | None:
        """Control all preview modals."""
        if inter.custom_id == f"preview_modal:{inter.user.id}":
            data: dict[str, int | str] = {}
            data["authorID"] = inter.user.id
            data["content"] = inter.components[0].components[0].value

            async with self.http_session.post("/previews", data=data) as res: # type: ignore[reportOptionalMemberAccess]
                response = inter.build_response()
                json = await res.json()

                if res.ok:
                    url = f"{environ['API_URL']}/{json['id']}"
                    response.set_content(f"Here is your preview: {url}")
                else:
                    response.set_content(f"Error uploading preview content:\n{await res.text()}")
                return response
        return None
