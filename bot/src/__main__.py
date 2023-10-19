"""The startup file for the bot."""

from crescent import Client
from dotenv import load_dotenv
from hikari import ModalInteraction

from src.impl.bot import Bot


def main() -> None:
    """Begin the bot's process."""
    load_dotenv()

    bot = Bot()
    client = Client(app=bot)

    client.plugins.load("src.plugins.__main__")

    bot.set_listener(
        ModalInteraction,
        bot.handle_preview_modal, # type: ignore[reportGeneralTypeIssues]
    )

    bot.run()


if __name__ == "__main__":
    main()
