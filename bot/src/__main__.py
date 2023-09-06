from __future__ import annotations

from os import environ
from typing import TYPE_CHECKING

from aiohttp import ClientSession
from crescent import Client
from dotenv import load_dotenv
from hikari import ModalInteraction, RESTBot

if TYPE_CHECKING:
    from hikari.api import InteractionMessageBuilder


def main() -> None:
    """Begin the bot's process."""
    load_dotenv()

    bot = RESTBot(token=environ["BOT_TOKEN"], public_key=environ["PUBLIC_KEY"])
    client = Client(app=bot)

    client.plugins.load("src.plugins.__main__")

    bot.set_listener(ModalInteraction, handle_preview_modal)  # type: ignore

    bot.run()


async def handle_preview_modal(
    inter: ModalInteraction,
) -> InteractionMessageBuilder | None:
    """Control all preview modals."""
    if inter.custom_id == f"preview_modal:{inter.user.id}":
        async with ClientSession() as session:
            data = {}
            data["authorID"] = inter.user.id
            data["content"] = inter.components[0].components[0].value

            async with session.post(f"{environ['API_URL']}/previews", data=data) as res:
                response = inter.build_response()
                json = await res.json()

                if res.ok:
                    url = f"{environ['API_URL']}/{json['id']}"
                    response.set_content(f"Here is your preview: {url}")
                else:
                    response.set_content(await res.text())

                return response
    else:
        return None


if __name__ == "__main__":
    main()
