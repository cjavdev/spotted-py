# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.show_base import ShowBase
from .shared.simplified_episode_object import SimplifiedEpisodeObject

__all__ = ["ShowRetrieveResponse", "ShowRetrieveResponseEpisodes"]


class ShowRetrieveResponseEpisodes(BaseModel):
    href: str
    """A link to the Web API endpoint returning the full result of the request"""

    items: List[SimplifiedEpisodeObject]

    limit: int
    """
    The maximum number of items in the response (as set in the query or by default).
    """

    next: Optional[str] = None
    """URL to the next page of items. ( `null` if none)"""

    offset: int
    """The offset of the items returned (as set in the query or by default)"""

    previous: Optional[str] = None
    """URL to the previous page of items. ( `null` if none)"""

    total: int
    """The total number of items available to return."""


class ShowRetrieveResponse(ShowBase):
    episodes: ShowRetrieveResponseEpisodes
    """The episodes of the show."""
