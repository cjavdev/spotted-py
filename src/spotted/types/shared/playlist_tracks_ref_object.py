# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PlaylistTracksRefObject"]


class PlaylistTracksRefObject(BaseModel):
    href: Optional[str] = None
    """
    A link to the Web API endpoint where full details of the playlist's tracks can
    be retrieved.
    """

    total: Optional[int] = None
    """Number of tracks in the playlist."""
