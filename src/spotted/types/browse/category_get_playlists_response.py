# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.paging_playlist_object import PagingPlaylistObject

__all__ = ["CategoryGetPlaylistsResponse"]


class CategoryGetPlaylistsResponse(BaseModel):
    message: Optional[str] = None
    """The localized message of a playlist."""

    playlists: Optional[PagingPlaylistObject] = None
