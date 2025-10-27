# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.artist_object import ArtistObject

__all__ = ["FollowingListResponse", "Artists", "ArtistsCursors"]


class ArtistsCursors(BaseModel):
    after: Optional[str] = None
    """The cursor to use as key to find the next page of items."""

    before: Optional[str] = None
    """The cursor to use as key to find the previous page of items."""


class Artists(BaseModel):
    cursors: Optional[ArtistsCursors] = None
    """The cursors used to find the next set of items."""

    href: Optional[str] = None
    """A link to the Web API endpoint returning the full result of the request."""

    items: Optional[List[ArtistObject]] = None

    limit: Optional[int] = None
    """
    The maximum number of items in the response (as set in the query or by default).
    """

    next: Optional[str] = None
    """URL to the next page of items. ( `null` if none)"""

    total: Optional[int] = None
    """The total number of items available to return."""


class FollowingListResponse(BaseModel):
    artists: Artists
