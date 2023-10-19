"""Contains all types returned/used when making HTTP requests."""

from typing import TypedDict

__all__ = ("PreviewResponse",)


class PreviewResponse(TypedDict):
    """All data returned from fetching a preview."""

    id: str
    authorID: str
    content: str
