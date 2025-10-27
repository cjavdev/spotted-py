# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .context_object import ContextObject
from ..shared.track_object import TrackObject

__all__ = ["PlayerListRecentlyPlayedResponse"]


class PlayerListRecentlyPlayedResponse(BaseModel):
    context: Optional[ContextObject] = None
    """The context the track was played from."""

    played_at: Optional[datetime] = None
    """The date and time the track was played."""

    track: Optional[TrackObject] = None
    """The track the user listened to."""
